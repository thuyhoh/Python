# **kwargs = parameter that will pack all arguments into a ditionary
#            useful so that a function can accept a varying amount of  keyword argument

def hello(**kwargs):
    print("hello !",end=" ")
    for key,value in kwargs.items():
        print(value,end = " ")

hello(title = "mr", first = "nguyen", middle = "trong", last = "thuy")