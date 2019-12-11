#!/usr/bin/python3

# Author_Name: Mohit Rane
#Date: 22 September 2019
#Project Members: Om Raheja & Mohit Rane
#Embedded Interface Design Project 1
#Temperature and Humidity monitoring system
# Referred to Trevor Payne youtube video as a reference for this code
# https://www.youtube.com/watch?v=2TibG64zLeA

import mysql.connector
from mysql.connector import errorcode
from datetime import datetime

##===============================================
class DatabaseUtility: 
	def __init__(self, database, tableName):
		self.db = database
		self.tableName = tableName

		# providing username and password for mysql
		self.cnx = mysql.connector.connect(user = 'eiduser',
									password = 'beboulder',
									host = '127.0.0.1')
		self.cursor = self.cnx.cursor()

		self.ConnectToDatabase()
		# self.CreateTable()
		
	# establish connection to database
	def ConnectToDatabase(self):
		try:
			self.cnx.database = self.db
		except mysql.connector.Error as err:
			if err.errno == errorcode.ER_BAD_DB_ERROR:
				self.CreateDatabase()
				self.cnx.database = self.db
			else:
				print(err.msg)

	# create a database
	def CreateDatabase(self):
		try:
			self.RunCommand("CREATE DATABASE %s DEFAULT CHARACTER SET 'utf8';" %self.db)
		except mysql.connector.Error as err:
			print("Failed creating database: {}".format(err))

	# create table in database if ti does not exist
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

	# get total number of entries in sql database
	def getNumOfEntries(self):
		return self.RunCommand("SELECT COUNT(*) FROM %s;" % self.tableName)
		
	# get all data from sql database
	def getData(self):
		return self.RunCommand("SELECT DATA FROM %s;" % self.tableName)

	# method to run command and return appropriate error message
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

	# method to add an entry to table
	def AddEntryToTable(self, temperature, humidity):
		date1 = datetime.now().strftime("%y-%m-%d")
		time = datetime.now().strftime("%H:%M")
		
		cmd = " INSERT INTO " + self.tableName + " (date, time, temperature, humidity)"
		cmd += " VALUES ('%s', '%s', '%f', '%f');" % (date1, time, temperature, humidity)
		self.RunCommand(cmd)

	# method to remove table from database
	def DropTable(self):
		self.RunCommand("DROP TABLE %s" % self.tableName)

	def __del__(self):
		self.cnx.commit()
		self.cursor.close()
		self.cnx.close()

##===============================================
#For Debugging purposes
##===============================================
# if __name__ == '__main__':
# 	db = 'eid_proj_1'
# 	tableName = 'testable2'

# 	dbu = DatabaseUtility(db, tableName)

# 	dbu.AddEntryToTable (34.41, 40.99)
# 	print (dbu.getLatestTemperatureValue())
# 	print (dbu.getLatestHumidityValue())

# 	print (dbu.getLastTenTemperatureValues())
# 	print (dbu.getLastTenHumidityValues())
