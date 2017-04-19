#! python3

import csv

try:
    input = raw_input
except NameError:
    pass

omitted = ("BOON LAY", "CHANGI BAY", "CENTRAL WATER CATCHMENT", "LIM CHU KANG", "MARINA EAST", "MARINA SOUTH", "NORTH-EASTERN ISLANDS", "PAYA LEBAR", "SIMPANG", "STRAITS VIEW", "WESTERN ISLANDS", "PIONEER", "TUAS", "DOWNTOWN CORE", "TENGAH")

filename_master = input("filename master:")
if not filename_master:
    filename_master = "tempvals.csv"

with open(filename_master) as f:
    csv_reader = csv.DictReader(f)
    master_data = [row for row in csv_reader]

while True:
    filename_data = input("filename data:")
    if filename_data == "":
        break
    
    join_col = input("Join Column:")
    if not join_col:
        join_col = "PLN_AREA_N"

    with open(filename_data) as f:
        csv_reader = csv.DictReader(f)
        join_data = {row[join_col].strip():row for row in csv_reader}

    master_headers = tuple( master_data[0].keys() )
    join_headers = next(iter(join_data.values())).keys()
    join_headers = tuple(col for col in join_headers if col not in master_headers)
    master_headers = master_headers + join_headers

    for row in master_data:
        join_val = row[join_col]
        join_row = join_data.get(join_val)
            
        if join_row:
            if join_val in omitted:
                print("NOTE: OMITTED planning area found: {}".format(join_val))
            for col in join_headers:
                row[col] = join_row[col]
        else:
            if join_val not in omitted:
                print("WARNING! NON OMITTED planning area not found: {}".format(join_val))
            for col in join_headers:
                row[col] = 0


import sys
if sys.version_info[0] == 2:
    f = open("new"+filename_master, "wb")
else:
    f= open("new"+filename_master, "w", newline="")
csv_writer = csv.DictWriter(f, master_headers)
csv_writer.writeheader()
for row in master_data:
    csv_writer.writerow(row)
f.close()