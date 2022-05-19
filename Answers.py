# for question 1



myObejct = {
    'name' : 'Alon',
     'age' : 12,
    'bith date': '1975/01/05'

}





# for question 2
myObejct = {
    'name' : 'Alon',
     'age' : 12,
    'bith date': '1975/01/05'

}

myObejct['lastName'] = 'vilces'





# for question 3


myObejct = {
    'name' : 'Alon',
     'age' : 12,
    'bith date': '1975/01/05'

}

myObejct['Hobbies'] =  'Drink Coffe' , 'Playing video games' , 'Watching a movie','Soccer'





#for question 4

def Object():
    myObejct = {
        'name': 'Alon',
        'age': 12,
        'bith date': '1975/01/05'

    }

    if  'name' in myObejct:
        return True

    else:
        return False






#for question 5

def Object():
    myObejct = {
        'name': 'Alon',
        'age': 6,
        'bith date': '1975/01/05'

    }

    if  myObejct['age'] == 6:
        return True

    else:
        return False


print(Object())

#for question 6


myObejct = {
    'name': 'Alon',
    'age': 6,
    'bith date': '1975/01/05',
    'equal' : 12
}

if myObejct['age'] == myObejct['equal']:
    print(True)


else:
    print(False)





#for question 7


myObejct = {
    'name': 'Alon',
    'age': 6,
    'bith date': '1975/01/05',
    'equal' : 12
}

myObejct2 = {
    'name': 'Alon',
    'age': 6,
    'bith date': '1975/01/05',
    'equal' : 12
}


objectSet = set(myObejct)
objectSet2 = set(myObejct2)





#for question 8

myObejct = {
    'name1': 'Alon',
    'age2': 6,
    'bith date3': '1975/01/05',
    'equal' : 12
}

myObejct2 = {
    'name': 'Alon',
    'age': 6,
    'bith date': '1975/01/05',
    'equal' : 12
}

objectSet = set(myObejct)
objectSet2 = set(myObejct2)

#for i in objectSet.intersection(objectSet2):
   #print(i)



#for question 9


def Comparing_keys(myObejct,name):
    if name in myObejct.keys():
        return True
    else:
        return False


myObejct = {
        'name': 'Alon',
        'age2': 6,
        'bith date3': '1975/01/05',
        'equal': 12
    }



#for question 10


def Comparing_values(myObejct,age):
    if age in myObejct.values():
        return True
    else:
        return False

myObejct = {
        'name': 'Alon',
        'age2': 6,
       'bith date3': '1975/01/05',
       'equal': 12
    }








#for question 11
myObejct = {
    'name': 1,
    'age2': 6,
    'bith date3': 22,
    'equal': 12
}

convertObjec=list(myObejct.items())
convertObjec.sort()






#for question 12

def update_dict(myObejct,key,value):
      myObejct[key] = value
      return myObejct

myObejct = {
    'name': 1,
    'age2': 6,
    'bith date3': 22,
    'equal': 12
}






#for question 13

def build_dict_from_list(list1,list2):
    dict = {}
    if len(list1) == len(list2):
        for i in range(len(list1)):
            dict[list1[i]] = list2[i]
        return dict
    else:
        return None

#for question 14


def buliding_dict_with_pow(x):
    dict = {}
    for i in range(1,x+1):
        dict[i] = pow(i,2)
    return dict





#for question 15


def buliding_dict_with_addition(x):
    dict = {}
    for i in range(1,x+1):
        dict[x] = x % 10
    return dict






#for question 16


def buliding_dict_with_addition(x):
    dict = {}
    for i in range(1,x+1):
        dict[i] = i + i
    return dict


def buliding_dict_with_pow(x):
    dict = {}
    for i in range(1,x+1):
        dict[i] = pow(i,2)
    return dict

def buliding_tuple(x):
    a = buliding_dict_with_pow(x)
    b = buliding_dict_with_addition(x)
    c = a[1]
    z = b[1]
    tuple = (c,z)
    return tuple




#for question 17

def buliding_dict_with_addition(x):
    dict = {}
    for i in range(1,x+1):
        dict[i] = i + i
    print(max(dict))
    print(min(dict))

#for question 18
def buliding_dict_from_pop(x):
    dict = {}
    for i in range(1,x+1):
        dict[i] = i + i
        if dict[i] == max(dict):
            dict[i] = dict.pop(i)

        elif dict[i] == min(dict):
            dict[i] = dict.pop(i)
        else:
            pass
        return dict[i]





#for question 19
def checking_for_common_keys_in_dict(key,myObejct):

    if key in myObejct:
        myObejct.pop(key)
    else:
        myObejct

    return myObejct
myObejct = {
        'name': 1,
        'age': 6,
        'bith date': 22,
        'equal': 12
    }







#for question 20
def get_key(dict, val):
    for key, value in dict.items():
        if val == value:
            return key




def checking_for_common_values_in_dict(value, dict):
    while value in dict.values():
        del dict[get_key(dict, value)]
    print(dict)
    return dict
dict = {
        'name': 'Yair',
        'age': 6,
        'bith date': 'Yair',
        'equal': 12
    }





#for my question 21




def pop_keys_in_dict_if_exists(myObejct,keys_delete = ["name", "age"]):

    for key in keys_delete:
        myObejct.pop(key)
    return myObejct
    myObejct = {
        'name': 1,
        'age': 6,
        'bith date': 22,
        'equal': 12
    }






#for question 22*

def get_key(dict, val):
    for key, value in dict.items():
        if val == values_delete:
            return key


def pop_values_in_dict_if_exists(myObejct,values_delete = [1,6]):

    while values_delete in myObejct.values():
        del myObejct[get_key(myObejct, values_delete)]
    return myObejct


    myObejct = {
        'name': 1,
        'age': 6,
        'bith date': 22,
        'equal': 12
    }










#for question 23
def func(myObejct,keys_add):
    dict = {}
    for i in keys_add:
        dict = myObejct[i]
        print(dict)
myObejct =  {
        'name': 1,
        'age': 6,
        'bith date': 22,
        'equal': 12
}





#for question 24
def concet_dictionary(dict1,dict2):
    final_dict = {}

    for i in dict2:
        final_dict[i] = dict2[i]
    for j in dict1:
        final_dict[j] = dict1[j]
    return final_dict


dict1 = {
    'name': "Josh",
    'Current age': 6,
    'bith date': "22/01/1975",
    }
dict2 = {
        'name': "Yair",
        'age': 6,
        'bith year': "22/01/1975",
    }



#for question 25*
def add_the_last_dict(array_of):
    store_dict = {}


    return store_dict



dict1 = {
    'name': "Josh",
    'Current age': 53,
    'bith date': "22/01/1975",
}