+++
date = '2026-02-09T05:03:55-07:00'
draft = false
title = 'Hero Dashboard'
description = 'Emergency Services dashboard running on a Raspberry Pi kiosk'
tags = ["raspberry pi", "application", "howto"]
cover = 'dashboard-angle.jpg'
+++

{{< img src="dashboard-angle.jpg" alt="Hero Dashboard" >}}

The Seattle city government provides a public API for fire department emergency dispatch data. There’s a very cool project, [SFD Live](https://sfdlive.com), that visualizes this information (and a lot more) with a ton of features.

What I wanted, though, was something much simpler: a stripped-down view of the data that would be interesting, if not especially useful, on a dashboard I could glance at from across the room. I had an old monitor and a spare Raspberry Pi lying around, so slapping those together and running a web app in kiosk mode on the Pi felt like the perfect excuse for a small side project.

---

## The Hardware

- Raspberry Pi 5
- Any display, mine is an old Dell 4k panel

---

## Setup

Using Raspberry Pi Imager, I flashed FullPageOS onto the Raspberry Pi and configured it according to the project’s instructions to display the dashboard page on boot.

The code for the Hero Dashboard can be found on my GitHub:
https://github.com/filbot/emergency-map

It’s a simple React app that can be run in a Docker container or deployed however you normally run your React applications.

{{< img src="dashboard-running.png" alt="Hero Dashboard app running" >}}
> Screenshot of app running

The display itself is mounted to an IKEA Skådis pegboard using a 3D-printed VESA mount designed specifically for the Skådis system. It’s a clean, flexible setup and makes the whole thing feel a bit more like a “command center” movie prop, which was the vibe I was after.

---

## Dashboard

Each active call is represented by a red dot on the map. The map automatically scales to encompass all current calls, and a list of those calls is displayed in the panels below. There’s also a countdown timer showing when the next data refresh will occur as well as a count of how many current incidents are displayed.

There’s no real-world utility for this data in my day-to-day life, it’s mostly just a fun prop to have running in my office. That said, the data itself obviously isn’t “fun.” Some of these points represent genuinely bad days for real people.

I don’t call it the Hero Dashboard for nothing, though. The men and women who respond to these calls are the best of us. For me, this display is a quiet reminder that things happen every day, and that there are people who choose to show up and help when they do.

{{< img src="dashboard-mounted.jpg" alt="Hero Dashboard mounted above my workbench" >}}
> Wide shot of where the dashboard lives