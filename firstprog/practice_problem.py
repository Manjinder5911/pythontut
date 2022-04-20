
user_input = int(input("please enter your age or year of birth : \n"))
if user_input < 100:
    year_birth = 2022 - user_input
    a = 100 - user_input
    print(f"your age by 2090 will be {2090 - year_birth}")
    print(f"you will turn 100 years old by {2022+a}")

elif  100 <= user_input <= 1922:
    print("Impressive, you seem to be oldest person alive. Please enter valid input")

elif 1922 < user_input < 2022:
    print(f"your age by 2090 will be {2090 - user_input}")
    print(f"you will turn 100 years old by {user_input + 100}")

elif user_input >= 2022:
    print(f"you are not born yet. Please enter valid input")

else:
    print("Error in your input")

b = input("Now if you want to know about your age by any particular year enter y,otherwise n : \n")
if b == "y":
    user_input2 = int(input("enter the year: \n"))
    if user_input < 100:
        if year_birth < user_input2:
            print(f"Your age by {user_input2} is {user_input2 - year_birth}")
        else:
            print("you have not entered correct year ")
    elif 1922 < user_input < 2022:
        if user_input < user_input2:
            print(f"Your age by {user_input2} is {user_input2 - user_input}")
        else:
            print("you have not entered correct year ")
    else:
        print("Sorry, you have not entered your valid age")

elif b != "n":
    print("enter valid input")




