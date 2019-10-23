#Author_Name: Om Raheja
#Date: 22 September 2019
#Project Members: Om Raheja & Mohit Rane
#Embedded Interface Design Project 1
#Temperature and Humidity monitoring system
# Referred to the following link for reading DHT values
# https://www.youtube.com/watch?v=2TibG64zLeA
# http://zetcode.com/gui/pyqt5/datetime/
# ARN: arn:aws:sns:us-east-1:222513434401:project_3_sns_topic
# arn:aws:sns:us-east-1:222513434401:project_3_sns_topic
# arn:aws:lambda:us-east-1:222513434401:function:myLambdaFunction

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'prototype_1.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import dbManager, sys
import Adafruit_DHT             #For Adafruit DHT22 humidity sensor
import pyqtgraph as pg          #For plotting temperature & humidity graphs on GUI
from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient

# AWS IoT certificate based connection
myMQTTClient = AWSIoTMQTTClient("123afhlss456")
myMQTTClient.configureEndpoint("a3daou1o8cc7z7-ats.iot.us-east-1.amazonaws.com", 8883)
myMQTTClient.configureCredentials("/home/pi/Documents/ECEN-5783-Embedded-Interface-Design/Project_3/Amazon_Root_CA_1.pem", "/home/pi/Documents/ECEN-5783-Embedded-Interface-Design/Project_3/3d9d689c17-private.pem.key", "/home/pi/Documents/ECEN-5783-Embedded-Interface-Design/Project_3/3d9d689c17-certificate.pem.crt")


#connect and publish
myMQTTClient.connect()
myMQTTClient.publish("thing01/info", "connected", 0)


DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 4                     #DHT22 data pin connected to Pin 4 of Raspberry Pi 3+ B
count = 1
flag = 0                        #If flag = 0, temp is in Celsius else Fahrenheit
default_temp_value_C = 25       #Default value for temp (in C) threshold
default_temp_value_F = 77       #Default value for temp (in F) threshold
default_hum_value = 50          #Default value for humidity threshold


