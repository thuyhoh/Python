# str.format() = optional method that gives users
#                more control when displaying output

animal = "cow"
item = "moon"
print("the {} jumped over the {}".format(animal,item))
# print("the "+ animal+" jumped over the "+ item)
print("the {1} jumped over the {0}".format(animal,item)) # positional argument
# animal(0) and item(1) ==> the moon jumped over the cow
print("the {s1} jumped over the {s2}".format(s1 = "cow",s2 = "moon")) # keyword arguments

text ="the {0} jumped over the {1}"
print(text.format(animal,item))



# padding of format

name = "bro"
print("hell, my name is {}. Nice to meet you!".format(name))
print("hell, my name is {:10}. Nice to meet you!".format(name))
print("hell, my name is {:<10}. Nice to meet you!".format(name))
print("hell, my name is {:>10}. Nice to meet you!".format(name))
print("hell, my name is {:^10}. Nice to meet you!".format(name))


# format of number

pi = 3.14159

print("the number pi is {:.3f}".format(pi))     
print("the number pi is {}".format(round(pi)))


number2 = 1000000 
print("the number is {:,}".format(number2))
print("the number is {:b}".format(number2)) # number2 ==> binary
print("the number is {:x}".format(number2)) # number2 ==> hexa
print("the number is {:e}".format(number2)) # number2 ==> 1e+7 