import random
print("Welcome to the snake water gun Game")
def check(computer,player):
    if(computer==player):
        return 0
    if(computer==0 and player==1):
        return -1
    if(computer==2 and player==0):
        return -1
    if(computer==1 and player==2):
        return -1
    else:
        return 1


computer=random.randint(0,2)
player=int(input("Enter your input form 0 for Snake 1 for Water And 2 Gun :"))
score=check(computer,player)
print("you",player)
print("computer",computer)
if(score==0):
    print("It's a draw")
elif(score==1):
    print("You won")
else:
    print("You lose")       
