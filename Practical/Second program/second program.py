file = open(r"E:\STUDY 12 Saksham\CS school\Practical\mytextfile2.txt","r")
cont1 = file.read()
cont = cont1.replace(" ", "")
v = 0
con = 0
lower = 0
upper = 0
for i in cont:
    if i.islower():
        lower+=1
    else:
        upper+=1
    if i in ["a","e","i","o","u","A","E","I","O","U"]:
        v+=1
    else:
        con+=1
file.close()
print("Number of Vowels are : ",v)
print("Number of Consonants are : ",con)
print("Number of Lower case charecters are : ",lower)
print("Number of Upper case charecters are : ",upper)






