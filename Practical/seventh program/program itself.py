import csv

fin = open(r"E:\STUDY 12 Saksham\CS school\Practical\mycsvfile.csv","w", newline = '')
a = int(input('how many users are there? '))
data = []
for i in range(a):
    u = input('please enter user-id :')
    p = input('please enter password for user :')
    list1 = [u,p]
    data.append(list1)


wr = csv.writer(fin)
for i in data:
    wr.writerow(i)
fin.close()
print('your file has been created succesfully')

f = open(r"E:\STUDY 12 Saksham\CS school\Practical\mycsvfile.csv","r")
f1 = csv.reader(f)
s = input('please enter user-id for login')
for i in f1:
    if s == i[0]:
        g = input('please enter password : ')
        if g == i[1]:
            print('The password is correct!')
        else:
            print('sorry, password is incorrect')

    else:
        pass
