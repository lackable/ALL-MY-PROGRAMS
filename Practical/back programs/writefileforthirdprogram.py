f = open(r"E:\STUDY 12 Saksham\CS school\Practical\mytextfile3.txt","w")
f.writelines(['this is a line','\nthis is line without forbidden word',
         '\nthis is also a line','\nthis is line2 without the forbidden word'])
f.close()
