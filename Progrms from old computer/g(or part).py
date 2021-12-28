# (i)
mylist = ['hello','morning','evening','great','fine','demo']

# (ii)
n = int(input('enter value n :'))

#(iii)
a=input('enter string a here')
b=input('enter string b here')
c=input('enter string c here')
d=input('enter string d here')
e=input('enter string e here')

l3 = []
list1 = [a,b,c,d,e]
for i in list1:
    if len(i) == n:
       l3.append(i) 
       print(i)

#(iv)
print(len(l3))
        
