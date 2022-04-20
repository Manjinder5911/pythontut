# try:
#     apple_input = int(input("enter the number of apples : \n"))
#     mn_range = int(input("enter the smallest no. of range: \n"))
#     mx_range = int(input("enter the highest no. of range: \n"))
# except ValueError:
#     print("enter integer only")
#
# if mn_range > mx_range:
#     print("min should be less than max")
# for i in range(mn_range,mx_range+1):
#     if apple_input%i == 0:
#         print(f"{i} is a divisor of {apple_input}")
#     elif apple_input%i != 0:
#         print(f"{i} is not a divisor of {apple_input}")
# a = []
# while True:
#     user_input = input("enter the no. to  be added in list or enter n to stop: \n")
#     if user_input == "n":
#         break
#     elif user_input.isnumeric() == True:
#         a.append(int(user_input))
#     else:
#         print("enter valid input")
#
# a.sort(reverse=True)
# print(f"calorie list is {a}")
#
#
# reverse1 = a[:]
# for i in range(len(reverse1)//2):
#     reverse1[i],reverse1[len(reverse1) -i -1] = reverse1[len(reverse1) -i -1],reverse1[i]
#
#
# print(f"reversed list is {reverse1}")
# slicing_reverse = a[::-1]
# print(f"reversed list using slicing {slicing_reverse}")
# inbuilt_reverse = a[:]
# inbuilt_reverse.reverse()
# print(f"reversed list {a} using method {inbuilt_reverse}")


# input_size = int(input("enter the number of test cases: \n"))
# list = []
#
# for i in range(input_size):
#     user_number = int(input("enter the input to obtain palindrome corresponding to that number: \n"))
#     list.append(user_number)
#
# numbers = []
# a = 0
# for j in list:
#    while True:
#        b = str(j)[::-1]
#        if str(j) == b:
#             numbers.append(j)
#             print(f"palindrome number for {a + 1} input is {numbers[a]}")
#             a += 1
#             break
#        else:
#            j = j + 1
#            continue

# taking input the size of list
# input_size = int(input("enter the size of list: \n"))
# list = []
#
# for i in range(input_size):
#     user_number = int(input("enter the input to obtain palindrome corresponding to that number: \n"))
#     list.append(user_number)
#
# numbers = []
#
# for j in list:
#    while True:
#        b = str(j)[::-1]
#        if str(j) == b and j > 10:
#             numbers.append(j)
#             break
#        elif str(j) != b and j > 10:
#            j = j + 1
#            # continue
#        else:
#            numbers.append(j)
#            break
# print(numbers)

# GUESS THE NUMBER
# import random
#
# # user_trials = []
# def player(name):
#     print(f"{name}\nPlease guess the number between {a} and {b}")
#     c = 1
#     while True:
#         try:
#             user_input = int(input(f"{c} attempt.Enter your guess: \n"))
#         except ValueError:
#             print("Invalid input.Please enter integer")
#         if user_input > rand:
#             print(f"Wrong guess.Your number is greater. Guess between {a} and {b}")
#             c += 1
#         elif user_input < rand:
#             print(f"Wrong guess.Your number is smaller. Guess between {a} and {b}")
#             c += 1
#         elif user_input == rand:
#             print(f"Correct guess.You took {c} trials to guess the number ")
#             # user_trials.append(c)
#             break
#     return c
#
#
#
#
# if __name__ == '__main__':
#     try:
#         a = int(input("enter any integer between which you want to guess number\nNumber1: \n"))
#         b = int(input("Number2: \n"))
#     except ValueError:
#         print("Invalid input.Please enter integer")
#     rand = random.randint(a, b)
#     p1 = player("Player 1")
#     p2 = player("Player 2")
#     if p1 > p2:
#         print("Player 2 wins!")
#     elif p1 < p2:
#         print("Player 1 wins!")
#     else:
#         print("match was a tie")

# SEARCH ENGINE
# def matchwords(sentence1,sentence2):
#     # strip will remove any extra spaces
#     words1 = sentence1.strip().split(" ")
#     words2 = sentence2.strip().split(" ")
#     score = 0
#     for word1 in words1:
#         for word2 in words2:
#             if word1.lower() == word2.lower():
#                 score += 1
#
#     return score
# if __name__ == '__main__':
#     list = ["how are you manjinder", "good manjinder is student", "manjinder is doing great"]
#     sentence1 = input("enter the query string:\n")
#     scores = [matchwords(sentence1,sentence2) for sentence2 in list]
#     output = []
#     for j in sorted(zip(list,scores),reverse=True):
#         if j[0] != 0:
#             output.append(j)
#     print(f"{len(output)} results found")
#     for item,key in output:
#         print(f"\"{key}\"")

# FUNNY NAMES
#
# input_size = int(input("enter the number of names:\n"))
# print(f"Enter the names below")
# names = []
# for i in range(input_size):
#     input_names = input()
#     names.append(input_names)
#
# first_name = []
# last_name = []
# a = []
# for i in range(len(names)):
#     first_name.append(names[i].split(" ")[0])
#     l_name = names[i].split(" ")[1:]
#     a = " ".join(l_name)
#     last_name.append(a)
#
# for j in range(len(first_name)):
#     if j == len(first_name)-1:
#         print(f"{first_name[j]} {last_name[0]}")
#     else:
#         print(f"{first_name[j]} {last_name[j+1]}")
#

records = []
grades = []
n = int(input("enter the no.:"))
for i in range(n):
    names = input("enter the names:")
    score = float(input("enter the score:"))
    records.append([names,score])
    grades.append(score)
grades.sort(key=float)
b = grades[1]
print(b)
name = []
name.sort()
for names,score in records:
    if score == b:
        name.append(names)


for i in name:
    print(i)


# 5
# Harsh
# 20
# Beria
# 20
# Varun
# 19
# Kakunami
# 19
# Vikas
# 21
