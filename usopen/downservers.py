#!/usr/bin/python3

# JSON is part of the Python Standard Library
import json

    ## open the file
with open("status.json", "r") as f:
    data = json.load(f)
    print(data)
    downed_servers = []
    for status in data:
        if status["state"] == "down":
            downed_servers.append(status["server"])

with open("downed_servers.json", "w") as f2:
    json.dump(downed_servers, f2, indent=4)
