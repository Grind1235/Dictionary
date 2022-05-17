# for question 1



myObejct = {
    'name' : 'Alon',
     'age' : 12,
    'bith date': '1975/01/05'

}

print(myObejct)



# for question 2
myObejct = {
    'name' : 'Alon',
     'age' : 12,
    'bith date': '1975/01/05'

}

myObejct['lastName'] = 'vilces'

print(myObejct)



# for question 3


myObejct = {
    'name' : 'Alon',
     'age' : 12,
    'bith date': '1975/01/05'

}

myObejct['Hobbies'] =  'Drink Coffe' , 'Playing video games' , 'Watching a movie','Soccer'

print(myObejct)



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

print(Object())




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

for i in objectSet.intersection(objectSet2):
    print(myObejct[i])



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

for i in objectSet.intersection(objectSet2):
    print(i)



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

print("9: " + str(Comparing_keys(myObejct, 'name')))


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

print("10: " + str(Comparing_values(myObejct, 12)))






#for question 11
myObejct = {
    'name': 1,
    'age2': 6,
    'bith date3': 22,
    'equal': 12
}

convertObjec=list(myObejct.items())
convertObjec.sort()
print(convertObjec)