# 2D list = a list of list

drinks = ["coffe","soda","tea"]
foods = ["pizza","hamburger","hotdog"]
deserts = ["cake","ice cream","bread"]

dinner = [drinks,foods,deserts]

print(dinner[1][1]) # dinner[1] -> foods and dinner[1][1] -> food[1] = hamburger
print("\n")

for i in range(2):
    for j in range(3):
        print(dinner[i][j])
