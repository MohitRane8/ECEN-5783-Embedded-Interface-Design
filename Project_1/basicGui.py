# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'basic.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import dbManager, sys
import Adafruit_DHT

DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 4

class Ui_Form(QtWidgets.QWidget):
    def __init__(self, database, tableName):
        self.dbu = dbManager.DatabaseUtility(database, tableName)
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(313, 245)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.temperatureLabel = QtWidgets.QLabel(Form)
        self.temperatureLabel.setObjectName("temperatureLabel")
        self.horizontalLayout.addWidget(self.temperatureLabel)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.temperatureDisplay = QtWidgets.QLineEdit(Form)
        self.temperatureDisplay.setObjectName("temperatureDisplay")
        self.horizontalLayout.addWidget(self.temperatureDisplay)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.humidityLabel = QtWidgets.QLabel(Form)
        self.humidityLabel.setObjectName("humidityLabel")
        self.horizontalLayout_2.addWidget(self.humidityLabel)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.humidityDisplay = QtWidgets.QLineEdit(Form)
        self.humidityDisplay.setObjectName("humidityDisplay")
        self.horizontalLayout_2.addWidget(self.humidityDisplay)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.updateButton = QtWidgets.QPushButton(Form)
        self.updateButton.setObjectName("updateButton")
        self.verticalLayout.addWidget(self.updateButton)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.temperatureLabel.setText(_translate("Form", "Temperature"))
        self.humidityLabel.setText(_translate("Form", "Humidity"))
        self.updateButton.setText(_translate("Form", "Update"))
        self.updateButton.clicked.connect(self.updateValue)

    def updateValue(self):
        humidity,temperature = Adafruit_DHT.read_retry(DHT_SENSOR,DHT_PIN)

        if humidity is not None and temperature is not None:
                # formated_temperature = '{0:0.1f}'.format(temperature)
                # formated_humidity = '{0:0.1f}'.format(humidity)

                # add formated values to db
                # self.dbu.AddEntryToTable (formated_temperature, formated_humidity)
                self.dbu.AddEntryToTable(temperature, humidity)

                # retrieve latest value from db
                temperatureFromDB = self.dbu.getTemperature()
                humidityFromDB = self.dbu.getHumidity()

                print(temperatureFromDB[0][0])
                print(humidityFromDB[0][0])

                self.temperatureDisplay.setText((str)(temperatureFromDB[0][0]))
                self.humidityDisplay.setText((str)(humidityFromDB[0][0]))
                print("Temp={0:0.1f}*C  Humidity={1:0.1f}%".format(temperature, humidity))
        else:
                print("Failed to retrieve data from humidity sensor")

if __name__ == '__main__':
    db = 'eid_proj_1'
    tableName = 'testable5'

    app = QtWidgets.QApplication(sys.argv)
    ex = Ui_Form(db, tableName)
    ex.show()
    sys.exit(app.exec_())