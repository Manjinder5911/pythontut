import random

print("welcome to the game")
lst = ["snake","water","gun"]

a = 10
c = 0
d = 0
e = 0
while 1:
    comp = random.choice(lst)
    b = input("enter your choice (s,w or g) :\n")
    if comp == "snake" and b == "w" or comp == "gun" and b == "s" or comp == "water" and b == "g":
        c = c + 1
        print("you lost")
    elif comp == "water" and b == "s" or comp == "snake" and b == "g" or comp == "gun" and b == "w":
        d = d + 1
        print("you won")
    elif comp == "snake" and b == "s" or comp == "gun" and b == "g" or comp == "water" and b == "w":
        e = e + 1
        print("tie")
    else:
        print("enter valid input,you lost")
        c = c + 1

    a = a-1
    if a == 0:
        print("game is over")
        if c > d:
            print("you lost the game")
        elif c < d:
            print("you won the game")
        else:
            print("game is a tie")
        print(" number of games you won",d)
        print(" number of games computer won", c)
        print(" number of games which are tie", e)
        break