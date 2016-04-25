# -*- coding: utf-8 -*-

import json
from dateutil.parser import parse

with open('smart.json') as data_file:
    data = json.load(data_file)

with open('smart.csv','w') as out:
	for d in data:
		date = parse(d["date"])
		c = ""
		c = "date," + date.strftime("%d-%m-%Y-%H:%M")
		for s in d["sensors"]:
			c += "," + s["name"] + "," + s["value"]
		print c
		out.write(c + "\n")






