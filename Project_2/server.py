import tornado.httpserver
import tornado.websocket
import tornado.ioloop
import tornado.web
import socket
import json
import os
from serial import *
import Adafruit_DHT             #For Adafruit DHT22 humidity sensor
import prototype_1 as project_1 
from dbManager import DatabaseUtility
import base64

tordbu = DatabaseUtility("eid_proj_1", "prototype_table")

'''
This is a simple Websocket Echo server that uses the Tornado websocket handler.
Please run `pip install tornado` with python of version 2.7.9 or greater to install tornado.
This program will echo back the reverse of whatever it recieves.
Messages are output to the terminal for debuggin purposes. 
''' 
DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 4                     #DHT22 data pin connected to Pin 4 of Raspberry Pi 3+ B

class WSHandler(tornado.websocket.WebSocketHandler):
    def open(self):
        #self.tordbu = dbManager.DatabaseUtility(eid_proj_1, prototype_table)
        print ("new connection")
      
    def on_message(self, message):
        print ('message received:  %s' % message)
        if message == "Temperature":
            #make a dictionary
            humidity,temperature = Adafruit_DHT.read(DHT_SENSOR,DHT_PIN)
            #If value not obtained, try for a max of 10 times until value is obtained        
            if humidity is None and temperature is None:
                for i in range(0,10):
                    humidity,temperature = Adafruit_DHT.read(DHT_SENSOR,DHT_PIN)
                    if humidity is not None and temperature is not None:
                        print("Got Temperature, Breaking Loop")
                        break
            
            latest_data = {"temp": temperature, "hum": humidity}
            
            #turn it to JSON and send it to the browser
            self.write_message(json.dumps(latest_data))
            
            with open("temperature.png", "rb") as imageFile:
                imgStr = base64.b64encode(imageFile.read())
                self.write_message(imgStr)
            

           # self.write_message({
           #     "img": base64.b64encode(temperature.png.read()),
           #     "desc": img_description,
           # })
            
        elif message == "Get_Ten_Latest_Values":
            '''
            humArray = [0,0,0,0,0,0,0,0,0,0]        #Initialize humidity array
            tempArray = [0,0,0,0,0,0,0,0,0,0]       #Initialize temp array
            
            for i in range(10):
                humidity,temperature = Adafruit_DHT.read_retry(DHT_SENSOR,DHT_PIN)
                humArray[i] = humidity
                tempArray[i] = temperature
                print("Humidity " ,i, "=" ,humArray[i])
                print("Temperature " ,i, "=", tempArray[i])
            
            self.write_message(str(humArray))
            '''
            
            #Get last 10 values of humidity from database
            sqlHumTenArray = tordbu.getLastTenHumidityValues()
            humArray = [0,0,0,0,0,0,0,0,0,0]        #Initialize the array

            for i in range(10):
                humArray[i] = sqlHumTenArray[i][0]
                
            self.write_message(str(humArray))
        
       
 
    def on_close(self):
        print ('connection closed')
 
    def check_origin(self, origin):
        return True
        
application = tornado.web.Application([
    (r'/ws', WSHandler),
])


def get_paramaters(message):
    if message == 'Temperature':
        humidity,temperature = Adafruit_DHT.read_retry(DHT_SENSOR,DHT_PIN)
        return temperature
 
 
 
if __name__ == "__main__":
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(8888, '10.0.0.180')
    myIP = socket.gethostbyname(socket.gethostname())
    print ('*** Websocket Server Started at %s***' % myIP)
    tornado.ioloop.IOLoop.instance().start()


