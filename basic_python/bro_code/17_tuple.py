# tuple = collection which is ordered and unchangeable
#         used to group together related data

student = ("nguyen trong thuy", 19, "male")

print(student[1]) # 19(index = 1)

print(student.count(19)) # count how many "19" appear in the tuple
print(student.index("male")) # index of male in the tuple


for i in student:
    print(i)

if "nguyen trong thuy" in student:
    print("you are here")