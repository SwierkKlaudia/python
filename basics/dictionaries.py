#   1
def D1(dict1):
    import operator
    sorted_dict = dict(sorted(dict1.items(), key=operator.itemgetter(1)))
    return sorted_dict
print("D1:",D1({1:2,5:4,3:1,4:0}))

def D1a(dict1):
    sorted_dict = dict(sorted(dict1.items(), key=(lambda v : v[1])))
    return sorted_dict
print("D1a:",D1a({1:2,5:4,3:1,4:0}))

#   3
def D2(dict1,dict2,dict3):
    new_dict = {}
    for k in (dict1,dict2,dict3):
        new_dict.update(k)
    return new_dict
print("D2:",D2({1:2,5:4,3:1},{2:3,0:6},{7:4,9:8}))

#   4
def D3(dict1,key):
    if key in dict1:
        answ = "Key is in dictionary"
    else:
        answ = "Key is not in dictionary"
    return answ
print("D3:",D3({1:2,5:4,3:1},5))


#   5
def D4(dict1):
    new_list = []
    for k in dict1:
        new_list.append(f"{k}:{dict1[k]}")
    return new_list
print("D4:",D4({1:2,5:4,3:1}))


#   6
def D5(rangeN):
    new_dict = {}
    for n in range(1,rangeN+1):
        new_dict.update({n:n*n})
    return new_dict
print("D5:",D5(5))

#   10
def D6(dict1):
    sum_val = sum(dict1.values())
    return sum_val
print("D6:",D6({1:2,5:4,3:1}))


#   11
def D7(dict1):
    mult_val = 1
    for k in dict1:
        mult_val *= dict1[k]
    return mult_val
print("D7:",D7({1:2,5:4,3:3}))


#   12
def D8(dict1,del_key):
    if del_key in dict1:
        dict1.pop(del_key)
    return dict1
print("D8:",D8({1:2,5:4,3:3},5))


#   13
def D9(keys,values):
    new_dict = dict(zip(keys,values))
    return new_dict
print("D9:",D9([1,2,3],[6,7,8]))



#   14
def D10(dict1):
    sorted_dict = dict(sorted(dict1.items()))
    return sorted_dict
print("D10:",D10({1:2,5:4,3:1,4:0}))



#   15
def D11(dict1):
    key_MaxVal = max(dict1.keys(), key=(lambda k : dict1[k]))
    return key_MaxVal
print("D11:",D11({1:2,5:4,3:1,4:10}))



#   17
def D12(dict1):
    new_dict = {}
    for k,v in dict1.items():
        if v not in new_dict.values():
            new_dict[k] = v
    return new_dict
print("D12:",D12({1:2,5:4,3:1,4:10,5:4,6:2}))


#   19
def D13(dict1,dict2):
    for k in dict2:
        if k in dict1:
            dict1[k] += dict2[k]
        else:
            dict1[k] = dict2[k]
    return dict1
print("D13:",D13({1:2,5:4,3:1,4:10},{11:2,5:7,3:4,14:1}))


###
def D14(string1):
    new_dict = {}
    for i in string1:
        if i in new_dict:
            new_dict[i] += 1
        else:
            new_dict[i] = 1
    return new_dict
print("D14:",D14('ala ma kota'))



###
def D15(list1):
    new_dict = {}
    for i in list1:
        new_dict[i] = len(i)
    return new_dict
print("D15:",D15(['ala','ma','fajnego','kota']))



###
def D16(list1, dict1):
    new_list = []
    for i in list1:
        if i in dict1:
            new_list.append(dict1[i])
        else:
            new_list.append('...')
    return new_list
print("D16:",D16(['ala','ma','fajnego','kota'],{'ma':'has','fajnego':'nice','kota':'cat'}))


###
def D17a(list1):
    max_age = 0
    for dicts in list1:
        if dicts['age'] > max_age:
            max_age = dicts['age']
            oldest = dicts['name']
    return oldest
print("D17a:",D17a([{'name':'Zawisza', 'age':35, 'heigth': 150, 'married': True},
{'name':'Malińska','age':25, 'heigth': 170, 'married': True},
{'name':'Adamski', 'age':15, 'heigth': 160, 'married': False}]))


###
def D17b(list1):
    higher150 = []
    for dicts in list1:
        if dicts['heigth'] > 150:
            higher150.append(dicts['name'])
    return higher150
print("D17b:",D17b([{'name':'Zawisza', 'age':35, 'heigth': 150, 'married': True},
{'name':'Malińska','age':25, 'heigth': 170, 'married': True},
{'name':'Adamski', 'age':15, 'heigth': 160, 'married': False}]))









