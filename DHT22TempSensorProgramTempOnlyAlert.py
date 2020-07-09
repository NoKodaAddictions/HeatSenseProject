import pigpio
import DHT22
from time import sleep
import pygame as sound

pi = pigpio.pi()

dht22 = DHT22.sensor(pi, 27)
dht22.trigger()

sleepTime = 2

sound.init()

def readDHT22():
    dht22.trigger()
    #humidity = '%.2f' % (dht22.humidity())
    temp = '%.2f' % (dht22.temperature())
    #return (humidity, temp)
    return (temp)

#for i in range(2):
    #temperature = readDHT22()
    #print("Temperature is: " + temperature + "C")
    #sleep(sleepTime)
while True:
    #humidity, temperature = readDHT22()
    temperature = readDHT22()
    #print("Humidity is: " + humidity + "%") 
    if float(temperature) >= 25:
        print("ALERT: Temperature Over 25C")
        sound.mixer.music.load("CarAlarm.mp3")
        sound.mixer.music.play()
    else:
        print("Temperature is: " + temperature + "C")
        sleep(sleepTime)