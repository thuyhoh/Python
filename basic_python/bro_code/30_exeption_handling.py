# exception = evens detected during execution that interrup the flow of a programing

try:
    number_1 = int(input("enter a number to divide: "))
    number_2 = int(input("enter a number to devide by: "))
    result = number_1/number_2
except ZeroDivisionError as e:
    print(e)
    print("you can't divide by zezo! idiot!")
except ValueError as e:
    print(e)
    print("enter only number plz")
except Exception as e:
    print(e)
    print("something went wrong")
else:
    print(result)
finally:
    print("this will always execute")