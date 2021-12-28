import pickle
f=open(r"E:\STUDY 12 Saksham\CS school\Practical\records1.dat", "wb")

pickle.dump([1, "Saksham", 90], f)
pickle.dump([2, "Tanish", 80], f)
pickle.dump([3, "Priyashi", 90], f)
pickle.dump([4, "Harjot", 80], f)
pickle.dump([5, "Gautam", 85], f)

f.close()

f=open(r"E:\STUDY 12 Saksham\CS school\Practical\records1.dat", "rb")
roll=int(input("Enter the Roll Number: "))
marks=float(input("Enter the updated marks: "))
List = [ ]
flag = False 
while True:
    try:
        record=pickle.load(f)
        List.append(record)
    except EOFError:
        break
f.close()

f=open(r"E:\STUDY 12 Saksham\CS school\Practical\records1.dat","wb")
for rec in List:
    if rec[0]==roll:
        rec[2] = marks
        pickle.dump(rec, f)
        print("Record updated successfully")
        flag = True
    else:
        pickle.dump(rec,f)
f.close()
if flag==False:
    print(r"This roll number doesn't exist")
