---
layout: post
title: "Convert an OSX dmg to an iso"
---

### Creating ISOs for use with VirtualBox and more


If you want to run OSX in a virtual machine, you need the OS as an image. If you are using the wonderful (read: free) [Oracle VirtualBox](https://www.virtualbox.org/), you are going to need said image in the "iso" format. Just follow the steps below to convert the OSX installer app you would get from the App Store into a workable iso format for VritualBox.

There really is only one step but I will break it down into smaller steps for clearity.

1. Locate InstallESD.dmg which is the image file we will be converting. Its typically located inside the installer app for OSX. Right click on the installer app and select "Show contents".

2. Go to `/Contents/SharedSupport/`

3. Open Terminal and run the following command:

`hdiutil makehybrid -iso -hfs /Path/to/InstallESD.dmg -o OSX.iso`

Here is a screenshot of what Terminal should look like.
<img src="{{ site.url }}/assets/images/dmg-to-iso/terminal.png">

It will take a little while, but once finished, you will have an iso version of the install image for use with VirtualBox or anything else that requires an iso.