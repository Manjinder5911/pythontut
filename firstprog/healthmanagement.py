def getdate():
    import datetime
    return datetime.datetime.now()


a = getdate()
b = int(input("enter 1 for lock and 2 for retrieve :\n"))
c = int(input("enter 1 for Harry, 2 for Rohan and 3 for Hammad :\n"))
d = int(input("enter 1 for exercise and 2 for food :\n"))
if b == 1:
    if c == 1:
        while d == 2:
            f = open("Harryfood.py", "a")
            e = input("enter your food : ")
            f.write(str([str(a)]) + " " + e + "\n")
            print("you wrote successfully")
            g = int(input("enter 1 to write again and 2 to stop :"))
            if g == 1:
                continue
            else:
                break
        while d == 1:
            f2 = open("Harryexer.py", "a")
            h = input("enter your exercise : ")
            f2.write(str([str(a)]) + " " + h + "\n")
            print("you wrote( successfully")
            j = int(input("enter 1 to write again and 2 to stop :"))
            if j == 1:
                continue
            else:
                break
    if c == 2:
        while d == 2:
            f3 = open("Rohanfood.py", "a")
            i = input("enter your exercise : ")
            f3.write(str([str(a)]) + " " + i + "\n")
            print("you wrote successfully")
            l = int(input("enter 1 to write again and 2 to stop :"))
            if l == 1:
                continue
            else:
                break

        while d == 1:
            f4 = open("Rohanexer.py", "a")
            m = input("enter your exercise : ")
            f4.write(str([str(a)]) + " " + m + "\n")
            print("you wrote successfully")
            n = int(input("enter 1 to write again and 2 to stop :"))
            if n == 1:
                continue
            else:
                break

    if c == 3:
        while d == 2:
            f5 = open("Hammadfood.py","a")
            o = input("enter your food : ")
            f5.write(str([str(a)]) + " " + o + "\n")
            print("you wrote successfully")
            p = int(input("enter 1 to write again and 2 to stop :"))
            if p == 1:
                continue
            else:
                break

        while d == 1:
            f6 = open("Hammadexer.py", "a")
            q = input("enter your exercise : ")
            f6.write(str([str(a)]) + " " + q + "\n")
            print("you wrote successfully")
            r = int(input("enter 1 to write again and 2 to stop :"))
            if r == 1:
                continue
            else:
                break

else:
    if c == 1:
        if d == 2:
            f7 = open("Harryfood.py", "r")
            for line in f7:
                print(line, end="")
            f7.close()
        else:
            f8 = open("Harryexer.py", "r")
            for lines in f8:
                print(lines, end="")
            f8.close()

    if c == 2:
        if d == 2:
            f9 = open("Rohanfood.py", "r")
            for lines in f9:
                print(lines, end="")
            f9.close()
        else:
            f10 = open("Rohanexer.py", "r")
            for lines in f10:
                print(lines, end="")
            f10.close()

    else:
        if d == 2:
            f11 = open("Hammadfood.py", "r")
            for lines in f11:
                print(lines, end="")
            f11.close()
        else:
            f12 = open("Hammadexer.py", "r")
            for lines in f12:
                print(lines, end="")
            f12.close()
