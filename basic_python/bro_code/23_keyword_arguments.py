# keyword arguments = arguments preceded by an identifier when we pass them to a function
#                     the order of the arguments doesn't matter, unlike positional arguments
#                     python knows the names of the arguments that our function receives

def hello(first, middle, last):
    print("hello "+ first +" "+ middle +" "+ last)

hello("thuy","nguyen","trong")
print("\n")
hello(first = "nguyen", middle = "trong", last = "thuy")