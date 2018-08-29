#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  appDhtWebHist_v2.py
#  
#  Created by MJRoBot.org 
#  10Jan18

'''
	RPi WEb Server for DHT captured data with Gage and Graph plot  
'''
import time
from datetime import datetime
import io
import sqlite3
dbname='sensorsData.db'
from threading import Timer
from random import randint
sampleFreq = 1*10 # time in seconds ==> Sample each 10 sec

conn=sqlite3.connect('sensorsData.db')
curs=conn.cursor()

# Retrieve LAST data from database
def getLastData():
	for row in curs.execute("SELECT * FROM DHT_data ORDER BY timestamp DESC LIMIT 1"):
		time = str(row[0])
		temp = row[1]
		hum = row[2]
	#conn.close()
	return time, temp, hum

# Get 'x' samples of historical data
def getHistData (numSamples):
	curs.execute("SELECT * FROM DHT_data ORDER BY timestamp DESC LIMIT "+str(numSamples))
	data = curs.fetchall()
	dates = []
	temps = []
	hums = []
	for row in reversed(data):
		dates.append(row[0])
		temps.append(row[1])
		hums.append(row[2])
		temps, hums = testeData(temps, hums)
	return dates, temps, hums

# Test data for cleanning possible "out of range" values
def testeData(temps, hums):
	n = len(temps)
	for i in range(0, n-1):
		if (temps[i] < -10 or temps[i] >50):
			temps[i] = temps[i-2]
		if (hums[i] < 0 or hums[i] >100):
			hums[i] = temps[i-2]
	return temps, hums


# Get Max number of rows (table size)
def maxRowsTable():
	for row in curs.execute("select COUNT(temp) from  DHT_data"):
		maxNumberRows=row[0]
	return maxNumberRows

# Get sample frequency in minutes
def freqSample():
	times, temps, hums = getHistData (2)
	fmt = '%Y-%m-%d %H:%M:%S'
	tstamp0 = datetime.strptime(times[0], fmt)
	tstamp1 = datetime.strptime(times[1], fmt)
	print("tstamp0",tstamp0)
	print("tstamp1",tstamp1)
	freq = tstamp1-tstamp0
	print("freq=",freq)
	freq = int(round(freq.total_seconds()/5))
	return (freq)

# define and initialize global variables
global numSamples
numSamples = maxRowsTable()
if (numSamples > 101):
        numSamples = 100

global freqSamples
freqSamples = freqSample()

global rangeTime
rangeTime = 100
				

# main function
def main():
    print("""********Program Start*******""")
    while True:
        getFrequency = freqSample()
        print("Data Frequency",getFrequency)
        getLastData1 = getLastData()
        print("Last Data",getLastData1)
        getHistData1 = getHistData(2)
        print(getHistData1)
        break
        #time.sleep(sampleFreq)
		
# ------------ Execute program 
main()



	
	




