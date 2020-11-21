import RPi.GPIO as GPIO
import time
import numpy as np
GPIO.setmode(GPIO.BCM)
#
#TRIG1 = 26
#ECHO1 = 19
#
#TRIG2 = 5
#ECHO2 = 6
#
#TRIG3 = 17
#ECHO3 = 27
#print ("Distance Measurement In Progress")
#
#GPIO.setup(TRIG1,GPIO.OUT)
#GPIO.setup(ECHO1,GPIO.IN)
#GPIO.setup(TRIG2,GPIO.OUT)
#GPIO.setup(ECHO2,GPIO.IN)
#GPIO.setup(TRIG3,GPIO.OUT)
#GPIO.setup(ECHO3,GPIO.IN)
#
#print ("Waiting For Sensor To Settle")
#time.sleep(2)
#
#GPIO.output(TRIG, True)
#time.sleep(0.00001)
#GPIO.output(TRIG, False)
#
#while GPIO.input(ECHO)==0:
#  pulse_start = time.time()
#
#while GPIO.input(ECHO)==1:
#  pulse_end = time.time()
#
#pulse_duration = pulse_end - pulse_start
#
#distance = pulse_duration * 17150
#
#distance = round(distance, 2)
#
#print ("Distance:",distance,"cm")
#
#GPIO.cleanup()

min=80
sensors = []
hapt_feed=27
SENSOR_SETTLE_TIME = 0.00001

MEASURE_INTERVAL_TIME = 0.1 # time delay to measure (min 15miliseconds)                 

# max distance threshold for sensors to react (in cm)
MAX_DISTANCE_THRESHOLD = 5.0

# Speed of sound at sea level = 343 m/s or 34300 cm/s
MEASURE_REFERENCE = 17150
GPIO.cleanup()
# sensor1 with pin configuration
sensor1 = {'ID': "1", 'TRIG': 26, 'ECHO': 19}
sensors.append(sensor1) # add to the list
# sensor2 with pin configuration
sensor2 = {'ID': "2", 'TRIG': 5, 'ECHO': 6}
sensors.append(sensor2) # add to the list
# sensor3 with pin configuration
sensor3 = {'ID': '3', 'TRIG': 20, 'ECHO': 21}
sensors.append(sensor3) # add to the list
# sensor4 with pin configuration
def initPins():
    if len(sensors) > 0:
        for sensor in sensors:
            #Sensor's echo pins shoud be in
            GPIO.setup( sensor['ECHO'], GPIO.IN );

            #Sensor's trig pins should be out
            GPIO.setup( sensor['TRIG'], GPIO.OUT );
initPins()
GPIO.setup(hapt_feed, GPIO.OUT);
def measure(sensor):
        print ("Measurement started for " + sensor['ID'] + ", Ctrl+z to cancel the measurement");
        distanceRound=[0,0,0,0,0]
        for i in range (0,5,1):

                GPIO.output(sensor['TRIG'], GPIO.LOW);
                time.sleep(MEASURE_INTERVAL_TIME); #DELAY

                GPIO.output(sensor['TRIG'], GPIO.HIGH);

                time.sleep(SENSOR_SETTLE_TIME);

                GPIO.output(sensor['TRIG'], GPIO.LOW);

                while GPIO.input(sensor['ECHO']) == 0:
                    pulse_start = time.time();

                while GPIO.input(sensor['ECHO']) == 1:
                    pulse_end = time.time();

                pulse_duration = pulse_end - pulse_start;

                distance = pulse_duration * MEASURE_REFERENCE;
                distanceRound[i] = round(distance, 2);
        a= np.array(distanceRound)
        median=np.median(a)
        #print median
        
        print ("Distance of sensor "+ sensor['ID'] + " : ", median, "cm");
        return median
try:
    while True:
        for sensor in sensors:
            if(sensor['ID']== "1"):
                D1=measure(sensor)
            elif(sensor['ID']== "2"):
                D2=measure(sensor)
            elif(sensor['ID']== "3"):
                D3=measure(sensor)
        print (D1)
        print (D2)
        print (D3)
        if(D1< min or D2< min or D3<min):
            GPIO.output(hapt_feed, GPIO.HIGH);
        else:
            GPIO.output(hapt_feed, GPIO.LOW);
except KeyboardInterrupt:
    GPIO.output(hapt_feed, GPIO.LOW);
    print ('Interrupted')
    pass            
finally:
    GPIO.output(hapt_feed, GPIO.LOW);
    GPIO.cleanup()
