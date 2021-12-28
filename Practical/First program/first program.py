file = open(r"E:\STUDY 12 Saksham\CS school\Practical\mytextfile1.txt","r")
words =[]
for i in file :
    words1=i.split()
    for j in words1:
        words.append(j)
        
print("#".join(words))
