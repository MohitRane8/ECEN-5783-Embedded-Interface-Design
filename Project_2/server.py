import tornado.httpserver
import tornado.websocket
import tornado.ioloop
import tornado.web
import socket
import json
import os
from serial import *
import Adafruit_DHT             #For Adafruit DHT22 humidity sensor
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
        print ("new connection")
      
    def on_message(self, message):
        print ('message received:  %s' % message)
        if message == "Temperature":
            #make a dictionary
            humidity,temperature = Adafruit_DHT.read_retry(DHT_SENSOR,DHT_PIN)
            latest_data = {"temp": temperature, "hum": humidity}
            #turn it to JSON and send it to the browser
            self.write_message(json.dumps(latest_data))
        
        
        
        
        #if message == "Temperature":
            #humidity,temperature = Adafruit_DHT.read_retry(DHT_SENSOR,DHT_PIN)
            #self.write_message(str(temperature))
        #    self.write_message(str(get_paramaters(message)))
            
        #else:    
            # Reverse Message and send it back
        #    print ('sending back message: %s' % message[::-1])
        #    self.write_message(message[::-1])
 
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
    http_server.listen(8888)
    myIP = socket.gethostbyname(socket.gethostname())
    print ('*** Websocket Server Started at %s***' % myIP)
    tornado.ioloop.IOLoop.instance().start()

#<label for="Humidity" id="Label_Humidity">Humidity: </label>
#<output type="text" id="Output_Humidity"></output></br>
#<input type="submit" id="get_humidity" value="get_humidity" /> </input>

#<div id="message_details">
#</br></br>
#<label for="message">message:</label>
#<input type="text" id="message" value="Hello World!"/><br />
#<input type="submit" id="send" value="send" />
#</div>
