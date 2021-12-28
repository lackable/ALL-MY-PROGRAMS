import csv
f = open(r"E:\STUDY 12 Saksham\CS school\Practical\mycsvfile.csv","r")
f1 = csv.reader(f)
s = input('please enter student name ')
flag = False
for i in f1:
    if s == i[0]:
        print('Roll no. is ', i[1])
        flag = True

    else:
        pass

if flag == False:
    print('Sorry , No student with that name exists')

