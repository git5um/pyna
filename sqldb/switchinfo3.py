#!/usr/bin/env python3

from napalm import get_network_driver
import json
import sqlite3

conn = sqlite3.connect('switch.db')
print("Opened database successfully")

cursor = conn.execute("SELECT hostname from CONFIG")
for row in cursor:
    print(row)
    driver = get_network_driver('eos')
    device = driver(row, 'admin', 'alta3')
    device.open() # start the connection
    config = device.get_config()
    rc = config['running']
    sc = config['startup']
    conn.execute("UPDATE CONFIG set running_config = '(rc)'")
    conn.execute("UPDATE CONFIG set startup_config = '(sc)'")


conn.commit()
print("Records created successfully")
conn.close()
