def myfunc(st):
    rst = []
    res = ''
    for index in range(len(st)):
        if index%2 == 0:
            rst.append(st[index].upper())
        else:
            rst.append(st[index].lower())
    print (res.join(rst))
myfunc("bigoof")


