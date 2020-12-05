# HeatWatcher Project

Hello Everyone!

This project is to prevent children from dying of a heat stroke. This solution was created because
we see many instances of adults/parents leaving their child in a locked, hot car either accidentaly
or purposely. This can lead to tragic consequences where the child can suffer from a heat stroke.
In 2019, a total of 51 cases were reported of children being locked in a car. Many people say that
they "will be back in a couple of minutes" or "I'm just going to grab one thing". But what you didn't
know is that temperatures can spike quickly from 70 deg F to 172 deg F in a matter of minutes, depending
on where you are of course. You see, the car is like a greenhouse. If your car is sitting in direct
sunlight, that is when the car can turn into an oven because the heat is being trapped on not let out
(This is the same concept of golbal warming!). To solve this, I have created a device using Raspberry Pi
as the brains of the operation. Along with a PIR Motion Sensor and a DHT22 Temperature/Humidity sensor,
I am able to create a system that can detect temperature and motion and send an alert via speaker to
alert someone that a car is heated up and there is someone inside.

## Proof Of Concept

If temp sensor detects a temperature over 78 deg F or 25 dec C:
  Check for motion
  If motion is detected:
    Send a text message (Represented by alarm) to adult or trusted one.

What you see are the 3 final files for the modules. PIR and DHT22. The first 2 programs were made to
seperately control the modules. Then, the 3rd program is the final combination of the 2.
