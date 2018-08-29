#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  insertDataTableDHT.py
#  
#  Developed by Marcelo Rovai, MJRoBot.org @ 9Jan18
#  
#  Query dada on table "DHT_data" 

import sqlite3
from threading import Timer
from random import randint
temp = randint(20, 30)
humidity = randint(50, 60)
conn=sqlite3.connect('sensorsData.db')
curs=conn.cursor()
counter = 0

def add_data ():
 temp = randint(20, 30)
 humidity = randint(50, 60)
 curs.execute("INSERT INTO DHT_data values(datetime('now'), (?), (?))", (temp, humidity))
 conn.commit()
 for row in curs.execute("SELECT * FROM DHT_data"):
  print(row)

# Execute the function above
add_data ()
add_data ()
add_data ()
add_data ()
add_data ()