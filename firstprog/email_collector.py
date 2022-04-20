import re
# mystr = " manji@gmail.com and  manjit@gmail.com and 23 and sdjk, msnj_sm9@alliance.edu.in"
# patt = re.compile(r'[\w\.-]+@[\w\.-]+')
# matches = patt.findall(mystr)
# for match in matches:
#     print(match)

s = "hi I am doing CDCDC cdcdc"
d = "cdc"

score = 0
for i in range(0,len(s)):
    a = i + len(d)
    if s[i] == d[0] and a <= len(s):
        if s[i:i+len(d)] == d:
            score += 1

print(score)







# FAKE MULTIPLICATION TABLE
# rohan das fake table
# import random
# def rohanmutiplication(user_input):
#     rand = random.randint(1,9)
#     fake_output = []
#     for i in range(1,11):
#         if i == rand:
#             correct_output = user_input*i
#             wrong_output = random.randint(correct_output-2,correct_output+2)
#             fake_output.append(wrong_output)
#         else:
#             fake_output.append(user_input*i)
#     return fake_output
#
# # CORRECT TABLE
# def iscorrect(fake_result,number):
#     for i in range(1,11):
#         real_output.append(number*i)
#
#     for j in range(0,10):
#         if real_output[j] != fake_result[j]:
#             return f"multiplication is wrong at index of {j} i.e, {fake_result[j]}\nfake table of rohan is {fake_result}"
#
# if __name__ == '__main__':
#     user_input = int(input("Enter the number:\n"))
#     fake_result = rohanmutiplication(user_input)
#     real_output = []
#     print(iscorrect(fake_result,user_input))
#     print(f"correct table is {real_output}")

