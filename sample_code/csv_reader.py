import csv

rows = []
data_file = open("../data/orangehrm_py.csv", "r")
reader = csv.reader(data_file)
next(reader)
for row in reader:
    rows.append(row)
    print(row)

print(rows)
