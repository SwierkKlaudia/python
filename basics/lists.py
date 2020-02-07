#   1
def L1(elements):
    sum_elem = 0
    for list_elem in elements:
        sum_elem += list_elem
    return sum_elem
print("L1:",L1([1, 4, 19]))

#   2
def L2(elements):
    mult_elem = 1
    for list_elem in elements:
        mult_elem *= list_elem
    return mult_elem
print("L2:",L2([1, 4, 19]))

#   3
def L3(elements):
    larg_numb = 0
    for list_elem in elements:
        if list_elem > larg_numb:
            larg_numb = list_elem
    return larg_numb
print("L3:",L3([1, 4, 19, 12, 3]))

#   5
def L4(strings):
    count_str = 0
    for list_str in strings:
        if len(list_str) > 4 and list_str[0] == list_str[-1]:
            count_str += 1
    return count_str
print("L4:",L4(['abh','qwerrtyuyq','abba','qazzaq','poilp','qwertyu','asdas']))

#   6
def L5(tuples):
    def keysort(n):
        return n[1]
    tuples.sort(key = keysort)
    return tuples
print("L5:",L5([(1,4), (3,3), (14,15), (12,1)]))

#   7
def L6(strings):
    no_duplic = []
    for list_str in strings:
        if list_str not in no_duplic:
            no_duplic += [list_str]
    return no_duplic
print("L6:",L6(['abh','qwertyu','abba','qazzaq','qwertyu','abba','poilp']))

#   10
def L7(strings, N):
    Nlength_list = []
    for list_str in strings:
        if len(list_str) >= N:
            Nlength_list += [list_str]
    return Nlength_list
print("L7:",L7(['abh','qwerrtyuyq','abba','qazzaq','poilp','qwertyu','asdas'],5))

#   11
def L8(list1,list2):
    statement = 'False'
    for list_elem in list1:
        if list_elem in list2:
            statement = 'True'
    return statement
print("L8:",L8([1, 4, 19, 12, 3],[1, 14, 19, 123, 31]))

#   12
def L9(elements):
    numb = [0, 4, 5]
    del_str = []
    for list_elem in elements:
        if list_elem not in numb:
            del_str += [list_elem]
    return del_str
print("L9:",L9([0, 1, 2, 3, 4, 5, 6, 7]))

#   14
def L10(elements):
    del_str = []
    for list_elem in elements:
        if list_elem % 2 == 1:
            del_str += [list_elem]
    return del_str
print("L10:",L10([1, 4, 19, 12, 3]))

#   16
def L11(elements):
    square_str = []
    for list_elem in elements:
        list_elem*= list_elem
        square_str += [list_elem]
    return (square_str[:5],square_str[-5:])
print("L11:",L11(range(1,15)))

#   18
def L12(elements):
    permut = []
    for i in elements:
        for j in elements:
            if j != i:
                permut.append((i,j))
    return permut
print("L12:",L12([1, 2, 3]))

#   19
    #diff_str = set(list1) - set(list2)
    #return list(diff_str)

def L13(list1,list2):
    new_str = []
    for elem in list1:
        if elem not in list2:
            new_str.append(elem)
    return new_str
print("L13:",L13([1, 4, 19, 12, 3],[1, 14, 19, 123, 4]))

#   12
def L14(strings):
    delet_str = []
    numb_delet = [0,4,5]
    for (i,x) in enumerate(strings):
        if i not in numb_delet:
            delet_str += [x]
    return delet_str
print("L14:",L14(['zero','first','second','third','fourth','fifth','sixth']))

#   21
def L15(elements):
    str_elem = ''.join(elements)
    return str_elem
print("L15:",L15(['a','b','c','d']))

#   20
def L16(elements, n):
    index_elem = 0
    for (i,x) in enumerate(elements):
        if x == n:
            index_elem = i
    return index_elem
print("L16:",L16([0, 1, 12, 43, 46, 53, 6, 7],12))

#   23
def L17(list1, list2):
    flat_list = list1
    for elem in list2:
        flat_list += [elem]
    return flat_list
print("L17:",L17([1, 4, 19, 12, 3],[1, 14, 19, 123, 4]))

