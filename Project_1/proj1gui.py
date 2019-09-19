# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'trial_2.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import Adafruit_DHT

DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 4
count = 1
flag = 0    #Temperature in C


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800 , 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Get_Latest_Value = QtWidgets.QPushButton(self.centralwidget)
        self.Get_Latest_Value.setGeometry(QtCore.QRect(200, 20, 131, 30))
        self.Get_Latest_Value.setObjectName("pushButton")
        self.Get_Latest_Value.clicked.connect(self.get_latest_values)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(27, 10, 51, 22))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(27, 50, 51, 22))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 30, 68, 22))
        self.label_3.setObjectName("label_3")
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(10, 140, 581, 131))
        self.graphicsView.setObjectName("graphicsView")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 280, 99, 30))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(120, 280, 99, 30))
        self.pushButton_3.setObjectName("pushButton_3")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(10, 80, 575, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(80, 10, 113, 21))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_6.setGeometry(QtCore.QRect(80, 30, 113, 21))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_7.setGeometry(QtCore.QRect(80, 50, 190, 21))
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(190, 120, 211, 22))
        self.label_4.setObjectName("label_4")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(10, 350, 581, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(450, 390, 141, 30))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(self.temperature_unit_change)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(270, 330, 68, 22))
        self.label_5.setObjectName("label_5")
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBox.setGeometry(QtCore.QRect(350, 20, 111, 32))
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.doubleSpinBox_2 = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBox_2.setGeometry(QtCore.QRect(480, 20, 131, 32))
        self.doubleSpinBox_2.setObjectName("doubleSpinBox_2")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(350, 0, 121, 22))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(480, 0, 141, 22))
        self.label_7.setObjectName("label_7")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 825, 28))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        self.timer = QtCore.QTimer()
        self.time = QtCore.QTime(0,0,0)
        self.timer.timeout.connect(self.timerEvent)
        self.timer.start(15000)
        
        print("*******************TEMPERATURE/HUMIDITY MONITORING SYSTEM*******************")

        
        

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Get_Latest_Value.setText(_translate("MainWindow", "Get_Latest_Values"))
        self.label.setText(_translate("MainWindow", "Temp:"))
        self.label_2.setText(_translate("MainWindow", "Time:"))
        self.label_3.setText(_translate("MainWindow", "Humidity:"))
        self.pushButton_2.setText(_translate("MainWindow", "Temperature"))
        self.pushButton_3.setText(_translate("MainWindow", "Humidity"))
        self.label_4.setText(_translate("MainWindow", "Temperature/Humidity Graph"))
        self.pushButton_4.setText(_translate("MainWindow", "Celcius/Fahrenheit"))
        self.label_5.setText(_translate("MainWindow", "Status"))
        self.label_6.setText(_translate("MainWindow", "Temp Threshold"))
        self.label_7.setText(_translate("MainWindow", "Humidity Threshold"))
        
    def get_latest_values(self):
            global flag
            _translate = QtCore.QCoreApplication.translate
            humidity,temperature = Adafruit_DHT.read(DHT_SENSOR,DHT_PIN)
            
            if humidity is not None and temperature is not None:
                    formated_temperature = '{0:0.1f}'.format(temperature)       #Format Temperature up to 1 digit precision
                    formated_humidity = '{0:0.1f}%'.format(humidity)            #Format Humidity up to 1 digit precision
                    current_time = QtCore.QDateTime.currentDateTime().toString()
                    if flag == 0:
                        formated_temperature_C = formated_temperature
                        self.lineEdit_5.setText(_translate("MainWindow",formated_temperature_C))
                        self.lineEdit_6.setText(_translate("MainWindow",formated_humidity))
                        self.lineEdit_7.setText(_translate("MainWindow",current_time))
                        print("Temp={0:0.1f}*C  Humidity={1:0.1f}%".format(float(formated_temperature_C), humidity))
                        print("TimeStamp:",current_time)



                    elif flag == 1:
                        formated_temperature_F = ((float(formated_temperature)*1.8) + 32)
                        print('{0:0.1f}'.format(formated_temperature_F))
                        self.lineEdit_5.setText(_translate("MainWindow",str('{0:0.1f}'.format(formated_temperature_F))))
                        self.lineEdit_6.setText(_translate("MainWindow",formated_humidity))
                        self.lineEdit_7.setText(_translate("MainWindow",current_time))
                        print("Temp={0:0.1f}*C  Humidity={1:0.1f}%".format(float(formated_temperature_F), humidity))
                        print("TimeStamp:",current_time)

#                   print("Temp={0:0.1f}*C  Humidity={1:0.1f}%".format(temperature, humidity))
#                   print("TimeStamp:",current_time)
            else:
                    print("Failed to retrieve data from humidity sensor")
        
    def get_temp_humidity_value(self):
            _translate = QtCore.QCoreApplication.translate
            humidity,temperature = Adafruit_DHT.read(DHT_SENSOR,DHT_PIN)
            
            if humidity is not None and temperature is not None:
                    formated_temperature = '{0:0.1f}'.format(temperature)       #Format Temperature up to 1 digit precision
                    formated_humidity = '{0:0.1f}%'.format(humidity)            #Format Humidity up to 1 digit precision
                    current_time = QtCore.QDateTime.currentDateTime().toString()
                    if flag == 0:
                        formated_temperature_C = formated_temperature
                        status_line = 'Temp: ' + str(formated_temperature_C) + ' ' + 'Humidity: ' + formated_humidity + ' ' + 'Time: ' + current_time + ' Sensor: Connected'  
                        self.lineEdit.setText(_translate("MainWindow",status_line))
                        print("Temp={0:0.1f}*C  Humidity={1:0.1f}%".format(float(formated_temperature_C), humidity))
                        print("TimeStamp:",current_time)

                    elif flag == 1:
                        formated_temperature_F = ((float(formated_temperature)*1.8) + 32)
                        status_line = 'Temp: ' + str('{0:0.1f}'.format(formated_temperature_F)) + ' ' + 'Humidity: ' + formated_humidity + ' ' + 'Time: ' + current_time + ' Sensor: Connected'  
                        self.lineEdit.setText(_translate("MainWindow",status_line))
                        print("Temp={0:0.1f}*C  Humidity={1:0.1f}%".format(float(formated_temperature_F), humidity))
                        print("TimeStamp:",current_time)

                     
#                    print("Temp={0:0.1f}*C  Humidity={1:0.1f}%".format(temperature, humidity))
#                    print("TimeStamp:",current_time)

            else:
                    formated_temperature = '-'
                    formated_humidity = '-'
                    current_time = QtCore.QDateTime.currentDateTime().toString()
                    status_line = 'Temp: ' + formated_temperature + ' ' + 'Humidity: ' + formated_humidity + ' ' + 'Time: ' + current_time + ' Sensor: Disconnected'
                    self.lineEdit.setText(_translate("MainWindow",status_line))
                    print("Failed to retrieve data from humidity sensor")
                    
            
                
    def timerEvent(self):
            global time
            global count
            if count <= 30:
                    self.time = self.time.addSecs(15)
                    self.get_temp_humidity_value()
                    count = count + 1
            else:
                    sys.exit()
                    
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

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

