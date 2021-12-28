import pickle

f=open(r"E:\STUDY 12 Saksham\CS school\Practical\records.dat", "wb")
pickle.dump(["Saksham", 1], f)
pickle.dump(["Tanish", 2], f)
pickle.dump(["Priyashi", 3], f)
pickle.dump(["Harjot", 4], f)
pickle.dump(["Gautam", 5], f)
f.close()


f=open(r"E:\STUDY 12 Saksham\CS school\Practical\records.dat", "rb")
n=int(input("Enter the Roll Number: "))
flag = False
while True:
    try:
        x=pickle.load(f)
        if x[1]==n:
            print("Name: ", x[0])
            flag = True
    except EOFError:
        break
if flag==False:
    print("This Roll Number does not exist")
