import pickle
e1={"empno":1,"name":"siya"}
e2={"empno":2,"name":"raghav"}
e3={"empno":3,"name":"abhinav"}
fh = open("E:\\STUDY 12 Saksham\\CS SHIT\\subject\\computerscience.dat","wb")

pickle.dump(e1,fh)
pickle.dump(e2,fh)
pickle.dump(e3,fh)

print('data written succesfully')

fh.close()
