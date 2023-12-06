# index operator [] = gives access to sequence's element (str,list,tuples)

name = "bro code"
if(name[0].islower()):
    name = name.capitalize()

print(name)

first_name = name[0:3].upper()
last_name = name[4:].lower()
last_character = name [-1]

print(first_name)
print(last_name)
print(last_character)