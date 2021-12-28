fin = open(r'E:\STUDY 12 Saksham\CS school\Practical\mytextfile3.txt','r')
fout = open(r'E:\STUDY 12 Saksham\CS school\Practical\mytextfile3(2).txt','w')

lines = fin.readlines()
for i in lines:
    if 'a' in i:
        pass
    else:
        fout.write(i)

fin.close()
fout.close()
         
         
