---
author: Centurio
categories:
- Linux
- Raspberry Pi
date: "2020-09-25T20:00:00Z"
guid: https://centurio.net/?p=3378
id: 3378
tags:
- NTFS
title: Setup external USB disk as NTFS volume on Raspbian
url: /2020/09/25/setup-external-usb-disk-as-ntfs-volume-on-raspbian/
---
I intend to use an external 2.5" USB disk formatted as NTFS volume on my Raspberry Pi. Since its rather larger (5TB) I don&#8217;t want to use MBR but GPT instead. Here&#8217;s a short list of commands I&#8217;ve used to setup the disk.

Start by identifying the connected disk:

<pre class="wp-block-code"><code>> lsblk
NAME        MAJ:MIN RM  SIZE RO TYPE MOUNTPOINT
sda           8:0    0  4.6T  0 disk
└─sda1        8:1    0  4.6T  0 part
mmcblk0     179:0    0 14.9G  0 disk
├─mmcblk0p1 179:1    0  1.5G  0 part
├─mmcblk0p2 179:2    0    1K  0 part
├─mmcblk0p5 179:5    0   32M  0 part
├─mmcblk0p6 179:6    0   69M  0 part /boot
├─mmcblk0p7 179:7    0  8.2G  0 part /
├─mmcblk0p8 179:8    0  512M  0 part
└─mmcblk0p9 179:9    0  4.5G  0 part</code></pre>

My disk is sda. 

I now usually used fdisk as a partitioning tool. However, there&#8217;s a tool I can highly recommend. Its called parted and can be installed using:

<pre class="wp-block-code"><code>sudo apt-get install parted</code></pre>

Since I&#8217;ll want to use ntfs as file system, I&#8217;ll need to install the ntfs drivers:

<pre class="wp-block-code"><code>sudo apt-get install ntfs-3g</code></pre>

Now create a new GPT partition table:

<pre class="wp-block-code"><code>> sudo parted /dev/sda mklabel gpt
Warning: The existing disk label on /dev/sda will be destroyed and all data on this disk will be lost. Do you want to continue?
Yes/No? yes
Information: You may need to update /etc/fstab.</code></pre>

Now create a new partition with ntfs. I&#8217;ll use all of the available space, so its from 0 to 100%:

<pre class="wp-block-code"><code>> sudo parted -a opt /dev/sda mkpart primary ntfs 0% 100%
Information: You may need to update /etc/fstab.</code></pre>

Now format the disk in quick format with ntfs. It will label the partition as &#8222;SynoBackups&#8220;:

<pre class="wp-block-code"><code>> sudo mkfs.ntfs -L SynoBackups -Q /dev/sda1
Cluster size has been automatically set to 4096 bytes.
Creating NTFS volume structures.
mkntfs completed successfully. Have a nice day.</code></pre>

This label is very helpful in identifying the partition, even when it is connected to a different USB port. Using a device like sda might point to a different drive, so its better to use the label. This is one of the big advantages of using gpt in comparison to mbr.

Let&#8217;s see the label in action:

<pre class="wp-block-code"><code>sudo lsblk --fs
NAME        FSTYPE LABEL       UUID                                 MOUNTPOINT
sda
└─sda1      ntfs   SynoBackups 4EE12D1B5321171F
mmcblk0
├─mmcblk0p1 vfat   RECOVERY    525E-19E4
├─mmcblk0p2
├─mmcblk0p5 ext4   SETTINGS    ceb0ae64-8675-406b-8eed-2244c26814c8
├─mmcblk0p6 vfat   boot        8454-E385                            /boot
├─mmcblk0p7 ext4   root0       65678398-7f53-48ec-8452-c277500fb4e8 /
├─mmcblk0p8 vfat               AC0D-3FB1
└─mmcblk0p9 ext4               ff645116-fe34-43bf-a580-b89fa963085d</code></pre>

Note that there&#8217;s also a more specific id, the UUID. We will use this UUID later when we configure a default mount point in /etc/fstab.

Now we&#8217;ll try to mount the new partition. Create a folder to mount the partition and mount it manually:

<pre class="wp-block-code"><code>sudo mkdir /mnt/backups
sudo mount -o defaults /dev/sda1 /mnt/backups</code></pre>

Verify that the disk is mounted and try to write some stuff to it:

<pre class="wp-block-code"><code>> df -h
Filesystem      Size  Used Avail Use% Mounted on
/dev/root       8.0G  2.7G  4.9G  36% /
devtmpfs        457M     0  457M   0% /dev
tmpfs           462M     0  462M   0% /dev/shm
tmpfs           462M  6.2M  455M   2% /run
tmpfs           5.0M  4.0K  5.0M   1% /run/lock
tmpfs           462M     0  462M   0% /sys/fs/cgroup
/dev/mmcblk0p6   68M   23M   46M  33% /boot
/dev/sda1       4.6T  210M  4.6T   1% /mnt/backups

> sudo lsblk --fs
NAME        FSTYPE LABEL       UUID                                 MOUNTPOINT
sda
└─sda1      ntfs   SynoBackups 4EE12D1B5321171F                     /mnt/backups
mmcblk0
├─mmcblk0p1 vfat   RECOVERY    525E-19E4
├─mmcblk0p2
├─mmcblk0p5 ext4   SETTINGS    ceb0ae64-8675-406b-8eed-2244c26814c8
├─mmcblk0p6 vfat   boot        8454-E385                            /boot
├─mmcblk0p7 ext4   root0       65678398-7f53-48ec-8452-c277500fb4e8 /
├─mmcblk0p8 vfat               AC0D-3FB1
└─mmcblk0p9 ext4               ff645116-fe34-43bf-a580-b89fa963085d

> echo "success" | sudo tee /mnt/backups/file
success
> cat /mnt/backups/file
success
> rm /mnt/backups/file
> sudo umount /mnt/backups</code></pre>

Now we&#8217;ll add the partition to /etc/fstab so that it can be mounted automatically:

<pre class="wp-block-code"><code>UUID=4EE12D1B5321171F   /mnt/backups    ntfs    defaults        0       2</code></pre>

See that I&#8217;m now using the UUID instead of /dev/sda to mount the ntfs volume to /mnt/backups. We can test the new setting:

<pre class="wp-block-code"><code>> sudo mount -a
> df -h
Filesystem      Size  Used Avail Use% Mounted on
/dev/root       8.0G  2.7G  4.9G  36% /
devtmpfs        457M     0  457M   0% /dev
tmpfs           462M     0  462M   0% /dev/shm
tmpfs           462M  6.2M  455M   2% /run
tmpfs           5.0M  4.0K  5.0M   1% /run/lock
tmpfs           462M     0  462M   0% /sys/fs/cgroup
/dev/mmcblk0p6   68M   23M   46M  33% /boot
/dev/sda1       4.6T  210M  4.6T   1% /mnt/backups</code></pre>

I think this is a really nice change in mounting the volumes and will create a more stable configuration, regardless which USB port you&#8217;ve used to connect your drive.