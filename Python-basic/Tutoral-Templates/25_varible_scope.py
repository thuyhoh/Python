# scope = the region that a variable is recognized
#         a variable is only available from onside the region it is created
#         a global and local scoped version of a vatiable can be created

name = "bro" # global scope (available inside & outside function)

def display_name():
    naem = "code" # local scope (available only inside this funcion)
    print(name)

display_name()
print(name)