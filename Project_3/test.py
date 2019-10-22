#import RPi.GPIO as GPIO
#import dht11
from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
from time import sleep
from datetime import date, datetime
import Adafruit_DHT             #For Adafruit DHT22 humidity sensor



DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 4                     #DHT22 data pin connected to Pin 4 of Raspberry Pi 3+ B


humidity,temperature = Adafruit_DHT.read_retry(DHT_SENSOR,DHT_PIN)    #Read value from sensor

#print("Temp={0:0.1f}*C  Humidity={1:0.1f}%".format(temperature, humidity))
 
# initialize GPIO
#GPIO.setwarnings(False)
#GPIO.setmode(GPIO.BCM)
#GPIO.cleanup()
 
# AWS IoT certificate based connection
myMQTTClient = AWSIoTMQTTClient("123afhlss456")
myMQTTClient.configureEndpoint("a3daou1o8cc7z7-ats.iot.us-east-1.amazonaws.com", 8883)
myMQTTClient.configureCredentials("/home/pi/Documents/ECEN-5783-Embedded-Interface-Design/Project_3/Amazon_Root_CA_1.pem", "/home/pi/Documents/ECEN-5783-Embedded-Interface-Design/Project_3/3d9d689c17-private.pem.key", "/home/pi/Documents/ECEN-5783-Embedded-Interface-Design/Project_3/3d9d689c17-certificate.pem.crt")
#myMQTTClient.configureOfflinePublishQueueing(-1)  # Infinite offline Publish queueing
#myMQTTClient.configureDrainingFrequency(2)  # Draining: 2 Hz
#myMQTTClient.configureConnectDisconnectTimeout(10)  # 10 sec
#myMQTTClient.configureMQTTOperationTimeout(5)  # 5 sec
 
#connect and publish
myMQTTClient.connect()
myMQTTClient.publish("thing01/info", "connected", 0)
 
#loop and publish sensor reading
while 1:
    now = datetime.utcnow()
    now_str = now.strftime('%Y-%m-%dT%H:%M:%SZ') #e.g. 2016-04-18T06:12:25.877Z
    #instance = dht11.DHT11(pin = 4) #BCM GPIO04
    #result = instance.read()
#    if result.is_valid():
    payload = '{ "timestamp": "' + now_str + '","temperature": ' + str(temperature) + ',"humidity": '+ str(humidity) + ' }'
    print (payload)
    myMQTTClient.publish("thing01/info", payload, 0)
#        sleep(4)
#    else:
#        print (".")
#        sleep(1)