#   27
def L18(elements):
    snd_number = 0
    elements.sort()
    for (i,x) in enumerate(elements):
        if i == 1:
            snd_number = x
    return snd_number
print("L18:",L18([1, 4, 19, 12, 3, -11, -3]))

#   29
def L19(elements):
    new_str = []
    for i in elements:
        if i not in new_str:
            new_str.append(i)
    return new_str
print("L19:",L19([1, 4, 19, 12, 1, 12, 55]))

#31
def L20(elements, small, large):
    counter = 0
    for i in elements:
        if i >= small and i <= large:
            counter += 1
    return counter
print("L20:",L20([1, 4, 19, 12, 1, 13, 55], 4, 12))

#37
def L21(list1, list2):
    same_elem = []
    for i in list1:
        if i in list2:
            same_elem.append(i)
    return same_elem
print("L21:",L21([1, 4, 19, 12, 3],[1, 14, 19, 123, 4]))

#44
def L22(elements):
    group = []
    list_group = []
    for (i,x) in enumerate(elements):
        group.append(x)
        if (i+1) % 3 == 0:
            list_group.append(group)
            group = []
    if len(elements) % 3 != 0:
        list_group.append(group)
    return list_group
print("L22:",L22([1, 4, 19, 12, 3, 14, 191, 123, 43, 11]))


#46
def L23(elements):
    new_list = []
    for (i,x) in enumerate(elements):
        if i % 2 == 0:
            new_list.append(x)
    return new_list
print("L23:",L23([1, 4, 19, 12, 3, 14, 191, 123, 43, 11]))


#51
def L24(elements,N):
    group = []
    list_group = []
    for (i,x) in enumerate(elements):
        group.append(x)
        if (i+1) % N == 0:
            list_group.append(group)
            group = []
    if len(elements) % N != 0:
        list_group.append(group)
    return list_group
print("L24:",L24([1, 4, 19, 12, 3, 14, 191, 123, 43, 11],4))


#56
def L25(string):
    new_list = list(string)
    return new_list
print("L25:",L25('ELEMENT'))


#63
def L26(list1,string):
    for (i,x) in enumerate(list1):
        x = string + x
        list1[i] = [x]
    return list1
print("L26:",L26(['aaa','bbb','ccc','ddd','eee'],'XXX'))


#64
def L27(list1,list2):
    new_string = ''
    for i in list1:
        new_string = new_string + i
    for j in list2:
        new_string = new_string + j  
    return new_string
print("L27:",L27(['aaa','bbb','ccc','ddd','eee'],['xxx','yyy','zzz']))



#69
def L28(list1):
    new_list = []
    for i in list1:
        if i not in new_list:
            new_list.append(i)
    return new_list
print("L28:",L28([[10, 20], [40], [30, 56, 25], [10, 20, 11], [33], [40],[]]))



###
def L29(list1, list2):
    statement = 'True'
    for (i,x) in enumerate(list1):
        if x.lower() != (list2[i]).lower():
            statement = 'False'
    return statement
print("L29:",L29(['Aaa','bb','cCcd'],['aaa','bb','CCC']))



###
def L30a(list1, list2):
    new_list = []
    for i in list1:
        if i in list2:
            new_list.append('...')
        else:
            new_list.append(i)
    return new_list
print("L30a:",L30a(['Aaa','bb','cCc', 'aaa'],['aaa','bb','CCC']))


###
def L30b(list1, list2):
    new_list = []
    for i in list1:
        dots = ''
        ctr = 0
        if i in list2:
            j = len(i)
            while ctr < j:
                ctr += 1
                dots += '.'
            new_list.append(dots)
        else:
            new_list.append(i)
    return new_list
print("L30b:",L30b(['Aaa','bb','cCc', 'aaa'],['aaa','bb','CCC']))



###
def L30c(list1, list2):
    new_list = []
    floor = '_'
    def appnd(oldelem,newelem,lists):
        if newelem in lists:
            new_list.append('...')
        else:
            new_list.append(oldelem)
        return new_list
    for i in list1:
        if i.endswith('_') == 1 or i.startswith('_') == 1:
            j = i.replace('_', '')
            appnd(i,j,list2)
        else:
            appnd(i,i,list2)
    return new_list
