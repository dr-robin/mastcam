# mastcam

This is a short script to capture and save timelapse images using the raspberry pi zero.
The camera will be located on a sailboat at the top of the mast. Files will be saved locally, then uploaded when wifi is avaliable.

# Notes on setting up pi zero w v1.1
* Download and install Stretch Lite Raspbian 2017 (source below)
http://77.161.176.191/domoticx/diskimages/raspberry_pi_raspbian/?sort_by=mod&sort_as=asc&dir=

* Create an empty file and save file as 'ssh'. Dump file into boot partition of microSD card.

* Create another new file and save as 'wpa_supplicant.conf'. Add the following, save and dump file into boot partition again. 
'''
country=US
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1

network={
    ssid="your_real_wifi_ssid"
    scan_ssid=1
    psk="your_real_password"
    key_mgmt=WPA-PSK
}
'''

* Find IP address of pi zero by logging into wifi hub as admin. The pi zero will be a device connected over 2.4hz.
* Remote access pi zero using ssh
  '''
  ssh pi@[IP address]
  pwd: raspberry
  '''
* After successful login, change default password
 `passwd`
