# fruit=["apple","banana","cherry"]
# x,y,z=fruit
# print(x)
# print(y)
# print(z)

# x="Python"
# y="is"
# z="awesome"
# print(x+y+z)

# x="Awesome"
# def myfunc():
#     global x
#     x="fantastic"
#     print("Python is" , x)
# myfunc()
# print("Python is" , x)
# x=5
# y=10
# z=x+y
# print("The Sum of ", x ,"and", y, "is: ", z)
# greeting = "Hello, Lew!"
# print('1:',greeting)
# print('2:',len(greeting))
# print('3:',greeting[0])
# print('4:',greeting[-1])
# greeting = greeting.replace("Lew","Class")
# print('5:',greeting)
# string1 = "Hello"
# string2 = "World"
# print("1:",string1, string2)
# cost = float(35.38)
# print("Bar tab = £%f" %cost)
# for i in range(0,6):
#     for a in range(6,i,-1):
#            print("*\t", end="")
#     print()
# test_string = "Dogs are better tha Cats"
# print("Last elements: ", test_string[4:])
# print("Second to last elements: ", test_string[:4])

# print(test_string[5:10])
# prices = {"Eggs": 2.30,
#           "Steak": 13.50,
#           "Bacon": 2.30,
#           "Beer": 14.95}
# print("1:",prices)
# print("2:",type(prices))
# print("The price of Bacon is:", prices["Bacon"])
# fname="RUGABA"
# def myname():
#     lname = "Gilbert"
#     print("My name is :",fname,lname)
# myname()

# a= "Hello, World!"
# print(len(a))


# for x in "banana":
#  print(len(x))

# for a in range(1,21):
#  print(a)

# txt="The best things in life is free!"
# if "frees" in txt:
#     print("Yes , 'free' is present")
# else:
#     print("Word not found")

# for a in range(0,21):
#     if a%2==0 :
#         print(a)
#     else:
#         print()

# for a in range(1,20,2):
#     print(a)

# a=3
# b=5

# if a%2==0 and b%2==0 :
#     print(a+b)
# else:
#     print(a*b)

# a="Welcome in IT Year 3"

# print(a.split())

# def myfunction():
#     return true

# if myfunction():
#     print("YES!")
# else:
#     print("NO!")

# x = 200
# y = 2.5
# print(isinstance(y,int))

# print(10>9)
# list1 = ["apple","Banana","cherry"]
# list2 = [1,5,7,9,3]
# list3 = [True,False,False]

# thislist = ["apple","banana","cherry","orange","kiwi","mango"]
# thislist[1:3]=["blackcurrant","watermelon"]
# print(thislist)

# a = input("Enter a number: ")
# print("You entered: ",a)

# a = int(input("Enter a initial number: "))
# b = int(input("Enter a Final number: "))


# for i in range(a,b):
#     if i%2==0:
#         print(i)
#     else:
#         continue

# thislist = ["apple","banana","cherry"]
# thislist[1:3]=["watermelon"]
# print(thislist)

# thislist = ["apple","banana","cherry"]
# thislist.insert(2,"watermelon")
# print(thislist)

# thislist = ["apple","banana","cherry"]
# thislist.append("Orange")
# print(thislist)

# thislist = ["apple","banana","cherry"]
# tropical = ("mango","pineapple","papaya")
# thislist.extend(tropical)
# print(thislist)

# thislist = ["apple","banana","cherry"]
# thislist.remove("banana")
# print(thislist)

# thislist = ["apple","banana","cherry"]
# thislist.pop(1)
# print(thislist)

# thislist = ["apple","banana","cherry"]
# del thislist[0]
# print(thislist)

# thislist = ["apple","banana","cherry"]
# thislist.clear()
# print(thislist)

# thislist = ["apple","banana","cherry"]

# for x in thislist:
#     print(x)

# thislist = ["apple","banana","cherry"]

# for x in range(len(thislist)):
#     print(thislist[x])

# thislist = ["apple","banana","cherry"]
# i = 0

# while i<len(thislist):
#     print(thislist[i])
#     i = i+1

# thislist = ["apple","banana","cherry"]
# [print(x) for x in thislist]

# fruit = ["apple","banana","cherry","kiwi","mango"]
# newlist = []

# for x in fruit:
#     if "i" in x:
#         newlist.append(x)
# print(newlist)

# thislist = ["apple","banana","cherry","kiwi","mango"]
# thislist.sort()
# print(thislist)

# def myfunc(n):
#     return abs(n-50)
# thislist = [100,50,65,82,23]
# thislist.sort(key = myfunc)
# print(thislist)

# thislist = ["apple","banana","cherry","kiwi","mango"]
# thislist.reverse()
# print(thislist)

# list1  = ["a","b","c"]
# list2 = [1,2,3]

# for x in list2:
#     list1.append(x)
# print(list1)

# fruit = ("apple","banana","cherry","strawberry","raspberry")

# (green,yellow,*red) = fruit

# print(green)
# print(yellow)
# print(red)

# thisset = {"apple","banana","cherry"}
# print(thisset)

# import datetime

# x = datetime.datetime(2024, 2, 2)
# print(x.strftime("%c"))

# x = min(5,10,25)
# y = max(5,10,25)

# print(x)
# print(y)

# x = abs(-7.25)
# print(x)

# x = pow(4,3)
# print(x)

# import math

# x = math.sqrt(64)
# print(x)

# x = math.pi

# print(x)

# number = [1,2,3]
# number.append(5)
# print(number)

# for i in range(1,10):
#     if i==3:
#         break
#     print(i)
# print()
# for i in range(1,10):
#     if i==3:
#         continue
#     print(i)

# school_nigth = True
# if school_nigth == True:
#     print("No Beer")
# else:
#     print("You may have a Beer")

# school_nigth = False
# if school_nigth == True:
#     print("No Beer")
# else:
#     print("You may have a Beer")

# Lew_is_tired = False
# Lew_is_hungry = True
# if Lew_is_tired is True:
#     print("Lew has to teach")
# elif Lew_is_hungry is True:
#     print("No food for Lew")
# else:
#     print("Go on, have a biscuit")

def multiply_function(a,b):
    result = a*b
    result2 = result * result
    return result, result2

number_list = [1, 2, 3]
multiplier_list = [2, 4]
for n in number_list:
    print("__________________________________________")
    for m in multiplier_list:
        current_answer, current_answer2 = multiply_function(n, m)
        print("The answer to %d * %d is : " %(n, m), current_answer)
        print("The result of this squared is : " ,current_answer2)