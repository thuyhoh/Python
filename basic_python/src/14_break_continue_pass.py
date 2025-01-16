# loop control statements = change a loops execution from its normal sequence

# break = used to terminate the loop entirely
# continue = skips to the nnext iteration of the loop
# pass = does nothing, acts as a placeholder

# while True:
#     name = input("enter your name : ")
#     if name != "":
#         break

phone_number = "123-456-789"
for i in range(len(phone_number)):
    if phone_number[i] == "-":
        pass
    print(phone_number[i],end = "")

for i in phone_number:
    if i == '-':
        pass
    else:
        print(i)
    