mystring = str(input('enter string'))
mystr = mystring.split()
n = len(mystr)
for i in range(0,n):
    mystr = mystr[0].upper()
print(str(mystr))

