# def myfun(things):
#     for x in things:
#         print(x)
#
#
# food = ['苹果', '香蕉', "李子"]
# myfun(food)
# def tri_recursion(k):
#   if(k>0):
#     result = k+tri_recursion(k-1)
#     print(result)
#   else:
#     result = 0
#   return result
#
# print("\n\nRecursion Example Results")
# tri_recursion(6)

# x = lambda a, b, c: a * b + c
# print(x(5, 2, 1))

# def mul(n):
#     return lambda a: a * n
#
#
# Mymul = mul(3)
# print(Mymul(11))
#
# class Person:
#     def __init__(self, fname, lname):
#         self.firstname = fname
#         self.lastname = lname
#
#     def printname(self):
#         print(self.firstname, self.lastname)
#
#
# class Student(Person):
#
#     def __init__(self, fname, lname, year):
#         super().__init__(fname, lname)
#         self.graduationyear = year
#
#     def welcome(self) -> object:
#         print("Welcome", self.firstname, self.lastname, "to the class of year ", self.graduationyear)
#
#
# x = Student("Elon", "Musk", 2019)
# x.welcome()
# print("Enter your name:")
# x = input()
# print("Hello ", x)

# price = 20
# txt = "The price is {} dollars"
# print(txt.format(price))
#文件写入
# f = open("test.txt","w")
# f.write(" Today is 8/3/2022")
# f.close()
#
# f = open("test.txt","r")
# print(f.read())

# 文件删除
import  os
if os.path.exists("test.txt"):
    print("准备删除文件")
    try:
        os.remove("test.txt")
        print("文件成功删除")
    except:
        print("文件删除失败")
else:
    print("文件不存在，请重试")
