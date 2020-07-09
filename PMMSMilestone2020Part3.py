import pigpio
import DHT22
from time import sleep
import pygame as sound
from gpiozero import MotionSensor
from gpiozero import LED

pi = pigpio.pi()

dht22 = DHT22.sensor(pi, 27)
dht22.trigger()
sound.init() 
pir = MotionSensor(4)
blue_led = LED(17)
blue_led.off()

sleepTime = 2

sound.init()

def readDHT22():
    dht22.trigger()
    #humidity = '%.2f' % (dht22.humidity())
    temp = '%.2f' % (dht22.temperature())
    #return (humidity, temp)
    return (temp)

while True:
#   print("Motion Detected")
    #humidity, temperature = readDHT22()
    temperature = readDHT22()
    #print("Humidity is: " + humidity + "%") 
    if float(temperature) >= 25:
        print("ALERT: Temperature Over 25C")
        pir.wait_for_motion()
        #print("Motion Detected")
        print("!HIGH TEMPERATURE ALERT!|Please Check Your Vehicle. Motion Detected Inside.")
        blue_led.on()
        sound.mixer.music.load("CarAlarm.mp3")
        sound.mixer.music.play()
    else:
        print("Temperature is: " + temperature + "C")
        sleep(sleepTime)
        blue_led.off()