# if statsment = a block of code that will execute if it's codition is True
# when one condition in the if statement True program will break of if statement

age = int(input("how old are you ? : "))
if age < 0:
    print("you haven't been born yet")
elif age < 18:
    print("you are a child")
else :
    print("you are adult")
