#!/usr/bin/python3

import mysql.connector
from mysql.connector import errorcode
from datetime import datetime

##===============================================

class DatabaseUtility: 
	def __init__(self, database, tableName):
		self.db = database
		self.tableName = tableName

		# f = open('C:\\Users\\The_Captain\\Desktop\\TPayne Experience\\_Episodes\\_LetsLearn\\026_LLP__SQL_Databases\\password.txt', 'r')
		# p = f.read(); f.close();
		self.cnx = mysql.connector.connect(user = 'eiduser',
									password = 'beboulder',
									host = '127.0.0.1')
		self.cursor = self.cnx.cursor()

		self.ConnectToDatabase()
		self.CreateTable()
		
	def ConnectToDatabase(self):
		try:
			self.cnx.database = self.db
		except mysql.connector.Error as err:
			if err.errno == errorcode.ER_BAD_DB_ERROR:
				self.CreateDatabase()
				self.cnx.database = self.db
			else:
				print(err.msg)

	def CreateDatabase(self):
		try:
			self.RunCommand("CREATE DATABASE %s DEFAULT CHARACTER SET 'utf8';" %self.db)
		except mysql.connector.Error as err:
			print("Failed creating database: {}".format(err))

	def CreateTable(self):
		cmd = (" CREATE TABLE IF NOT EXISTS " + self.tableName + " ("
			" `ID` int(5) NOT NULL AUTO_INCREMENT,"
			" `date` date NOT NULL,"
			" `time` time NOT NULL,"
			" `temperature` float NOT NULL,"
			" `humidity` float NOT NULL,"
			" PRIMARY KEY (`ID`)"
			") ENGINE=InnoDB;")
		self.RunCommand(cmd)

	# def GetTable(self):
	# 	self.CreateTable()
	# 	return self.RunCommand("SELECT * FROM %s;" % self.tableName)

	# def GetColumns(self):
	# 	return self.RunCommand("SHOW COLUMNS FROM %s;" % self.tableName)

	# get latest temperature value
	def getLatestTemperatureValue(self):
		# SELECT temperature FROM testable2 ORDER BY ID DESC LIMIT 1;
		return self.RunCommand("SELECT temperature FROM %s ORDER BY ID DESC LIMIT 1;" % self.tableName)

	# get latest humidity value
	def getLatestHumidityValue(self):
		# SELECT humidity FROM testable2 ORDER BY ID DESC LIMIT 1;
		return self.RunCommand("SELECT humidity FROM %s ORDER BY ID DESC LIMIT 1;" % self.tableName)

	# get last 10 temperature values
	def getLastTenTemperatureValues(self):
		# SELECT temperature FROM testable2 ORDER BY ID DESC LIMIT 1;
		return self.RunCommand("SELECT temperature FROM %s ORDER BY ID DESC LIMIT 10;" % self.tableName)

	# get last 10 humidity values
	def getLastTenHumidityValues(self):
		# SELECT humidity FROM testable2 ORDER BY ID DESC LIMIT 1;
		return self.RunCommand("SELECT humidity FROM %s ORDER BY ID DESC LIMIT 10;" % self.tableName)


	def RunCommand(self, cmd):
		print ("RUNNING COMMAND: " + cmd)
		try:
			self.cursor.execute(cmd)
		except mysql.connector.Error as err:
			print ('ERROR MESSAGE: ' + str(err.msg))
			print ('WITH ' + cmd)
		try:
			msg = self.cursor.fetchall()
		except:
			msg = self.cursor.fetchone()
		return msg

	def AddEntryToTable(self, temperature, humidity):
		date1 = datetime.now().strftime("%y-%m-%d")
		time = datetime.now().strftime("%H:%M")
		
		cmd = " INSERT INTO " + self.tableName + " (date, time, temperature, humidity)"
		cmd += " VALUES ('%s', '%s', '%f', '%f');" % (date1, time, temperature, humidity)
		self.RunCommand(cmd)

	def __del__(self):
		self.cnx.commit()
		self.cursor.close()
		self.cnx.close()

##===============================================
##===============================================


# if __name__ == '__main__':
# 	db = 'eid_proj_1'
# 	tableName = 'testable2'

# 	dbu = DatabaseUtility(db, tableName)

# 	dbu.AddEntryToTable (34.41, 40.99)
# 	print (dbu.getTemperature())
# 	print (dbu.getHumidity())