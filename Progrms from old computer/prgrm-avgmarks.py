def avgmarks():
    maxmarks = int(input('please enter the maximum marks obtainable: '))
    numsub = int(input('please enter the no. of subjects you have: '))
    markspercentage = []

    for i in range(numsub):
        marks = int(input('please enter the marks obtained: '))
        markspercentage.append(marks*100/maxmarks)
    total = 0
    for i in markspercentage:
        total = +i
    aggrigatepercentage = total*100/numsub
    print('Your aggrigate percentage is',aggrigatepercentage)

avgmarks()
        
