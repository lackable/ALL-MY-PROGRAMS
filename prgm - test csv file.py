import csv
a = open('mycsv.csv','w')
l1 = [['oof','hi'],['zemb','d'],['my','csv'],['why','dsv']]
swriter = csv.writer(a)
swriter.writerows(l1)
