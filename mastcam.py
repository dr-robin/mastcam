from time import sleep
from picamera import PiCamera

#Take snapshot
def snapshot():
    #Initialize
    camera = PiCamera()

    #Settings
    camera.resolution = (1024, 768, framerate=30)
    camera.iso = 100

    #Start preview
    camera.start_preview()

    # Camera warm-up
    sleep(2)

    camera.shutter_speed = camera.exposure_speed
    camera.exposure_mode = 'off'

    # Image capture
    camera.capture('foo.jpg')

# Timelapse capture
def timelapse():
    camera = PiCamera()
    camera.start_preview()
    sleep(2)
    duration = list(range(0,1800, 5))
    for d in duration:
        for filename in camera.capture_continuous('img{counter:03d}.jpg'):
            print('Captured %s' % filename)
            sleep(d) # wait 5 seconds

# Video capture
def video():
    #Record video to file
    camera = picamera.PiCamera()
    camera.resolution = (640, 480)
    camera.start_recording('my_video.h264')
    camera.wait_recording(60)
    camera.stop_recording()

#Schedule times for timelapse capture using crontab
