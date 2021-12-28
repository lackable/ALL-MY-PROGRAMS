import csv
a = open('mycsv.csv','r')
reader = csv.reader(a)
for i in reader:
    print(next(reader))
