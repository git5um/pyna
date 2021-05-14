#!/usr/bin/env python3

import sqlite3
conn = sqlite3.connect('switch.db')
print("Opened database successfully")
conn.execute('''CREATE TABLE IF NOT EXISTS CONFIG
 (HOSTNAME      CHAR,
 IP             CHAR,
 STARTUP_CONFIG CHAR,
 RUNNING_CONFIG CHAR,
 VALID_CONFIG   BOOL);''')
print("Table created successfully")
conn.close()

