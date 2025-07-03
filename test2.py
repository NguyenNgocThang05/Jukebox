import csv

with open('data.csv') as csvfile:
    csv_reader = csv.reader(csvfile)
    next(csv_reader)
    for row in csv_reader:
        print(row[0], row[2])