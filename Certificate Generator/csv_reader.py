import csv

reader=csv.reader(open("wordpress.csv"))

for raw in reader:
    print(raw[0])
