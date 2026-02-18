+++
date = '2025-11-09T08:03:55-07:00'
draft = false
title = 'Realtime BART Arrival Display'
description = 'Mini model of the old school BART platform displays with live data from the official BART API'
tags = ["esp32", "lcd", "howto", "bart"]
cover = 'hero.webp'
repository = 'https://github.com/filbot/bart-proxy'
+++

{{< img src="hero.webp" alt="AI generated image of the physical BART display" >}}

I have a love-hate relationship with BART. I’m grateful for it, but let’s just say it’s not always the most reliable so it's nice to see before hand when the train you need is due to arrive. There are plenty of projects out there that show real-time BART arrival information. This one does that too, it’s nothing groundbreaking, but I wanted to build my own version that captures the vintage BART platform sign vibe I associate with commuting between the East Bay and my job in the city.

{{< img src="orinda-platform-sign.webp" alt="BART platform sign at the Orinda BART station" >}}

---

## The Hardware

- Seeed Studio XIAO ESP32C6 
- SPI Red 20x4 Character OLED Display Module from [BuyDisplay](https://www.buydisplay.com/spi-red-20x4-character-oled-display-module-for-arduino-raspberry-pi)
- SparkFun Logic Level Converter

I wanted to find a display that felt as close as possible to the real thing, though I knew it wouldn’t be an exact match. I was mainly after the right vibe, and the BuyDisplay red OLED character display nailed it. The PCB was a bit taller than the display itself, which affected the final dimensions, but it was a tradeoff I was happy to make. I love an OLED.

{{< img src="raw-display.webp" alt="buydisplay connected and testing" >}}

The only other components I needed on the electronics side were the ESP32-C6 to run the display and fetch the latest BART arrival times, along with a logic level shifter. Both parts are small, so I soldered them onto a piece of perfboard with header pins, allowing the whole assembly to plug directly into the display like a cartridge.

{{< img src="yellow-wire-solder.webp" alt="perf board back side" >}}
{{< img src="module-cartridge.webp" alt="electronic modules plugged into display" >}}

---

## Firmware

The official BART API uses [GTFS Realtime](https://www.bart.gov/schedules/developers/gtfs-realtime), a data specification developed in collaboration with Google. I’d never worked with it before, and expecting the ESP32 to fetch and parse the raw feed on its own felt like a stretch (or at least, too much for me to figure out). So instead, I built a middleware service that handles the heavy lifting: it pulls the data, extracts only what I need, and serves a simplified API tailored for the display the ESP32 calls. All the code is available on my [GitHub](https://github.com/filbot/bart-proxy).

---

## Demo

Once I had all the pieces together, including some early 3D prints of the housing, I assembled everything to get a feel for the scale and how it works as a finished product. This video shows it all together but before paint. Data is being pulled in live.

{{< video src="demo.mp4" >}}

---

## Finishing

All that was left to do was some post processing of the 3d prints and paint, along with some little details like screws and stickers of the company that made the real deal platform signs and which platform the sign was for. I used a Brothers label maker for both. 3D files are available to download on [Makerworld](https://makerworld.com/en/models/1979236-mini-bart-platform-display).

{{< img src="sanding-priming.webp" alt="3D parts post processing" >}}
{{< img src="brand-sticker.webp" alt="Brother label printed stickers" >}}

---

## Result

I used double-stick tape to mount this under a metal shelf above my monitor. Now I can see upcoming train arrivals at a glance, and the display also shows the time and official BART platform safety messages, like staying behind the yellow line, which really makes it feel like I’m standing on the platform. Sure, I could just look it up online, but having this miniature version of the platform display on my wall is much more fun.

{{< img src="finished-display.webp" alt="Finished display" >}}