dict1 = {'dog' : 4,'human': 2}
dict2 = {'cat':'purr', "horse":"Neigh",'dog':'woof'}
dict3 = {}

def adddict(dict1,dict2):
    for i in dict1:
        for j in dict2:
            if i == j:
                dict3[i]=dict1[i]
            else:
                dict3[j] = dict2[j]
        dict3[i]=dict1[i]
    print(dict3)
adddict(dict1,dict2)
