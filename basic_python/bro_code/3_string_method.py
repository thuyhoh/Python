name = "nguyen trong thuy"
class_ = ["name", "age", "class"]

print(len(name)) # lenght of string
# 17
print(name.find("g")) # find in the string the first appearent of "g"
# 1
print(name.capitalize()) #capitalize the first letter
# Nguyen trong thuy
print(name.upper())
# NGUYEN TRONG THUY
print(name.lower())
# nguyen trong thuy
print(name.isdigit()) # return True if all of memmber in string is number
# False
print(name.isalpha()) # return True if all of memmber in the string is alpha
# False (have " ")
print(name.count("g")) # count "g" in the string
# 2
print(name.replace("a","g"))
# nauyen trona thuy
print(name*3) # display "nguyen trong thuy" three times

s1 = name.split(" ") #s1 = ["nguyen", "trong", "thuy"]
for i in s1:
    print (i)

s2 = ","
s2 = s2.join(class_)
print(s2)
