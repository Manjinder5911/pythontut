"""d = {"45*3":"555","56+9":"77","56/6":"4"}
print("welcome to the calculator")
op = input("enter the operator : ")
a = input("enter first no. : ")
b = input("enter 2nd no. : ")
n = a + op + b
if n == "45*3" or n == "56+9" or n == "56/6":
    print(d[n])
elif op == "+":
    print(int(a)+int(b))
elif op == "-":
    print(int(a)-int(b))
elif op == "*":
    print(int(a)*int(b))
elif op == "/":
    print(int(a)/int(b))
else:
    print("unexpected operator")


while(1):
    s = input("enter your no.: ")
    if int(s)<101:

        continue
    if int(s) > 100:
        print("congo")
        break"""

n = 9
print("welcome to the guessing game")
print("total no. of guess", n)
print("hint : the no. is two digit and a multiple of 4 and the sum of two digits is < 10  ")
while 1:
    s = input("enter your guess no.: ")
    if int(s) > 32:
        print("your no. is greater")
    elif int(s) < 32:
        print("your no. is smaller")
    if n < 10:
        n = n-1
        print("no. of guess left" , n)
    if n == 0:
        print("game over")
        break

    if int(s) == 32:
        print("your guess is right")
        print("no of guess you took" , 9-n)
        break




