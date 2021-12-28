'''#strings programs
#Q1
line = input('please enter line')
line1 =line.split()
line2 = []
for i in line1:
    if i[0] == 'A':
       line2.append(i)
print(line2)

#Q2
mystr = input('pls enter str')
mystrlen = len(mystr.split())
print('number of elements in this string is ',mystrlen)

#Q3
mystr = input('pls eneter string with the most vovels ;)')
mystrvowel = mystr.count('a')+mystr.count('A')+mystr.count('e')+mystr.count('E')+mystr.count('i')+mystr.count('I')+mystr.count('o')+mystr.count('O')+mystr.count('u')+mystr.count('U')
print('Number of vowels in your string are ',mystrvowel)

#Q4
mystr = input('enter your line')
sub = input('enter the sub string')
output = mystr.count(sub)
print('your sub string was reapeated',output,'times')

#Q5
cant do it

#Q6
mystr = input('enter your line')
print(mystr[::-1])

#Q7
mystr = input('enter your line')
if mystr == mystr[::-1]:
    print('THIS IS A PALINDROME')
else:
    print('sorry this isnt a palindrome :(')

#8 (turning into a list form but cant do it in a string)
mystr = input('enter your line')
l1 = []
for i in mystr:
    if mystr.index(i)%2 == 0:
       l1.append(i.upper())
    else:
        l1.append(i)
mystr1 = str(l1)
print(mystr1)

#Q9(sir cant do it)
l1 = input('enter your list')
l2 = l1.split()
for i in l2:
    if i%2 == 0:
        pass
    else:
        l2.remove([i])

#Q10(how to define alphabets,digits and special charecters)

#Q11
mystr = input('enter your line')
print(mystr[:-3]+mystr[:3])
'''
#Q12(sir list reverse karne ka toh koi command he nahi bataya)
mystr = eval(input('enter your line'))
