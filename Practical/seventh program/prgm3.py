#Taking list input
list2= (input('Enter list here :'))
list1 = list2.split(',')

#To remove 
for i in list1:
    if i in [',','[',']']:
        list1.remove(i)
    else:
        pass

for i in range(len(list1)):
    list1[i] = int(list1[i])


print("Original list is: ",list1)
n = len(list1)
for i in range(n):
    for j in range(0,n-i-1):
        if list1[j]>list1[j+1]:
            list1[j],list1[j+1]=list1[j+1],list1[j]
print("List after sorting: ",list1)