class Ui_TemperatureAndHumidity(QtWidgets.QWidget):
    def __init__(self, database, tableName):
        self.dbu = dbManager.DatabaseUtility(database, tableName)
        QtWidgets.QWidget.__init__(self)
        #self.setupUi(self)

    def setupUi(self, TemperatureAndHumidity):
        TemperatureAndHumidity.setObjectName("TemperatureAndHumidity")
        TemperatureAndHumidity.resize(559, 500)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(TemperatureAndHumidity)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tempLabel = QtWidgets.QLabel(TemperatureAndHumidity)
        self.tempLabel.setObjectName("tempLabel")
        self.horizontalLayout.addWidget(self.tempLabel)

        #Display Latest Values of Temperature
        self.tempLatestValue = QtWidgets.QLineEdit(TemperatureAndHumidity)
        self.tempLatestValue.setObjectName("tempLatestValue")
        self.horizontalLayout.addWidget(self.tempLatestValue)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)        
        self.tempThreshLabel = QtWidgets.QLabel(TemperatureAndHumidity)
        self.tempThreshLabel.setObjectName("tempThreshLabel")
        self.horizontalLayout.addWidget(self.tempThreshLabel)
        
        #Set Threshold Values for Temperature
        self.setTempThresh = QtWidgets.QDoubleSpinBox(TemperatureAndHumidity)
        self.setTempThresh.setObjectName("setTempThresh")
        self.setTempThresh.setValue(default_temp_value_C)
        self.horizontalLayout.addWidget(self.setTempThresh)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.humLabel = QtWidgets.QLabel(TemperatureAndHumidity)
        self.humLabel.setObjectName("humLabel")
        self.horizontalLayout_2.addWidget(self.humLabel)
        
        #Display Latest Values for Humidity
        self.humLatestValue = QtWidgets.QLineEdit(TemperatureAndHumidity)
        self.humLatestValue.setObjectName("humLatestValue")
        self.horizontalLayout_2.addWidget(self.humLatestValue)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.humThreshLabel = QtWidgets.QLabel(TemperatureAndHumidity)
        self.humThreshLabel.setObjectName("humThreshLabel")
        self.horizontalLayout_2.addWidget(self.humThreshLabel)
        
        #Set Threshold for Humidity
        self.setHumThresh = QtWidgets.QDoubleSpinBox(TemperatureAndHumidity)
        self.setHumThresh.setObjectName("setHumThresh")
        self.setHumThresh.setValue(default_hum_value)
        self.horizontalLayout_2.addWidget(self.setHumThresh)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.timeLabel = QtWidgets.QLabel(TemperatureAndHumidity)
        self.timeLabel.setObjectName("timeLabel")
        self.horizontalLayout_3.addWidget(self.timeLabel)
        
        #Display Latest Value of Timestamp
        self.timeLatestValue = QtWidgets.QLineEdit(TemperatureAndHumidity)
        self.timeLatestValue.setObjectName("timeLatestValue")
        self.horizontalLayout_3.addWidget(self.timeLatestValue)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        
        #Get Latest Values fo Temperature, Humidity and Timestamp
        self.getLatestValuesButton = QtWidgets.QPushButton(TemperatureAndHumidity)
        self.getLatestValuesButton.setObjectName("getLatestValuesButton")
        self.getLatestValuesButton.clicked.connect(self.get_latest_values)
        self.horizontalLayout_3.addWidget(self.getLatestValuesButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem3)
        self.statusLabel = QtWidgets.QLabel(TemperatureAndHumidity)
        self.statusLabel.setObjectName("statusLabel")
        self.horizontalLayout_10.addWidget(self.statusLabel)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem4)
        self.verticalLayout_2.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        
        #Display Temperature, Humidity, Timestamp and Sensor status every 15 secs
        self.statusLineEdit = QtWidgets.QLineEdit(TemperatureAndHumidity)
        self.statusLineEdit.setObjectName("statusLineEdit")
        self.horizontalLayout_4.addWidget(self.statusLineEdit)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem5)
        self.graphLabel = QtWidgets.QLabel(TemperatureAndHumidity)
        self.graphLabel.setObjectName("graphLabel")
        self.horizontalLayout_13.addWidget(self.graphLabel)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem6)
        self.verticalLayout_2.addLayout(self.horizontalLayout_13)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        
        #Plot Graph of last 10 values of humidity or temperature
        #self.graphicsView = QtWidgets.QGraphicsView(TemperatureAndHumidity)
        self.graphicsView = pg.PlotWidget(TemperatureAndHumidity)
        self.graphicsView.setObjectName("graphicsView")
        self.horizontalLayout_5.addWidget(self.graphicsView)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        
        #Push Button to get Graph of temperature
        self.getTempGraphButton = QtWidgets.QPushButton(TemperatureAndHumidity)
        self.getTempGraphButton.setObjectName("getTempGraphButton")
        self.getTempGraphButton.clicked.connect(self.get_temp_graph)
        self.horizontalLayout_6.addWidget(self.getTempGraphButton)
        
        #Push Button to get Graph of humidity
        self.getHumGraphButton = QtWidgets.QPushButton(TemperatureAndHumidity)
        self.getHumGraphButton.setObjectName("getHumGraphButton")
        self.getHumGraphButton.clicked.connect(self.get_humidity_graph)
        self.horizontalLayout_6.addWidget(self.getHumGraphButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem7)
        self.alarmLabel = QtWidgets.QLabel(TemperatureAndHumidity)
        self.alarmLabel.setObjectName("alarmLabel")
        self.horizontalLayout_11.addWidget(self.alarmLabel)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem8)
        self.verticalLayout_2.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        
        #Displays Appropriate message based on the threshold temp and humidity
        self.alarmMessageLineEdit = QtWidgets.QLineEdit(TemperatureAndHumidity)
        self.alarmMessageLineEdit.setObjectName("alarmMessageLineEdit")
        self.horizontalLayout_7.addWidget(self.alarmMessageLineEdit)
        self.verticalLayout_2.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")

        #Push Button to change Temperature units from C to F and vice-versa
        self.CFButton = QtWidgets.QPushButton(TemperatureAndHumidity)
        self.CFButton.setObjectName("CFButton")
        self.CFButton.clicked.connect(self.temperature_unit_change)
        self.horizontalLayout_8.addWidget(self.CFButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout_8)

        self.retranslateUi(TemperatureAndHumidity)
        QtCore.QMetaObject.connectSlotsByName(TemperatureAndHumidity)

        #Setup and start timer
        self.timer = QtCore.QTimer()
        self.time = QtCore.QTime(0,0,0)
        self.timer.timeout.connect(self.timerEvent)
        self.timer.start(15000)
        
        print("*******************TEMPERATURE/HUMIDITY MONITORING SYSTEM*******************")

    def retranslateUi(self, TemperatureAndHumidity):
        _translate = QtCore.QCoreApplication.translate
        TemperatureAndHumidity.setWindowTitle(_translate("TemperatureAndHumidity", "Temperature & Humidity Monitoring System"))
        self.tempLabel.setText(_translate("TemperatureAndHumidity", "Temp:"))
        self.tempThreshLabel.setText(_translate("TemperatureAndHumidity", "Temp. Threshold"))
        self.humLabel.setText(_translate("TemperatureAndHumidity", "Hum :"))
        self.humThreshLabel.setText(_translate("TemperatureAndHumidity", "Hum. Threshold"))
        self.timeLabel.setText(_translate("TemperatureAndHumidity", "Time:"))
        self.getLatestValuesButton.setText(_translate("TemperatureAndHumidity", "Get Latest Values"))
        self.statusLabel.setText(_translate("TemperatureAndHumidity", "Status"))
        self.graphLabel.setText(_translate("TemperatureAndHumidity", "Temperature / Humidity Graph"))
        self.getTempGraphButton.setText(_translate("TemperatureAndHumidity", "Temperture Graph"))
        self.getHumGraphButton.setText(_translate("TemperatureAndHumidity", "Humidity Graph"))
        self.alarmLabel.setText(_translate("TemperatureAndHumidity", "Alarm Message"))
        self.CFButton.setText(_translate("TemperatureAndHumidity", "Celsius/Fahrenheit"))
        

    #Gets the latest value of temperature in C or F and Humidity along with timestamp
    def get_latest_values(self):
        global flag
        _translate = QtCore.QCoreApplication.translate
        humidity,temperature = Adafruit_DHT.read(DHT_SENSOR,DHT_PIN)    #Read value from sensor

        #If value not obtained, try for a max of 10 times until value is obtained        
        if humidity is None and temperature is None:
                for i in range(0,10):
                        humidity,temperature = Adafruit_DHT.read(DHT_SENSOR,DHT_PIN)
                        if humidity is not None and temperature is not None:
                                print("Got Temperature, Breaking Loop")
                                break
        
        if humidity is not None and temperature is not None:
            formated_temperature = '{0:0.1f}'.format(temperature)       #Format Temperature up to 1 digit precision
            formated_humidity = '{0:0.1f}'.format(humidity)            #Format Humidity up to 1 digit precision
            current_time = QtCore.QDateTime.currentDateTime().toString()
            payload = '{ "Msg_type": "data" , "timestamp": "' + current_time + '","temperature": ' + str(formated_temperature) + ',"humidity": '+ str(formated_humidity) + ' }'
            print (payload)
            myMQTTClient.publish("my/lambda/topic", payload, 0)

            if flag == 0:
                formated_temperature_C = formated_temperature
                self.tempLatestValue.setText(_translate("MainWindow",formated_temperature_C))
                self.humLatestValue.setText(_translate("MainWindow",formated_humidity))
                self.timeLatestValue.setText(_translate("MainWindow",current_time))
                print("Temp={0:0.1f}*C  Humidity={1:0.1f}%".format(float(formated_temperature_C), humidity))
                print("TimeStamp:",current_time)

            elif flag == 1:
                formated_temperature_F = ((float(formated_temperature)*1.8) + 32)
                print('{0:0.1f}'.format(formated_temperature_F))
                self.tempLatestValue.setText(_translate("MainWindow",str('{0:0.1f}'.format(formated_temperature_F))))
                self.humLatestValue.setText(_translate("MainWindow",formated_humidity))
                self.timeLatestValue.setText(_translate("MainWindow",current_time))
                print("Temp={0:0.1f}*C  Humidity={1:0.1f}%".format(float(formated_temperature_F), humidity))
                print("TimeStamp:",current_time)

        else:
                payload = '{ "Msg_type": "alert" , "Sensor Status": "Sensor Disconnected" }'
                myMQTTClient.publish("my/lambda/topic", payload, 0)
                print("Failed to retrieve data from humidity sensor")


    #Get temperature and humidity values every time the 15 sec timer fires
    def get_temp_humidity_value(self):
        _translate = QtCore.QCoreApplication.translate
        humidity,temperature = Adafruit_DHT.read(DHT_SENSOR,DHT_PIN)

        #Set threshold values for temperature and humitidy
        temp_thresh = self.setTempThresh.value()
        hum_thresh  = self.setHumThresh.value()

        if humidity is None and temperature is None:
            for i in range(0,10):
                humidity,temperature = Adafruit_DHT.read(DHT_SENSOR,DHT_PIN)
                if humidity is not None and temperature is not None:
                    print("Got Temperature, Breaking Loop")
                    break

        if humidity is not None and temperature is not None:
            #store temperature and humidity values in database
            self.dbu.AddEntryToTable(temperature, humidity)
            
            formated_temperature = '{0:0.1f}'.format(temperature)       #Format Temperature up to 1 digit precision
            formated_humidity = '{0:0.1f}'.format(humidity)             #Format Humidity up to 1 digit precision
            current_time = QtCore.QDateTime.currentDateTime().toString()
            
            payload = '{ "Msg_type": "data" , "timestamp": "' + current_time + '","temperature": ' + str(formated_temperature) + ',"humidity": '+ str(formated_humidity) + ' }'
		    print (payload)
		    myMQTTClient.publish("my/lambda/topic", payload, 0)
            
            if flag == 0:
                formated_temperature_C = formated_temperature
                if (float(formated_temperature_C) <= temp_thresh) and (float(formated_humidity) <= hum_thresh):
                    self.alarmMessageLineEdit.setText(_translate("MainWindow","Temperature: Below Threshold             Humidity: Below Threshold"))
                    payload = '{ "Msg_type": "alert" , "timestamp": "' + current_time + '","temperature alert level": ' + str(temp_thresh) + ',"temperature trigger level": '+ str(formated_temperature) + ',"Humidity alert level":  '+ str(hum_thresh) + ',"Humidity trigger level": '+ str(formated_humidity) + ' }'
                    print (payload)
                    myMQTTClient.publish("my/lambda/topic", payload, 0)
                elif (float(formated_temperature_C) >= temp_thresh) and (float(formated_humidity) <= hum_thresh):
                    self.alarmMessageLineEdit.setText(_translate("MainWindow","Temperature: Above Threshold             Humidity: Below Threshold"))
                    payload = '{ "Msg_type": "alert" , "timestamp": "' + current_time + '","temperature alert level": ' + str(temp_thresh) + ',"temperature trigger level": '+ str(formated_temperature) + ',"Humidity alert level":  '+ str(hum_thresh) + ',"Humidity trigger level": '+ str(formated_humidity) + ' }'
                    print (payload)
                    myMQTTClient.publish("my/lambda/topic", payload, 0)
                elif (float(formated_temperature_C) <= temp_thresh) and (float(formated_humidity) >= hum_thresh):
                    self.alarmMessageLineEdit.setText(_translate("MainWindow","Temperature: Below Threshold             Humidity: Above Threshold"))
                    payload = '{ "Msg_type": "alert" , "timestamp": "' + current_time + '","temperature alert level": ' + str(temp_thresh) + ',"temperature trigger level": '+ str(formated_temperature) + ',"Humidity alert level":  '+ str(hum_thresh) + ',"Humidity trigger level": '+ str(formated_humidity) + ' }'
                    print (payload)
                    myMQTTClient.publish("my/lambda/topic", payload, 0)
                elif (float(formated_temperature_C) >= temp_thresh) and (float(formated_humidity) >= hum_thresh):
                    self.alarmMessageLineEdit.setText(_translate("MainWindow","Temperature: Above Threshold             Humidity: Above Threshold"))
                    payload = '{ "Msg_type": "alert" , "timestamp": "' + current_time + '","temperature alert level": ' + str(temp_thresh) + ',"temperature trigger level": '+ str(formated_temperature) + ',"Humidity alert level":  '+ str(hum_thresh) + ',"Humidity trigger level": '+ str(formated_humidity) + ' }'
                    print (payload)
                    myMQTTClient.publish("my/lambda/topic", payload, 0)

                status_line = 'Temp: ' + str(formated_temperature_C) + ' ' + 'Humidity: ' + formated_humidity + ' ' + 'Time: ' + current_time + ' Sensor: Connected'  
                self.statusLineEdit.setText(_translate("MainWindow",status_line))
                print(count)
                print("Temp={0:0.1f}*C  Humidity={1:0.1f}%".format(float(formated_temperature_C), humidity))
                print("TimeStamp:",current_time)

            elif flag == 1:
                formated_temperature_F = ((float(formated_temperature)*1.8) + 32)
                status_line = 'Temp: ' + str('{0:0.1f}'.format(formated_temperature_F)) + ' ' + 'Humidity: ' + formated_humidity + ' ' + 'Time: ' + current_time + ' Sensor: Connected'  
                self.statusLineEdit.setText(_translate("MainWindow",status_line))
                print(count)
                print("Temp={0:0.1f}*C  Humidity={1:0.1f}%".format(float(formated_temperature_F), humidity))
                print("TimeStamp:",current_time)
                
        else:
            formated_temperature = '-'
            formated_humidity = '-'
            current_time = QtCore.QDateTime.currentDateTime().toString()
            status_line = 'Temp: ' + formated_temperature + ' ' + 'Humidity: ' + formated_humidity + ' ' + 'Time: ' + current_time + ' Sensor: Disconnected'
            self.statusLineEdit.setText(_translate("MainWindow",status_line))
            payload = '{ "Msg_type": "alert" , "Sensor Status": "Sensor Disconnected" }'
            myMQTTClient.publish("my/lambda/topic", payload, 0)
            print("Failed to retrieve data from humidity sensor")

    # Flag = 0 (Temperature is in C)
    # Flag = 1 (Temperature is in F)
    def temperature_unit_change(self):
        global flag
        if flag == 0:   #If temperature is in Celsius
            flag = 1    #Set flag to 1
            print("Flag =",flag) 
            print("Temperature will now be displayed in F")
            
        elif flag == 1: #If temperature is in F
            flag = 0    #Set flag to 0
            print("Flag =",flag)
            print("Temperature will now be displayed in C")


    def timerEvent(self):  
        global time
        global count
        if count <= 30:
            self.time = self.time.addSecs(15)
            self.get_temp_humidity_value()
            count = count + 1
        else:
            self.sysExit()

    def get_temp_graph(self):
        self.graphicsView.clear()
        #Get last ten entries from database for plotting graphs
        sqlTempTenArray = self.dbu.getLastTenTemperatureValues()
        
        #Initialize the array
        tempArray_C = [0,0,0,0,0,0,0,0,0,0]
        tempArray_F = [0,0,0,0,0,0,0,0,0,0]

        for i in range(10):
            tempArray_C[9-i] = sqlTempTenArray[i][0]

        if flag == 0:
            self.graphicsView.plot(tempArray_C)       
        else:
            for i in range(10):
                tempArray_F[i] = tempArray_C[i] * (1.8) + 32

            self.graphicsView.plot(tempArray_F)

    #Plot humidity graph on appropriate button press
    def get_humidity_graph(self):
        self.graphicsView.clear()       #Clear graphic window before plotting a new graph

        #Get last 10 values of humidity from database
        sqlHumTenArray = self.dbu.getLastTenHumidityValues()
        humArray = [0,0,0,0,0,0,0,0,0,0]        #Initialize the array

        for i in range(10):
            humArray[9-i] = sqlHumTenArray[i][0]

        self.graphicsView.plot(humArray)        #Plot humidity graph

    #Exit
    def sysExit(self):
        self.dbu.DropTable()
        sys.exit()


if __name__ == "__main__":
    db = 'eid_proj_1'
    tableName = 'prototype_table'

    app = QtWidgets.QApplication(sys.argv)
    TemperatureAndHumidity = QtWidgets.QWidget()
    ui = Ui_TemperatureAndHumidity(db, tableName)
    ui.setupUi(TemperatureAndHumidity)
    TemperatureAndHumidity.show()
    sys.exit(app.exec_())
    ui.sysExit()
