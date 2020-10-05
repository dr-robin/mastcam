#requirements Huawei E303 Stick or Huawei E3531s Stick

#check for drivers
lsusb

#install drivers
sudo apt-get install usb-modeswitch --yes

#confirm drivers installed
lsusb

sudo reboot

#check network interfaces - usb0
ifconfig -a

#open 192.168.1.1
#enter pin code
# Settings> Connection> Profile Management.
#create a new profile, APN - dynamic
#Connection> Mobile Connection ==> activate
#open webpage to check 3G connection

#to load 3G on reboot
sudo nano /etc/network/interfaces

#add lines in iface eth0 or wwan0 (instead of usb0)
allow-hotplug usb0
iface usb0 inet dhcp

#to switch back to Wifi instead of 3G
#comment out lines in /etc/network/interfaces
