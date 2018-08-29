import time
import sqlite3
dbname='sensorsData.db'
from threading import Timer
from random import randint
sampleFreq = 1*10 # time in seconds ==> Sample each 10 sec

# get data from DHT sensor
def getDHTdata():	
    hum = randint(50, 60)
    temp = randint(25, 35)
    if hum is not None and temp is not None:
        hum = round(hum)
        temp = round(temp)
    return temp, hum

# log sensor data on database
def logData (temp, hum):
    conn=sqlite3.connect(dbname)
    curs=conn.cursor()
    print ("\n------------------------")
    print ("Connected to Sensor DB:")
    print ("------------------------\n")
    curs.execute("INSERT INTO DHT_data values(datetime('now'), (?), (?))", (temp, hum))
    print("Values inserted:: Temprature:=",temp,"& Humidity:=", hum)
    conn.commit()
    conn.close()

#get total count of entred data so far
def getCountOfDHTdata ():
    conn = sqlite3.connect('sensorsData.db')
    curs=conn.cursor()
    for row in curs.execute("SELECT count(1) FROM DHT_data"):
        print ("\nTotal Sensor values entered:= ", row[0], "& last data logged on database is:\n")
    for row in curs.execute("SELECT * FROM DHT_data ORDER BY timestamp DESC LIMIT 1"):
        print (row)
    
	
# main function
def main():
    print("""********Program Start*******""")
    while True:
        temp, hum = getDHTdata()
        logData (temp, hum)
        getCountOfDHTdata()
        time.sleep(sampleFreq)
		
# ------------ Execute program 
main()

