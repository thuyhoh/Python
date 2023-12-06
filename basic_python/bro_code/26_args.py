# *args = parameter that whill pack all arguments into  a tuple
#         useful so tha t  a function can accept a varying amout of  arguments

def add(*stuff):
    sum = 0
    for i in stuff:
        sum += i
    return sum

print(add(1,2,3,4,5,6,7,8))


# you don't change value in stuff -> errol (because stuff is tuple)
# if you want to change, you must casting stuff(tuple) -> list

def change(*stuff):
    stuff = list(stuff)
    stuff[0] = 1000
    return stuff
    
print(change(1,2,3,4,5,6))