# fruit=["apple","banana","cherry"]
# x,y,z=fruit
# print(x)
# print(y)
# print(z)
#
# x="Python"
# y="is"
# z="awesome"
# print(x+y+z)
#
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
#
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

a = int(input("Enter a initial number: "))
b = int(input("Enter a Final number: "))


for i in range(a,b):
    if i%2==0:
        print(i)
    else:
        continue