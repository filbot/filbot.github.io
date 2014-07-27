---
layout: post
title: "Time Machine Backups with FreeNAS"
---

### Configuring FreeNAS as a destination for Time Machine backups


[FreeNAS](http://www.freenas.org/) is a free network attached storage system that has both enterprise grade options as well as small business/home functionality. It also has an amazing community around it and full time developers constantly imporving it. In this post, I'll talk about how I stetup freeNAS to act as a destination for Time Machine backups for multiple computers. I've broken the project out into three sections. Installing FreeNAS. Configuring FreeNAS. Configuring Time Machine.


You will need the following:
- [FreeNAS image](http://www.freenas.org/download-releases.html) on a USB drive or other bootable media
- Computer with enough storage to perform backups

Start by creating a bootable install image of Freenas. Bootable media must be at least 2GB. Once the image is done, you will have a bootable thumbdrive/card or CD-ROM with the FreeNAS software on it.

To create a bootable thumbdrive or compact flash card:
1. Uncompress the FreeNAS image using [The Unarchiver](https://itunes.apple.com/us/app/the-unarchiver/id425424353?mt=12)
2. Insert the thumbdrive/card
3. Launch Disk Utility and format the thumdrive/card with the "Free Space" option and a single partition
<img src="{{ site.url }}/assets/images/timemachine-freenas/diskutil.png">
4. Luanch Terminal and run `diskutil list` to find the name of the thumbdrive/card inserted in the computer
<img src="{{ site.url }}/assets/images/timemachine-freenas/diskutil-list.png">
This lists the storage devices on your machine. Look for the thumbdrive/card in the list. If you have trouble figuring out which one it is. Run this command without the thumbdrive/card and then again with it in and compare the differece. Make note of the device path. It will be used in the next step.
5. In a terminal, unmount the thumbdrive/card
{% highlight bash %}
diskutil unmountDisk /dev/disk1
Unmount of all volumes on disk1 was successful
{% endhighlight %}
6. use the `dd` command to write the image to the thumbdrive/card
{% highlight bash %}
dd if=FreeNAS-9.1.1-RELEASE-x64.img of=/dev/disk1 bs=64k
{% endhighlight %}

FreeNAS will now run from your thumbdrive/card. This is the prefered method as it doesn't take up any disk space on the NAS.

To create a bootable CD-ROM using Disk Utility (Mac OS X 10.3 or later):

1. Open Disk Utility, in the Utilities folder (/Applications/Utilities).
2. If the disk image you want to use doesn't appear in the list, drag its icon to the Disk Utility window.
3. Select the disk image and click Burn.
4. Insert a blank CD or DVD into your computer's optical drive and follow the onscreen prompts.

Once the image is burned onto the disk. Insert it into your machine and follow the promts to install FreeNAS.

Configuring User Accounts:

Create a user account for every user in the network where the name of each account is the same as a logon name used on a computer. For example, if a OS X system has a login name of bobsmith, you should create a user account with the name bobsmith on FreeNAS®. If your intent is to assign groups of users different permissions to shares, you will need to also create groups and assign users to the groups.

<img src="{{ site.url }}/assets/images/timemachine-freenas/add-user.jpeg">



Configuring FreeNAS Volumes:

FreeNAS runs independently of the storage discs in your system. You have to configure at least one volume to actually be able to use the storage as network-attached storage. FreeNAS gives you the option of either UFS or ZFS volumes. ZFS volumes are recommended to get the most out of your FreeNAS® system.

1. Click the storage icon at the top of the admin interface
2. Launch the ZFS Volume Manager
3. Name your volume and select which discs you would like to use. FreeNAS will suggest the best configuration given the number and types of discs selected
4. Click on Add Volume

<img src="{{ site.url }}/assets/images/timemachine-freenas/add-volume.png">

Now that you have a volume, lets create a dataset on said volume to use as our Time Machine backup storage space. Datasets are like partitions that can have there own limits, quoatas, and permissions. Go ahead and create a dataset by selecting your volume and clicking dataset along the bottom of the window. Name your dataset and and press add dataset.


Configure Shares:

1. Click the Sharing button at the top of the admin screen
2. Make sure Apple (AFP) is selected and click on Add Apple (AFP) Share
3. Fill out the form with the following attributes:
- Path to designated dataset
- Allow List set to user account created earlier
- Read-write Access set to user account created earlier
- Disk Discovery checkbox checked
- Disck Discovery mode set to Time Machine
4. Configure the Services -> AFP service as follows:
- Set server name e.g. "freenas"
- Guest Access checkbox is unchecked
5. Start AFP service


Configure time machine on each computer:

To configure Time Machine on the Mac OS X client, go to System Preferences → Time Machine which will open the screen shown in Figure 7.1e. Click ON and a pop-up menu should show the FreeNAS® system as a backup option. In our example, it is listed as backup_user1 on "freenas". Highlight the entry representing the FreeNAS® system and click the "Use Backup Disk" button. A connection bar will open and will prompt for the user account's password--in this example, the password for the user1 account.

<img src="{{ site.url }}/assets/images/timemachine-freenas/time-machine-settings.png">

Time Machine will create a full backup after waiting two minutes. It will then create a one hour incremental backup for the next 24 hours, and then one backup each day, each week and each month. Since the oldest backups are deleted when the ZFS dataset becomes full, make sure that the quota size you set on the dataset is sufficient to hold the backups. Note that a default installation of Mac OS X is ~21GB in size.


This walkthrough only scratches the surface of what's possible with FreeNAS. The [official documentation](http://doc.freenas.org/index.php/Main_Page) is pretty great and there are a bunch of writups just like this one on all the various storage and service configurations possible with FreeNAS.