#!/usr/bin/env python3

import sqlite3

conn = sqlite3.connect('switch.db')
print("Opened database successfully")

conn.execute("INSERT INTO CONFIG (HOSTNAME,IP) VALUES ('sw-1','10.10.17.31' )")

conn.execute("INSERT INTO CONFIG (HOSTNAME,IP) VALUES ('sw-2','10.14.102.32' )")

conn.commit()
print("Records created successfully")
conn.close()
