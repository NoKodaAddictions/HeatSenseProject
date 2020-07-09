from gpiozero import LED
from gpiozero import MotionSensor
import pygame as sound

sound.init()
pir = MotionSensor(4)
blue_led = LED(17)
blue_led.off()

while True:

    #pir.wait_for_no_motion()
    #print("Motion Stopped")
    pir.wait_for_motion()
    print("Motion Detected")
    sound.mixer.music.load("CarAlarm.mp3")
    sound.mixer.music.play()
    blue_led.on()
    pir.wait_for_no_motion()
    blue_led.off()
    print("Motion Stopped")
    