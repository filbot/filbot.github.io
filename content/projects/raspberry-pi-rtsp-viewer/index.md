+++
date = '2025-09-15T08:03:55-07:00'
draft = false
title = 'RTSP Video Stream on Raspberry Pi'
description = 'How to build a Raspberry Pi configured to act as a simple, dedicated fullscreen RTSP video display.'
tags = ["raspberry-pi", "lcd", "howto", "unifi", "ubiquity", "rtsp"]
cover = 'hero.jpg'
+++

{{< img src="hero.jpg" alt="ChatGPT generated image of the cube" >}}

My doorbell camera provides an RTSP stream, which made me think it would be perfect to display on a small dedicated screen. I built this using Jay Doscher’s excellent [ARM Terminal 2 - The Cube](https://www.doscher.com/arm-terminal-2-the-cube/). I highly recommend taking a look at his blog, because if you're reading this, you're gonna love his stuff, [doscher.com](https://www.doscher.com).

---

## The Hardware

- Raspberry Pi 4 running Raspberry Pi OS Lite (Bookworm)
- [Geekworm Raspberry Pi 4 Heatsink](https://www.amazon.com/dp/B08N5VZN8R?ref=ppx_yo2ov_dt_b_fed_asin_title&th=1)
- [Waveshare 4inch HDMI LCD (C)](https://www.waveshare.com/wiki/4inch_HDMI_LCD_(C))
- [ARM Terminal 2 - The Cube](https://www.doscher.com/arm-terminal-2-the-cube/)
- Repurposed metal adjustable arm - [Example on Amazon](https://www.amazon.com/dp/B08FNQC6TZ?ref_=ppx_hzsearch_conn_dt_b_fed_asin_title_6&th=1)

{{< img src="top-down-labels.jpg" alt="Labeled photo of hardware" >}}

My metal arm originally had a lamp attached, so I removed the lamp and saved it for parts. The clamp that came with the arm is not the strongest, but it works fine for the weight of this project. With a little creativity, you can attach it almost anywhere. I mounted mine to a monitor arm so I could position the screen just above my secondary monitor.

The 3D-printed frame pieces from doscher.com came out great. I followed the instructions and parts list from Jay’s blog. 

Fitting the Pi and display into the frame takes a little patience, but once they are in place, it is very solid. I used a 90-degree USB-C cable to route power neatly out the back and zip-tied it along the arm for clean cable management.

{{< img src="pi-closeup.jpg" alt="raspberry pi closeup" >}}

> The display connects to the Pi with an HDMI adapter and draws power through pogo pins so no wires involved, which is a nice touch.

The only custom part I made was a small adapter plate to attach the cube to the arm using the peg from the old lamp mount. The metal peg had a curved plate to match the radius of the lamp housing but I was able to hammer it flat. The 3d printed adapter is just a square with screw holes and a larger hole for the peg. Thumb screws came from jar of screws I keep exactly for these types of situations.

{{< img src="mounting-bracket.jpg" alt="mounting bracket" >}}

---

## The Software

For playback I used GStreamer with a set of plugins for RTSP decoding and video handling, along with Cage, a minimal Wayland compositor that runs a single app in fullscreen mode.

{{< img src="pi-booting.jpg" alt="raspberry pi booting" >}}

Here is what the pipeline does:

- Connects to the RTSP stream (rtspsrc)  
- Depayloads and parses H.264 (rtph264depay ! h264parse)  
- Hardware-decodes with the Pi’s V4L2 (v4l2h264dec)  
- Crops the 960×720 source to keep the right-hand 720×720 region (videocrop left=240)  
- Scales to the LCD resolution (videoscale ! video/x-raw,width=720,height=720)  
- Displays fullscreen inside Cage (waylandsink) 

The first script is the meat of this project. It should be easy enough to edit for anyone thinking about using it for their own display, if your display has a different resolutions, and if your video feed needs a different resolution or crop.

```bash
#!/usr/bin/env bash
set -euo pipefail

# --- CONFIG ---
URL='rtsp://192.168.1.1:7447/tDm5IQb26KLGtQ4t'
CROP_LEFT=240 # 960x720 source -> keep RIGHT side
OUT_W=720; OUT_H=720
FPS="30/1"
RETRY_SEC=3
CONNECT_TIMEOUT_US=5000000 # 5s timeout

# --- Pipelines ---
stream_cmd=(
  gst-launch-1.0 -v
  rtspsrc location="$URL" latency=0 timeout=$CONNECT_TIMEOUT_US protocols=tcp
    ! rtph264depay ! h264parse ! v4l2h264dec
    ! videoconvert
    ! videocrop left=$CROP_LEFT
    ! videoscale
    ! "video/x-raw,width=$OUT_W,height=$OUT_H,framerate=$FPS"
    ! waylandsink fullscreen=true sync=false
)

nosignal_cmd=(
  gst-launch-1.0 -q
  videotestsrc pattern=black
    ! "video/x-raw,width=$OUT_W,height=$OUT_H,framerate=$FPS"
    ! textoverlay text="NO SIGNAL" font-desc="Sans 64" halignment=center valignment=middle color=0xFFFFFFFF
    ! waylandsink fullscreen=true sync=false
)

probe_cmd=(
  gst-launch-1.0 -q
  rtspsrc location="$URL" timeout=$CONNECT_TIMEOUT_US protocols=tcp
    ! rtph264depay ! h264parse ! avdec_h264
    ! fakesink sync=false
)

# --- Loop forever: stream or fallback ---
while true; do
  "${stream_cmd[@]}" && continue
  "${nosignal_cmd[@]}" & NS_PID=$!
  until "${probe_cmd[@]}" >/dev/null 2>&1; do
    sleep "$RETRY_SEC"
  done
  kill "$NS_PID" 2>/dev/null || true
  wait "$NS_PID" 2>/dev/null || true
done
```

---

## Running as a Service

The second part of this is the potatoes. Create a systemd service file so the Pi runs this automatically at boot.

```bash
# /etc/systemd/system/cam-kiosk.service
[Unit]
Description=RTSP Kiosk (Cage + GStreamer) with NO SIGNAL fallback
After=network-online.target
Wants=network-online.target

[Service]
User=pi
PAMName=login
TTYPath=/dev/tty1
StandardInput=tty
Environment=XCURSOR_THEME=blank
Environment=XCURSOR_SIZE=1
ExecStart=/usr/bin/cage -m -- /usr/local/bin/cam-player.sh
Restart=always
RestartSec=2

[Install]
WantedBy=multi-user.target
```

Enable and start the service:

```bash
sudo systemctl enable cam-kiosk.service
sudo systemctl start cam-kiosk.service
```

Check logs if you need to debug:

```bash
sudo journalctl -u cam-kiosk.service -f
```

If you are still editing the script, stop the service first:

```bash
sudo systemctl stop cam-kiosk.service
```

Then run your script manually. Remember to restart the service when finished. Each time the pi reboots, the feed should show up on its own.

---

## The Result

The LCD has a native 720x720 resolution, but the doorbell feed is 960x720. The script crops 240 pixels from the left side so the image fits perfectly. The cropped area was just more of my front door, so nothing important was lost. The video delay is minimal, about the same as viewing through the official app. The one thing still left to do on this is to "hide" the cursor. Its so small on this display that it doesn't really bother me, but I don't think it would be hard to do and would be a nice finishing touch.

{{< img src="rtsp-stream.jpg" alt="RTSP stream" >}}

This has been more useful than I expected. It is great to glance over and see what is happening at the front door. You can of course use any RTSP stream. Maybe you want to display a public webcam or a traffic camera in your area. The possibilities are wide open.
