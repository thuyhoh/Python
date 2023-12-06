import random

x = random.randint(1,6) # random [1->6]
print(x)
y = random.random()     # [0,1)
print(y)

# rock, paper and scissors
list = ["rock","paper","scissors"]
pc_choice = random.choice(list)
your_choice = input("choice 'rock'or'paper' or 'scissors'")
print(pc_choice)
if(pc_choice == "rock"):
    if(your_choice == "paper"):
        print("you win")
    elif(your_choice == "rock"):
        print("you peace")
    elif(your_choice == "scissors"):
        print("you lose")

if(pc_choice == "paper"):
    if(your_choice == "paper"):
        print("you peace")
    elif(your_choice == "rock"):
        print("you lose")
    elif(your_choice == "scissors"):
        print("you win")

if(pc_choice == "scissors"):
    if(your_choice == "paper"):
        print("you win")
    elif(your_choice == "rock"):
        print("you lose")
    elif(your_choice == "scissors"):
        print("you peace")

cards = [2,3,4,5,6,7,8,9,10,"J","Q","K","A"]
random.shuffle(cards)
print(cards)