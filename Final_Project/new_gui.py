# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import dbManager, sys
import pyqtgraph as pg          #For plotting temperature & humidity graphs on GUI
import re

correct_cnt = 0
wrong_cnt = 0
invalid_cnt = 0
i_size = 0

class Ui_MainWindow(QtWidgets.QWidget):
    def __init__(self, database, tableName):
        self.dbu = dbManager.DatabaseUtility(database, tableName)
        QtWidgets.QWidget.__init__(self)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(20, 60, 141, 30))
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(180, 60, 113, 32))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(320, 60, 113, 32))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(20, 140, 141, 30))
        self.pushButton_2.setObjectName("pushButton_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(180, 140, 113, 32))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(320, 140, 113, 32))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(210, 30, 68, 22))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(350, 30, 68, 22))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(210, 110, 68, 22))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(350, 110, 68, 22))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(170, 460, 131, 22))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(30, 250, 401, 211))
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap("cat.jpeg"))
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName("label_6")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(170, 210, 141, 30))
        self.pushButton_3.setObjectName("pushButton_3")
        # MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 28))
        self.menubar.setObjectName("menubar")
        # MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        # MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        self.pushButton.clicked.connect(self.get_wand_stats)
        self.pushButton_2.clicked.connect(self.get_voice_stats)
        self.pushButton_3.clicked.connect(self.show_image)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Image Statistics"))
        self.pushButton_2.setText(_translate("MainWindow", "Voice Statistics"))
        self.label.setText(_translate("MainWindow", "Correct"))
        self.label_2.setText(_translate("MainWindow", "Wrong"))
        self.label_3.setText(_translate("MainWindow", "Correct"))
        self.label_4.setText(_translate("MainWindow", "Wrong"))
        self.label_5.setText(_translate("MainWindow", "Last Image Taken"))
        self.pushButton_3.setText(_translate("MainWindow", "Get Latest Image"))    

    def show_image(self):
            self.label_6.setPixmap(QtGui.QPixmap("image.jpg")) 

    def get_wand_stats(self):
            global correct_cnt
            global wrong_cnt
            global invalid_cnt
            global i_size

            data_str = self.dbu.getData()
            i_size = self.dbu.getNumOfEntries()
            data_list = []
            col2 = []
            col3 = []
            for i in range(0,(i_size[0][0] - 1)):
                    data_list.append(re.findall(r'\w+', str(data_str[i]))) 
                    #print(data_list)
                    #print(type(data_str))
                    
                    #split data
                    print(data_list[i][0])     # label
                    #print(data_list[i])       # correct/wrong
                    #col2.append(data_list[i][1])
                    
                    if data_list[i][0] != "invalid_input":
                            col3.append(data_list[i][2])
                            print("col3[] " + col3[i])
                    elif data_list[i][0] == "invalid_input":
                            col3.append("invalid_input")
                    
            for i in range(0,(i_size[0][0] - 1)):
                    if col3[i] != "invalid_input":
                            if col3[i] == "correct":
                                    correct_cnt = correct_cnt + 1
                            elif col3[i] == "wrong":
                                    wrong_cnt = wrong_cnt + 1
                            else:
                                    invalid_cnt = invalid_cnt + 1
        
            print("correct count = " + str(correct_cnt*100/i_size[0][0]))
            print("wrong count = " + str(wrong_cnt*100/i_size[0][0]))
            print("invalid count = " + str(100 - ((wrong_cnt + correct_cnt)*100/i_size[0][0])))
            self.lineEdit.setText(str(round(correct_cnt*100/i_size[0][0],2)))         
            self.lineEdit_2.setText(str(round(wrong_cnt*100/i_size[0][0],2)))
    
    def get_voice_stats(self):
            global correct_cnt
            global wrong_cnt
            global invalid_cnt
            global i_size
            
            self.lineEdit_3.setText(str(round(correct_cnt*100/i_size[0][0],2)))         
            self.lineEdit_4.setText(str(round(wrong_cnt*100/i_size[0][0],2)))
            
            i_size = 0
            correct_cnt = 0
            wrong_cnt = 0
            invalid_cnt = 0


if __name__ == "__main__":
    # setup sql database and table that will be used
    db = 'final_proj'
    tableName = 'final'

    app = QtWidgets.QApplication(sys.argv)
    # MainWindow = QtWidgets.QMainWindow()
    MainWindow = QtWidgets.QWidget()
    ui = Ui_MainWindow(db, tableName)
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
    ui.sysExit()
