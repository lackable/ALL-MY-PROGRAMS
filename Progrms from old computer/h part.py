
'''# first part
mystr = input('enter string : ')
anumber = mystr.count('a')
enumber = mystr.count('e')
inumber = mystr.count('i')
onumber = mystr.count('o')
unumber = mystr.count('u')

print("no. of times a is there =",anumber)
print("no. of times e is there =",enumber)
print("no. of times i is there =",inumber)
print("no. of times o is there =",onumber)
print("no. of times u is there =",unumber)
'''
#or part
list1 = eval(input('copy paste list here:'))
print(type(list1))
n = input('pls enter the value you search for:')
if n in list1:
    print('FOUND!')
else:
    list1.append(n)
    print('it wasnt in there, added it for you ;)')
