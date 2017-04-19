#! python3

import csv
import json

try:
    input = raw_input
except NameError:
    pass

filename = input("filename:")
if not filename:
    filename = "tempvals.csv"

with open(filename) as f:
    csv_reader = csv.DictReader(f)
    data = {row["OBJECTID"]:row for row in csv_reader}

filename = filename[:filename.rfind(".")] + ".json"
with open(filename, "w") as f:
    f.write("index_data = " + json.dumps(data))

input("done")