"""d1={"Rohan":"paani","Ram":"Sitafal","Rita":{"B":"fish","L":"roti"}}
d1["Dharm"]="golgappe"
print(d1)
#del d1["Dharm"]
print(d1["Rohan"])
d2 = d1.copy()

del d2["Dharm"]
print(d1)
print(d2)
#print(d1["Rohan"])
d2.update({"Neera":"pizza"})
print(d2)
print(d2.items())
d1 = {"annoyed":"irritated","relaxed":"calm","happy":"cheerful"}
print("welcome to the dictionary")
spl1 = input()
print("meaning is",d1[spl1])"""

# d={"45*3":"555","56+9":"77","56/6":"4"}
# while(1):
#     print("enter operator")
#     op = input()
#     print("enter first no.")
#     n1 = input()
#     print("enter 2nd no.")
#     n2 = input()
#     nf = n1 + op + n2
#     if nf == "45*3":
#         print("555")
#     elif nf == "56+9":
#         print("77")
#     elif nf == "56/6":
#         print("4")
#     elif op == "+":
#         print(int(n1) + int(n2))
#     elif op == "-":
#         print(int(n1) - int(n2))
#     elif op == "*":
#         print(int(n1) * int(n2))
#     elif op == "/":
#         print(int(n1) / int(n2))
#     else:
#         print("unexpected operator")
#         continue


# s = {1,2,3,4}
# print(type(s))
# s1= s.union({1,2,3,3,4,5,7})
# s3= set([8,9,19])
# print(s1.union(s3))
# list = [1,2,3,4,7,6,7,8]
# l = list[2]
# print(l+2)
# list1 = [["harry",2],["jarry",4]]
# for items,drinks in list1:
#     print(items,drinks)
# d = dict(list1)
# for items,drinks in d.items():
#     if drinks<3:
#         print(items,drinks)
# l1 = [['manji'],"jarvis",23,56,4,2]
# for items in l1:
#     if str(items).isnumeric() and items>6:
#         print(items)
d = {"harry": "2","jarry":"4"}
print(d.get("harry"))