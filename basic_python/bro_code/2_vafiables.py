# variable = a cpntainer for a value. behaves as the value that it contains

    ### str

name = "thuy"
print("hello "+ name) # hello thuy
print(type(name)) # print data type of name

first_name = "nguyen"
last_name = "trong thuy"
full_name = first_name +" "+ last_name
print("hello "+ full_name) # hello nguyen trong thuy
 

    ### int
age = 18
age += 1 # age = age +1
print("your age is: " + str(age)) # string cast
print(type(age))

    ### float
height = 1.75
print("ypur hieght is: " + str(height) + "m")
print(type(height))

    ### boolen ( True/False )
human = True
print("Are you " + str(human))
print(type(human))

# multiple assignment = allows us to assign multiple variables at the same time in one line of code

name, age, attractive = "thuy", 19, True
# name = "thuy"
# age = 19
# attractive = True
