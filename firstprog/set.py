"""l = [2,3,56,57,8,9]
ms = set(l)
print(ms)
print(type(ms))
ms.add(1)
print(ms)
s = set()
s.add(1)
s.add(4)
s2= s.union({1,2,3})
print(s2)
s3= set([2,3,5,6])
s4=s.union(s3)
print(s4, s)
"""

"""print("enter your age")
var2=int(input())
if var2>18:
    print("you can drive")
elif var2==var1:
    print("we are unable to decide\nkindly visit for physical checkup")
else:
    print("you cannot drive")
l1 = ["bread","cake","egg","sandwich"]"""
# r = 1
# for i in l1:
#     if r%2 is 0:
#         print(i)
#     r +=1
# for i,item in enumerate(l1):
#     if i%2 == 0:
#         print(item)
# def function(waht):
#     return(f"what is this {waht}")
#
# print(function("kukkad"))
#
# if __name__ == '__main__':
#     print("ki kar rahe ho bhai")
# lis = ["rna","pratap","jinder"]
# a = " , ".join(lis)
# print(f"{a} ,other superstars ")
# MAP
# lis = [2 ,3 ,44,5 , 32]
# s = list(map(lambda a:a*a*a,lis))
# print(s)
# def cube(a):
#     return a*a*a
# def vakhra(a):
#     return a%2
# lis = [cube,vakhra]
# for i in range(9):
#     val = list(map(lambda x:x(i),lis))
#     print(val)
# FILTER
# lis = [1,2,3,4,5,6,7,8,8,10]
# def func(a):
#     return a > 4
# v = list(filter(func,lis))
# print(v)
# from functools import reduce
#
# lis = [1,2,4,5]
# v = reduce(lambda x,y: x+y,lis)
# print(v)d
# import socket
# hostname = socket.gethostname()
# IPAddr = socket.gethostbyname(hostname)
# print(IPAddr)
# def func(num):
#     if num == 0:
#         return print
#     if num == 1:
#         return int
#
# print(func(0))
# def exe(func):
#     func(9+8)
# exe(print)
# def dec(func):
#     def exe():
#         print("hii")
#         func()
#         print("haha")
#     return exe
# @dec
# def why():
#     print("who is this")
# why()


# def sec(func):
#     def exe(a,b):
#         if a < b:
#             a,b = b,a
#         return func(a,b)
#     return exe
# @sec
# def div(a,b):
#     print(a/b)
# div(3,9)
# class Employee:
#     no_of_leaves = 8
#     pass
#
#     def __init__(self,name,salary):
#         self.name = name
#         self.salary = salary
#
#     def func(self):
#         return f"my name is {self.name}. salary is {self.salary}"
#
#     @classmethod
#     def changeleaves(cls,newleaves):
#         cls.no_of_leaves = newleaves
#
#     @classmethod
#     def dashfunc(cls,string):
#         return cls(*string.split("-"))
#
#     @staticmethod
#     def printgood(string):
#         print("this is good " + string)
#
#     def __repr__(self):
#         return f"Employee({self.name},{self.salary})"
#
#     def __str__(self):
#         return f"name is {self.name},salary is {self.salary}"
#
# harry = Employee("harry",2839)
# rohan = Employee.dashfunc("rohan-2389")
#
# class A :
#     var1 = "its 234"
#     def __init__(self):
#         self.var1 = " its 46"
#         self.var2 = "893"
# class B(A):
#     var1 = "its 879"
#     def __init__(self):
#
#         self.var1 = "its 89"
#
# a = A()
# b = B()
# from abc import ABC,abstractmethod
# class Shape(ABC):
#     @abstractmethod
#     def printarea(self):
#         return 0
#
# class Rectangle(Shape):
#     var1 = "ja bhjja"
#     def printarea(self):
#         return f"{self.var1  + self.var1}"
# harry = Rectangle()
# print(harry.printarea())
# class Employee:
#     # i dont know
#     def __init__(self,fname,lname):
#         self.fname = fname
#         self.lname = lname
#         # self.email = f"{self.fname}{self.lname}@gmail.com"
#
#     def function(self):
#         return f"name is {self.fname} {self.lname}"
#
#     @property
#     def email(self):
#         if self.lname == None or self.fname == None:
#             return "enter valid email"
#         return f"{self.fname}.{self.lname}@gmail.com"
#
#     @email.setter
#     def email(self,string):
#         name = string.split("@")[0]
#         self.fname = name.split(".")[0]
#         self.lname = name.split(".")[1]
#
#     @email.deleter
#     def email(self):
#         self.fname = None
#         self.lname = None
#
# rohan_sekhon = Employee("rohan","sekhon")
# # all i am writing is not visible
# # import inspect
# print(inspect.getsource(Employee))\
# def gener(n):
#     for i in range(n):
#         yield i
#
# print(gener(23))
# import turtle
# t = turtle.Turtle()
# s = turtle.Screen()
# s.bgcolor('black')
# t.pencolor('red')
# t.speed(0)
# for i in range(150):
#     t.circle(190-1,90)
#     t.lt(98)
#     t.circle(190-1,90)
#     t.dlt(18)
# import requests
# r = requests.get("https://api.github.com/users/Manjinder5911")
# print(r.content)
import pickle
cars = ["bmw","audi","maruti suzuki"]
a = pickle.dumps(cars)
print(pickle.loads(a))