print("L30c:",L30c(['_Aaa','_bb','cCc', 'aaa'],['aaa','bb','CCC']))


###
def L30d(list1, list2):
    new_list = []
    for i in list1:
        if i not in list2:
            new_list.append(i)         
    return new_list
print("L30d:",L30d(['Aaa','bb','cCc', 'aaa'],['aaa','bb','CCC']))


###
def L31(list1, list2):
    new_list = []
    indx = -1
    new_word = ''
    word_len = 0
    for i in list1:
        word_len = len(i)
        for j in list2:
            if word_len == 0:
                new_word = '?'
            elif j.find(i) != -1:
                indx = j.find(i)
                new_word = j[(word_len+1):]
        if indx != -1:
            new_list.append(new_word)
            indx = -1
        else:
            new_list.append('?')
    return new_list
print("L31:",L31(['kot','pies','kon',''],['pies:dog','kot:cat','dom:house']))



###
def L32a(listA, animal, plant, unit):
    new_list = []
    for elem in listA:
        if elem in animal:
            new_list.append(elem + ':animal')
        elif elem in plant:
            new_list.append(elem + ':plant')
        elif elem in unit:
            new_list.append(elem + ':unit')
        else:
            new_list.append(elem)
    return new_list
print("L32a:",L32a(['kilogram','mouse','tree','stone'],['dog','cat','mouse'],['tree','grass','flower'],['meter','kilogram','newton'],))



###
def L32b(listA, animal, mammal, pet):
    new_list = []
    for elem in listA:
        if elem in animal:
            if elem in mammal:
                new_list.append(elem + ':animal:mammal')
            elif elem in pet:
                new_list.append(elem + ':animal:pet')
            else:
                new_list.append(elem + ':animal')
        elif elem in mammal:
            new_list.append(elem + ':mammal')
        elif elem in pet:
            new_list.append(elem + ':pet')
        else:
            new_list.append(elem)
    return new_list
print("L32b:",L32b(['horse','stone','frog'],['dog','horse','frog'],['horse','dog'],['cat']))



###
def L33(list1):
    new_list = []
    counter = 0
    new_elem = []
    for elem in list1:
        counter = list1.count(elem)
        new_elem = [elem,counter]
        if new_elem not in new_list:
            new_list.append(new_elem)
    return new_list
print("L33:",L33(['pies','kot','kot','zaba','kon','kon','kon','panda']))


###
def L34(string1):
    new_list = string1.split(' ')
    for (i,x) in enumerate(new_list):
        if not x.isalpha():
            new_list[i] = f'<b>{x}</b>'
    new_str = ' '.join(new_list)
    return new_str
print("L34:",L34('Lczba 7 dzielona przez 2 daje liczbe 3.5 a 1 przez 8 daje liczbe 0.128'))



###
def L35(string1):
    numbers_float = []
    precisions = []
    new_list = string1.split(' ')
    for (i,x) in enumerate(new_list):
        if not x.isalpha():
            precisions.append(len(x) - x.find('.') - 1)
            numbers_float.append([i,float(x)])
    for [n,flt] in numbers_float:
        new_list[n] = f'{flt:.{min(precisions)}f}'
    new_str = ' '.join(new_list)
    return new_str
print("L35:",L35('ala 1.23456 ma 12.3456 kota 123.456'))



###
def L36(string1):
    numbers_i = []
    numbers = []
    new_list = string1.split(' ')
    for (i,x) in enumerate(new_list):
        if not x.isalpha():
            numbers_i.append([i,float(x)])
            numbers.append(float(x))
    for [n,flt] in numbers_i:
        if flt == max(numbers):
            new_list[n] = f'<font color=\'red\'>{flt}</font>'
        elif flt == min(numbers):
            new_list[n] = f'<font color=\'green\'>{flt}</font>'
    new_str = ' '.join(new_list)
    return new_str
print("L36:",L36('1 dzielone przez 8 daje 0.128 a 7 dzielone przez 2 daje 3.5'))











