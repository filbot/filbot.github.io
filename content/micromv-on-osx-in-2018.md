+++
date = '2018-10-05T11:51:48-07:00'
draft = false
title = 'MicroMV on OS X in 2018'
description = 'How to digitize your old MicroMV tapes on a modern Apple computer using legacy hardware and software tools like AVCVideoCap and HandBrake'
tags = ['howto', 'osx']
+++

![micromv-header-image](/assets/micromv-on-osx-in-2018/micromv-header.png)

What you need:
- Apple Thunderbolt to FireWire Adapter
- MicroMV playback device with FireWire port
- FireWire cable
- MicroMV tapes with footage
- Apple computer running OS X 10.6 or higher
- AVCVideoCap software ([download](https://nofile.io/f/mNaGHHh9297/AVCVideoCap.app.zip))

Once you have all the hardware needed to connect everything up to a computer, turn it all on, insert the tape you want to ingest, and fire up the free AVCVideoCap application (download), which is actually a small app written by Apple to show off some capabilities of the FireWire protocol in XCode back in the day when FireWire was a thing. If when opening the app, you get a message like:

![Opening an app from an unidentified developer](/assets/micromv-on-osx-in-2018/micromv-warning-screenshot.png)

right-click on the file and select open from the menu. After all that you will be presented with a screen that looks like this:

![AVCVideoCap app window with device listed](/assets/micromv-on-osx-in-2018/micromv-device-list.png)

Your device should be listed in this window. I used a Sony DCR-IP5 camera for this but the procedure should be largely the same for most devices. Put your device in “playback” mode and rewind the tape to the start. The AVCVideoCap app has tape control functions which can start the tape playback on capture but it will start wherever the tape is currently so make sure to rewind to where you want to start capturing. When you are ready, hit “Capture From Device” and you will be presented with this window:

![Capture file creation window](/assets/micromv-on-osx-in-2018/micromv-capture-screenshot.png)

Here you have the opportunity to name the file, which will be captured as a raw stream with the file extension m2t, and to choose a location for the file. Hit save and then make sure to select “Tape Control” from the drop down so that the software knows to start playback of the tape for capturing. The other option is for capturing live streams of video coming through FireWire such as video coming out of a cable box.

![Window showing Tape Control as the selected option](/assets/micromv-on-osx-in-2018/micromv-recording-mode-screenshot.png)

Once you press “Continue” to start the capture, your device should start playback in real-time and the data stream coming through the FireWire cable will begin saving to the file and location you specified earlier. Again, this is real time so sit back and let it do its thing until its played through all the footage you wish to capture. Aborting the capture will stop the process and keep whatever was played through, or if you wait until either the footage on the tape runs out or the tape itself runs out, the app will stop the capture process automatically.


From here, you are left with a file format that few apps can play back and even fewer apps can edit. The simplest solution is to use [HandBrake](https://handbrake.fr/), a free video conversion app, to convert the m2t file into something more usable in today's ecosystem of playback and editing apps. I used the default mp4 settings from HandBrake but feel free to play with this to get the file exactly how you want.