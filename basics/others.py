###
def I1a(str1):
    edges = 0
    for i in range(0,len(str1)-1):
        if str1[i] != str1[i-1]:
            edges += 1
    return edges
print("I1a:",I1a('01011001'))


def I1b(str1):
    str2 = '-'
    for i in range(1,len(str1)):
        if str1[i] != str1[i-1]:
            str2 += '*'
        else:
            str2 += '-'
    return str2
print("I1b:",I1b('00111000100001'))


def I1c(str1):
    str2 = '-'
    for i in range(1,len(str1)):
        if str1[i] != str1[i-1]:
            if str1[i] == '1':
                str2 += 'r'
            else:
                str2 += '-'
        else:
            str2 += '-'
    return str2
print("I1c:",I1c('001110100001'))



def I1d(str1):
    counter = 0
    max_ctr = 0
    lst2 = ['-']
    for i in range(1,len(str1)):
        if str1[i] != str1[i-1]:
            if str1[i] == '1':
                lst2 += 'r'
                counter = 0
            else:
                lst2 += '-'
                counter += 1
        else:
            lst2 += '-'
            counter += 1
        if counter > max_ctr:
            max_place = i + 1
            max_ctr = counter
    lst2[max_place] = 'x'
    str2 = ''.join(lst2)
    return str2
print("I1d:",I1d('0011101000011010'))


def I1e(str1):
    counter = 0
    max_ctr = 0
    periods = []
    for i in range(1,len(str1)):
        if str1[i] != str1[i-1]:
            if str1[i] == '1':
                periods += [counter+1]
                counter = 0
            else:
                counter += 1
        else:
            counter += 1
        if counter > max_ctr:
            max_ctr = counter
    av_period = sum(periods[1:])/2
    return av_period
print("I1e:",I1e('001110100001'))




def I1f(str1):
    counter = 0
    max_ctr = 0
    periods = []
    squares = []
    odch_stand = 0
    for i in range(1,len(str1)):
        if str1[i] != str1[i-1]:
            if str1[i] == '1':
                periods += [counter+1]
                counter = 0
            else:
                counter += 1
        else:
            counter += 1
        if counter > max_ctr:
            max_ctr = counter
    av_period = sum(periods[1:])/2
    ####
    for x in periods[1:]:
        squares += [(x-av_period)**2]
        counter += 1
    och_stand = (sum(squares)/counter)**(1/2)
    return och_stand
print("I1f:",I1f('001110100001'))



def I2(str1,str2):
    list1 = list(str1)
    list2 = list(str2)
    new_str = ''
    for i in range(0,len(str1)-1):
        if list1[i] == '1' and list2[i] == '1':
            new_str += '1'
        else:
            new_str += '0'
    return new_str
print("I2:",I2('001101010','101001100'))



def I3(strSDA,strSCL):
    listSDA = list(strSDA)
    listSCL = list(strSCL)
    new_str = '-'
    for i in range(1,len(strSDA)):
        if listSCL[i] == '1':
            if listSDA[i-1] == '1' and listSDA[i] == '0':
                new_str += 's'
            elif listSDA[i-1] == '0' and listSDA[i] == '1':
                new_str += 't'
            else:
                new_str += '-'
        elif listSCL[i] == ' ':
            new_str += ' '
        else:
            new_str += '-'
    return new_str
print("I3:",I3('1100 0011','1111 1111'))


def I4a(str1):
    new_str = ''
    new_lst = []
    lst_str = str1.split('. ')
    for i in lst_str:
        x = i.capitalize()
        new_lst.append(x)
    new_str = '. '.join(new_lst)
    return new_str
print("I4a:",I4a('ala ma kota. kot ma ale. domki dwa'))


def I4b(str1,ctr_space):
    new_str = ''
    str_space = ''
    lst_str = str1.split(',')
    while ctr_space != 0:
        str_space += ' '
        ctr_space -= 1
    new_str = f'{str_space},{str_space}'.join(lst_str)
    return new_str
print("I4b:",I4b('ala ma kota,kot ma ale, domki dwa',3))



def I5(str1,ctr_space):
    new_str = ''
    new_lst = []
    len_list = []
    lst_str = str1.split('\n')
    for k in lst_str:
        len_list += [len(k)]
    max_len = max(len_list)
    for i in lst_str:
        x = i.rjust(max_len)
        new_lst.append(x)
    new_str = '\n'.join(new_lst)
    return new_str
print("I5:",I5('\naaaaaaaaa\nbbd\nc\neeee',20))


def I5vol2(str1,ctr_space):
    new_str = ''
    new_lst = []
    lst_str = str1.split('\n')
    for i in lst_str:
        x = i.rjust(ctr_space)
        new_lst.append(x)
    new_str = '\n'.join(new_lst)
    return new_str
print("I5vol2:",I5vol2('\naaaaaaaaa\nbbd\nc\neeee',20))




def I6(str1):
    new_str = ''
    new_lst = []
    lst_str = str1.split('\n')
    for i in lst_str:
        if i != '':
            new_lst.append(i)
    new_str = '\n'.join(new_lst)
    return new_str
print("I6:",I6('\naaaaaaaaa\n\nbb\n\n\nd\nc\neeee'))




def I7a(str1):
    new_str = ''
    new_lst = []
    lst_str = str1.split('\n')
    for i in lst_str:
        if i.find('err') != -1:
            x = '*' + i
            new_lst.append(x)
        else:
            new_lst.append(i)
    new_str = '\n'.join(new_lst)
    return new_str
print("I7a:",I7a('\naaaerraaaaaa\nbbd\nc\neerree'))


def I7b(str1):
    new_str = ''
    new_lst = []
    lst_str = str1.split('\n')
    for i in lst_str:
        lst_words = i.split(' ')
        x = i
        for j in lst_words:
            k = j.lower()
            if k == 'error':
                x = '*' + i
        new_lst.append(x)
    new_str = '\n'.join(new_lst)
    return new_str
print("I7b:",I7b('\naaaerraaa error aaa\nbbdERROR\nc\ne eRRoR ee'))


def I7c(str1):
    new_str = ''
    new_lst = []
    lst_str = str1.split('\n')
    for i in lst_str:
        lst_words = i.split(' ')
        x = i
        for j in lst_words:
            if not j.isalpha():
                x = '*' + i
        new_lst.append(x)
    new_str = '\n'.join(new_lst)
    return new_str
print("I7c:",I7c('\naaaerraaa 12.345 aaa\nbbdERROR\nc\ne eRRoR ee'))



def I8(str1):
    new_str = ''
    new_lst = []
    lst_str = str1.split(' ')
    for i in lst_str:
        if i != '':
            new_lst.append(i)
    new_str = ' '.join(new_lst)
    return new_str
print("I8:",I8('ala ma   kota         xdd '))






