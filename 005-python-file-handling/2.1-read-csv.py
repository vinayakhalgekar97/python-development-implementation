import csv

with open("./upload/demo.csv", "r") as file:
        csvreader = csv.reader(file)
        for row in csvreader:
            print(row)