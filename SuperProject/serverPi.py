#!/usr/bin/python3

#Author_Name: Om Raheja and Mohit Rane
#Date: 19 November 2019
#Project Members: Om Raheja & Mohit Rane
#Embedded Interface Design Super Project
#Based on Project 2
#Sample Code

import tornado.httpserver
import tornado.websocket
import tornado.ioloop
import tornado.web
import socket
import json
import os
from serial import *
# import Adafruit_DHT             #For Adafruit DHT22 humidity sensor
# import prototype_1 as project_1 
from dbManager import DatabaseUtility
import base64                   #For transfering images from server to client

tordbu = DatabaseUtility("eid_proj_1", "prototype_table")

class WSHandler(tornado.websocket.WebSocketHandler):
    def open(self):
        print ("new connection")
      
    def on_message(self, message):
        print ('message received:  %s' % message)            
        if message == "Get_Ten_Latest_Values":
            #Get last 10 values of humidity from database
            sqlHumTenArray = tordbu.getLastTenHumidityValues()
            humArray = [0,0,0,0,0,0,0,0,0,0]        #Initialize the array

            for i in range(10):
                humArray[9-i] = sqlHumTenArray[i][0]
                
            self.write_message(str(humArray))
        
        # elif message == "Temperature Graph":
        #     with open("temperature.png", "rb") as imageFile:
        #         imgStr = base64.b64encode(imageFile.read())
        #         self.write_message(imgStr)
            
        # elif message == "Humidity Graph":
        #     with open("humidity.png", "rb") as imageFile:
        #         imgStr = base64.b64encode(imageFile.read())
        #         self.write_message(imgStr)
 
    def on_close(self):
        print ('connection closed')
 
    def check_origin(self, origin):
        return True
        
application = tornado.web.Application([
    (r'/ws', WSHandler),
])
 
 
if __name__ == "__main__":
    http_server = tornado.httpserver.HTTPServer(application)
    # http_server.listen(8888, '128.138.189.73')
    http_server.listen(8888)
    myIP = socket.gethostbyname(socket.gethostname())
    print ('*** Websocket Server Started at %s***' % myIP)
    tornado.ioloop.IOLoop.instance().start()
