import sqlite3 as lite
import sys
con = lite.connect('sensorsData.db')
with con:
    cur = con.cursor() 
    cur.execute("INSERT INTO DHT_data VALUES(datetime('now'), 21.5, 35)")
    cur.execute("INSERT INTO DHT_data VALUES(datetime('now'), 26.8, 45)")
    cur.execute("INSERT INTO DHT_data VALUES(datetime('now'), 31.3, 55)")
