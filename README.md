# Smite-Cane

## ❓ Problem Statement

Without vision, can you imagine how challenging it would be for a visually impaired person to navigate through the pathway without bumping into obstacles?
Even if you use a normal white cane there might be chances that you could fall or your cane gets stuck somewhere in the hurdle.
The problems that visually impaired people face includes:
* Detecting hurdles
* Finding Path
* Hit with speeding object

## 😎 Solution

* Giving them a new vision and environment to visually impaired people. 

Smite Cane (Smart White Cane) provides the blind people or visually impaired people, a hearable environment that focuses on the field of assistive devices.
It converts visual data by image processing into an auditory modality that will assist the user with a robotic vision through speech.
It contains: 
* A Raspberry Pi 
* An artificial intelligence module.
* Ultrasonic sensor
* A Motor
* A Pi camera or a webcam and 
* Headphones/Speakers

On pressing the button on the cane, the camera module will start taking real-time video stream and analyze it using the Caffe Model(Artificial Intelligence Module using OpenCV) to detect the object/person, and then using a speaker or headphone, the cane will voice assist the person about the environment. 
Also, we are attaching a motor for vibrations so that the detected object will be translated into Morse code since visually impaired people are already trained about it and the vibrations in the motor will be according to the frequency of Morse code. This feature will not only help the blind but also the deaf people about the environment and guide through the path.

## 🌟 Features of our product

* Object/Person Detection using MobileNet_V2.
* Real time text to speech conversion of object detected.
* Optical Character Recognition for large street signs.
* Haptic Feedback using motor via response from ultrasonic sensor.
* Location logging using location magic.
* Emergency button is used to send the live location to thier dear ones using Twilio Communication API.
* Translation of detected hurdle to Morse Code.

## ✅ Scalability

Most of the visually impaired people are aged 50 years and above. The burden of visual impairment in India is estimated at 62 million; of these, 54 million persons have low vision, and 8 million are blind.
Out of every 5 visually impaired people atmost 2 of them meets with a road accident.
https://www.jfmpc.com/article.asp?issn=2249-4863;year=2019;volume=8;issue=4;spage=1432;epage=1439;aulast=Vignesh#:~:text=Most%20of%20the%20visually%20impaired,and%208%20million%20are%20blind.

## 😊 Our Impact

* The Person with our cane will get alerted if there is a hurdle ahead. 
* The Person with our cane will be able to walk freely without any fear of accidents.
* Our cane will provide speech assistance to the user and guide them the path.
* In case, the user is deaf our cane will vibrate according to the frequency of Morse Code of the detected hurdles.

## 🛠️ Software Used

* OpenCV
* MobileNet_V2
* pyttsx3
* Twilio Communication API
