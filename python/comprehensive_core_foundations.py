""" DAY 1 TO DAY 30 
Language Python
100 Day series (Code with Harry)"""
# Escape Sequence Characters and print() statement:
print("My name is \"Ahmad\"\\age = \'21\' \nfriend_name = \"Osama\",\t We study in BS-CS")
print("Ahmad","21","Osama","20:", sep = "~", end = "\nWe are friends")
# Variables, Data types
# It's type
# Complex number:
name = "Ahmad"
age = 21
hight = 5.9
print(name)
print(type(name))
print(age)
print(type(age))
print(hight)
print(type(hight))
num = complex(3,4)
print(num)
print(type(num))
data = {"name" : "Ahmad", "age" : 21}
print(data)
print(type(data))
# Operators:
# Arithmetic operator:
num1  = 10
num2 = 2
print("The value of num1 + num2 is =",num1+num2)
print("The value of num1 - num2 is =",num1-num2)
print("The value of num1 * num2 is =",num1*num2)
print("The value of num1 / num2 is =",num1/num2)
print("The value of num1 // num2 is =",num1//num2)
print("The value of num1 ** num2 is =",num1**num2)
print("The value of num1 % num2 is =",num1%num2)
# Relational operators:
a = 2
b = 3
print(a==b, b!=a, a<b, b>a, a>=b, b<=a)
# Assignment operator:
a = 3
b = 4
a += 2
print(a)
b -= 7
print(b)
a *= 2
b /= 3
print(a)
print(b)
a %= 6
b //= 7
print(a, b)
a **= 2
print(a)
# Logical operator:
a = True
b = False
print(a == b and b != a)
print(a >=b or b<a)
print(not(a))
print(not(b))
# Bitwise operator:
print(7&3)
print(7|3)
print(7^3)
print(~7,~3)
print(7<<3 ,7>>3)
# Identity operator:
a = "Ahmad"
b = a
print(a is not b)
print(b is a)
print(a == b)
b = "Osama"
print(a is not b)
a = [1, 2, 3]
b = [1, 2, 3]
print(a is not b)
print(a is b)
b = a
print( a == b)
print(a is b)
a = ("Ahmad", 21)
b = (20 , "Osama")
print(a is not b)
print(a is b)
print(a == b)
b = a
print(a is not b)
# Membership operator:
a = ["Ahmad", "Osama", "Python"]
print("Ahmad" in a)
print("Python" not in a)
print(21 not in a)
a = ("Ahmad", 21)
print(21 in a)
print("Ahmad" not in a)
# Type casting:
# Implicit typecasting
a = 2.5
b = 5
sol = a + b
print(sol)
print(type(sol))
# Explicit typecasting
a = 2.5
b = 5
a = int(a)
sol = a + b
print(sol)
print(type(sol))
a = "10"
a = int(a)
sol = a - b
print(sol)
print(type(sol))
# Common Functions:
print(float(10))
print(type(float(10)))
print(repr(str(21)))
print(type(str(21)))
print(int(10.0))
print(type(int(10.0)))
print(list("Ahmad"))
print(type(list("Ahmad")))
print(bool(1))
print(bool(0))
print(bool(""))
print(bool("Python"))
print(type(bool("Python")), type(bool("")), type(bool(1)), type(bool(0)))
print(tuple(["Ahmad" , "Osama", 21]))
print(type(tuple(["Ahmad" , "Osama", 21])))
print(set([1,2,3]))
print(type(set([1,2,3])))
# Typecasting with input():
num1 = int(float(input("Enter a num1:")))
num2 = int(float(input("Enter a num2:")))
print("The value of num1 + num2 is =",num1+num2)
print("The value of num1 - num2 is =",num1-num2)
print("The value of num1 * num2 is =",num1*num2)
print("The value of num1 / num2 is =",num1/num2)
print("The value of num1 // num2 is =",num1//num2)
print("The value of num1 ** num2 is =",num1**num2)
print("The value of num1 % num2 is =",num1%num2)
# Strings:
name = "Ahmad"
print(name)
print(type(name))
print("Osama")
print(type("Osama"))
# Multi line strings:
Data = """My name is \"Ahmad\".I'm \'21\' years old.Study \"BS-CS\""""
print(Data)
print(type(Data))
print('''My name is \"Osama\".I'm \'20\' years old.''')
print(type('''My name is \"Osama\".I'm \'20\' years old.'''))
# String indexing:
name = "Ahmad"
print(name[0])
print(name[4])
print(name[-4])
data = ["Ahmad", "Osama", "AbuBakar"]
print(data[0])
print(data[-1])
data = ("Ahmad", 21, 20, "Osama")
print(data[2])
print(data[-1])
# Loop through string:
name = "Ahamd"
for ch in name:
    print(ch)
data = ["Ahmad", "Osama"]
for item in data:
    print(item)
data = ("Ahmad", 21)
for item in data:
    print(item)
# String slicing:
data = "Ahamd"
print(data[1:])
print(data[:4])
print(data[:])
print(data[0:3])
print(data[0:4:2])
print(data[-4:-1])
print(len(data))
print(data[2:len(data)])
print(data[len(data)-4:len(data)-1])
# String methods:
name = "Ahmad"
print(name.upper())
print(name.lower())
print(name.isupper())
print(name.islower())
print(name.swapcase())
print(name.count("a"))
print(name.index("m"))
print(name.find("d"))
name = "   Ahmad  "
print(name.strip())
name = "!!!Ahamd!!!"
print(name.lstrip("!"))
print(name.rstrip("!"))
name = "Ahmad"
print(name.replace("Ahmad","Osama"))
data = "I like Java"
print(data.replace("Java","Python"))
print(name.replace("d","6"))
data = "Ahamd, Osama ,AbuBakar"
print(data.split())
name = "ahmad"
print(name.capitalize())
print(name.center(10))
print(name.center(11,"*"))
name = "Ahmad!"
print(name.endswith("!"))
print(name.startswith("&"))
data = "Ahmad21  20"
print(data.isalnum())
data = "Ahamd21"
print(data.isalnum())
data = "Ahmad"
print(data.isalnum())
data = "212123"
print(data.isalnum())
print(data.isalpha())
name = "Ahmad"
print(name.isalpha())
print(name.isprintable())
print(name.isspace())
print(name.istitle())
print(name.title())
# if-else statements:
name = input("Enter a name:")
if name == "Ahmad":
    print("Hey! Ahmad")
num1 = int(float(input("Enter a num:")))
operator = input("Choose operator(+, -, *, /, %, //, **):")
num2 = int(float(input("Enter a num:")))
if operator == "+":
    print(num1 + num2)
elif operator == "-":
    print(num1 - num2)
elif operator == "*":
    print(num1 * num2)
elif operator == "/":
    print(num1 / num2)
elif operator == "%":
    print(num1 %num2)
elif operator == "//":
    print(num1 // num2)
else:
    print(num1 ** num2)
num = int(float(input("Enter a num:")))
if num % 2 == 0:
    print(num,"is Even")
else:
    print(num,"is Odd")
car_name = input("Enter a car_name:")
model = int(input("Enter a model:"))
if car_name == "BMW m5":
    if model == 2005:
        print("Congratulation!You are now owner of m5")
    else:
        print("Please!Enter a model corrrect that you ordered")
elif model == 2005:
    print("Please!Enter correct car_name")
else:
    print("To own Car.Please!Enter a correct Data")
name = input("Enter a name:")
password = int(input("Enter a password:"))
if name != "Ahmad":
    if password != 181314:
        print("Error!Enter a correct Data")
    else:
        print("Error!Enter a correct name")
elif name == "Ahmad":
    if password == 181314:
        print("Login Successfully")
    else:
        print("Error!Enter a correct password")
name = input("Enter a name:")
password = int(input("Enter a password:"))
if name != "Ahmad" and password != 181314:
    print("Incorrect Data")
elif name == "Ahmad":
    if password == 181314:
        print("Login Successfully")
    else:
        print("Error!Incorrect password")
else:
    print("Error!Incorrect name")
marks = int(input("Enter obtained marks:"))
if marks >=50 and marks <60:
    print("Grade D")
elif marks >=60 and marks <70:
    print("Grade C")
elif marks >=70 and marks <80:
    print("Grade B")
elif marks >=80 and marks <90:
    print("Grade A")
else:
    print("Grade A+")
marks = int(input("Enter marks:"))
if marks >=90:
    if marks >=90 and marks <100:
        print("Grade A+")
elif marks >=70:
    if marks >=80 and marks <90:
        print("Grade A")  
    else:
        print("Grade B")
elif marks >=50:
    if marks >=60 and marks <70:
        print("Grade C")
    else:
        print("Grade D")
else:
    print("Grade F")
marks = int(input("Enter marks:"))
if marks >=90 and marks <=100:
    print("Grade A+")
elif marks >=80 and marks <90:
    print("Grade A")  
elif marks >=70 and marks <80:
    print("Grade B")
elif marks >=60 and marks <70:
    print("Grade C")
else:
    if marks >=50 and marks <60:
        print("Grade D")
    else:
        print("Grade F")
user_name = input("Enter a user_name:")
password = int(input("Enter a password:"))
if user_name == "Ahmad" and password ==181314:
    print("Login Successfully")
elif user_name != "Ahmad":
    if password != 181314:
        print("Error!Incorrect Data")
    else:
        print("Error!Incorrect name")
else:
    print("Error!Incorrect password")
# Modules:
# Built-in modules:
import math
result = math.sqrt(10)
print(result)
result = math.ceil(4.5)
print(result)
print(math.floor(4.5))
print(math.pi)
import operator
result = operator.add(4,5)
print("The addition of 4,5 is =",result)
result = operator.sub(5,4)
print("The subtraction of 5,4 is =",result)
result = operator.mul(3,6)
print("The multiplication of 3,6 is =",result)
print(operator.truediv(5,10))
print(operator.floordiv(5,10))
print(operator.mod(5,10))
print(operator.pow(3,4))
import random
result = random.randint(1,5)
print(result)
data = ["Ahmad", "Osama", "Hassan", "AbuBakar"]
print("Today lucky name is:",random.choice(data))
import os
result = os.rmdir("folder1")
import os
print(os.rename("folder1","folder"))
import os
result = os.system('rmdir /s /q "folder"')
import os 
print(os.getcwd())
import time
current_time = time.strftime("%H:%M:%S")
print(current_time)
hour = int(time.strftime("%H"))
if hour >=0 and hour <8:
    print("Good Morning")
elif hour >=8 and hour <12:
    print("Good Afternoon")
elif hour >=12 and hour <21:
    print("Good Evening")
else:
    print("Good Night")
import datetime
hour = datetime.datetime.now().hour
name = "Ahmad"
if hour >=0 and hour <8:
    print("Good morning",name)
elif hour >=8 and hour <18:
    print("Good Afternoon",name)
elif hour >=18 and hour <21:
    print("Good Evening,name")
else:
    print("Good Night",name)
import time
print(time.strftime("%H:%M:%S"))
# Match case:
name = "Ahmad"
match name:
    case "AbuBakar":
        print("Hey!AbuBakar")
    case "Osama":
        print("Hey!Osama")
    case _ :
        print("Hey!Ahmad")
num = 2
match num:
    case 1:
        print("You got 90 percent")
    case 2:
        print("You got 80 percent")
    case _ :
        print("You got 70 percent")
data = "Osama"
match data:
    case "Ahmad" | "Osama":
        print("WE ARE FRIENDS")
    case _ :
        print("WE ARE NOT FRIENDS")
day = "Monday"
match day:
    case "Saturday" | "Sunday":
        print("Weekend")
    case _ :
        print("Working Day")
points = (1,9)
match points:
    case (1,y):
        print("Y axis")
    case (x,1):
        print("X axis")
    case _ :
        print("Others")
data = ["Ahmad", "Osama", 20]
match data:
    case [_, _, 20]:
        print("My Friend age is: 20")
    case _ :
        print("Unknown person")
data = {"name": "Ahmad", "friend_name": "Osama"}
match data:
    case {"name": name, "friend_name": friend_name}:
        print(name, friend_name)
    case _ :
        print("No data match")
marks = 89
match marks:
    case x if x >= 80:
        print("Successfully!Passed Exam")
    case _ :

        print("Failed!Try next time")
data = {"Ahmad", 21, 20, "Osama"}
match data:
    case _ if "Ahmad" in data:
        print(data)
    case _ :
        print("Incorrect data")
data = ("Turkey", "U.S", "U.K", "Pakistan")
match data:
    case x if "Pakistan" in data:
        print(data)
    case _ :
        print("Invalid Data")
data = ["Mango", "Banana", "Apple", "Orange"]
match data:
    case _ if "Mango" in data:
        print("Mango is include in data:",data)
    case _ :
        print("Invalid data")
# Loops:
# For loop:
name = "Ahmad"
for i in name:
    print(i)
data = ("Ahmad", "Osama", 21, 20)
for item in data:
    print(item)
data = [2005, 2006, 2007, 2008]
for years in data:
    print(years)
nums = {21, 22, 23, 24, 25, 26}
for num in nums:
    print(num)
data = {"name": "Ahmad", "friend_name": "Osama", "ages": 21}
for key in data:
    print(key)
for value in data.values():
    print(value)
data = {"name": "Ahmad", "friend_name": "Osama", "ages": 21}
for key, value in data.items():
    print(key, ":", value)
for i in range(1,10):
    print(i)
for i in range(1,10,3):
    print(i)
for i in range(10,0,-1):
    print(i)
for i in range(1,5):
    if i==3:
        print("3 is Found")
    print(i)  
for i in range(1,10):
    if i %2 == 0:
        print("Even",i)
    else:
        print("Odd",i)
data = [44, 55, 66, 77, 88 ,99]
for i in data:
    if i>=50 and i<60:
        print("Grade D",i)
    elif i>=60 and i<70:
        print("Grade C",i)
    elif i>=70 and i<80:
        print("Grade B",i)
    elif i>=80 and i<90:
        print("Grade A",i)
    elif i>=90 and i<100:
        print("Grade A+",i)
    else:
        print("Grade F",i)
for i in range(3):
    for j in range(2):
        print(i,j)
for i in range(1,10):
    if i == 4:
        continue
    else:
        if i == 8:
            break
    print(i)
# While loop:
num = int(input("Enter a num:"))
while num<10:
    print(num)
    num+=1
num = int(input("Enter a num:"))
while num>2:
    print(num)
    num-=1
name = input("Enter a name:")
while name != "Ahmad":
    print("Invalid")
    name = input("Enter a name:")
print("Login Successfully")
password = int(input("Enter a password:"))
while password != 181314:
    print("Invalid")
    password = int(input("Enter a password:"))
else:
    print("Login Successfully")
nums = 10
while nums>0:
    nums-=1
    if nums ==5:
        continue
    if nums == 2:
        break
    print(nums)
for i in range(1,8):
    if i ==4:
        continue
        print(i)
    else:
        if i ==6:
            break
    print(i) 
num = 10
while num > 0:
    if num ==6:
       num-=1
       continue
       print(num) 
    num-=1
    if num == 3:
       break
       num-=1
    print(num)
# Functions:
# User-defined:
# Also use loops:
# Function arguments:
def name():
    print("Ahmad")
name()
def user_name(name):
    print(name)
user_name("Ahmad")
def square(num):
    return num*num
result =square(2)
print(result)
def add(num1,num2):
    return num1 + num2
num1 = 2
num2 = 3
print(add(num1,num2))
def num():
    for i in range(1,10,2):
        if i == 5:
            continue
            print(i)
        if i == 7 :
            break
        print(i)
num()
def num():
    for i in range(1,10):
        if i %2 == 0:
            print("Even",i)
        else:
            print("Odd",i)
num()
def obtained_marks(marks):
        if 50<= marks <60:
            print("Grade D",marks)
        elif 60<= marks <70:
            print("Grade C",marks)
        elif 70<= marks <80:
            print("Grade B",marks)
        elif 80<= marks <90:
            print("Grade A",marks)
        elif 90<= marks <100:
            print("Grade A+",marks)
        else:
            print("Grade F",marks)
marks = int(input("Enter obtained_marks:"))
obtained_marks(marks)
def num():
    i = 10
    while i>1:
        i -=1
        if i ==5:
            continue
        if i ==3:
            break
        print(i)
    else:
        print("Loop Finished")
num()
def num():
    i =2
    while i <9:
        i +=1
        if i == 5:
            continue
        print(i)
num()
def num():
    i =2
    while i <9:
        i +=1
        if i ==6:
            break
        print(i)
num()
def num():
    i = 12
    while i >2:
        i -=1
        if i ==9:
            continue
        if i ==6:
            break
        print(i)
num()
def data(name = "Ahmad"):
    print("Hey!",name)
data()
data(name = "Osama")
def data(name,age):
    print(name,age)
data("Ahmad",21)
def data(name,age):
    print(name,age)
data(name = "Ahmad",age = 21)
def data(*args):
    print(args)
data(1,2,3)
def data(**kwargs):
    print(kwargs)
data(name = "Ahmad",age = 21)
def data(nums):
    print(nums)
nums = (1,2,3,4,5)
data(nums)
def data(nums):
    print(nums)
nums ={1,2,3}
data(nums)
def data(a,b,c):
    print(a*b*c)
nums = (1,2,3)
data(*nums)
# List:
# Built-in functions:
data = ("Ahmad", "Osama", 21, 20)
print(len(data))
nums = (12,21,3,2,5,7)
print(max(nums))
print(min(nums))
print(sum(nums))
print(sorted(nums))
# List:
# List indexing and slicing and concatentation and built-in functions:
# List methods:
data = ["ahmad", "osama", "abubakar"]
print(data)
nums = [21,22,23,24,25,26,272,28,29]
print(nums[2])
print(nums[-2])
print(nums[:4])
print(nums[1:])
print(nums[:])
print(nums[1:5])
print(nums[-6:-1])
print(len(nums))
print(nums[:len(nums)])
print(nums[len(nums)-6:len(nums)-1])
print(max(nums))
print(min(nums))
print(sum(nums))
print(sorted(nums))
nums1 = [31,32,33,34,35,36,37,38,39]
result = nums +nums1
print(result)
nums = [1,3,5,7,9,2,4,6,8,9]
nums.sort()
print(nums)
result = nums.index(9)
print("Position of 9 is:",result)
result = nums.count(9)
print(result)
nums.clear()
nums = [1,3,5,7,9,2,4,6,8,9]
print(nums)
nums.append(10)
print(nums)
nums.append([11,12])
print(nums)
nums.extend([13,14,15])
print(nums)
nums.remove(9)
print(nums)
removed = nums.pop(4)
print("Removed:",removed)
print("List:",nums)
nums.insert(1,2)
print(nums)
nums = [23,25,24,22,20]
nums.sort()
print(nums)
nums.sort(reverse=True)
print(nums)
nums.reverse()
print(nums)
nums = [20,21,22,23,24,25,26]
print("Copy:",nums)
nums.extend([27,28])
new_copy = nums.copy()
print("New_Copy:",nums)
nums = [1,2,3,4,5]
for i in nums:
    print(i)
for i in range(len(nums)):
    print(nums[i])
i = 0
while i <len(nums):
    print(nums[i])
    i +=1
# Tuple:
# Tuple indexing and slicing and built-in functions:
# Tuple methods:
data = ("Ahmad", 21, "Osama", 20)
print(data)
nums = (1,2,3,4,5,6,7,8,9)
print(nums[3])
print(nums[-5])
print(nums[:])
print(nums[:4])
print(nums[2:])
print(nums[2:6])
print(nums[-5:-2])
print(len(nums))
print(nums[:len(nums)])
print(nums[len(nums)-5:len(nums)-2])
print(max(nums))
print(min(nums))
print(sum(nums))
nums = (2,4,3,6,5,8,7,2)
print(sorted(nums))
print(nums.count(2))
print(nums.index(5))
# List through loop and List comprehension:
data = ["Ahmad", "Osama", "Abubakar"]
for i in data:
    print(i)
for i in range(len(data)):
    print(data[i])
nums = [40,51,62,73,84,95]
for num in range(len(nums)):
    print(nums[num])
for num in nums:
    if num%2 ==0:
        print("Even",num)
    else:
        print("Odd",num)
for num in nums:
    if 50<= num <60:
        print("Grade D",num)
    elif 60<= num <70:
        print("Grade C",num)
    elif 70<= num <80:
        print("Grade B",num)
    elif 80<= num <90:
        print("Grade A",num)
    elif 90<= num <100:
        print("Grade A+",num)
    else:
        print("Grade F",num)
for num in nums:
    if num>40:
        if num %2 == 0:
            if num ==62:
                continue
            if num ==84:
                break
            print("Even",num)
        else:
            print("Odd",num)
nums = [40,51,62,73,84,95]
i = 0
while i<len(nums):
    print(nums[i])
    i +=1
nums = [40,51,62,73,84,95]
i =len(nums)-1
while i>=0:
    if nums[i] == 84:
        i-=1
        continue
    if nums[i] == 51:
        break
    print(nums[i])
    i-=1
marks = [40,51,62,73,84,95]
i =0
while i<len(marks):
    if marks[i] == 62:
        i +=1
        continue 
    if marks[i] == 84:
            break
    if marks[i] >=90:
        print("Grade A+")
    elif marks[i] >=80:
        print("Grade A")
    elif marks[i] >=70:
        print("Grade B")
    elif marks[i] >=60:
        print("Grade C")
    elif marks[i] >=50:
        print("Grade D")
    else:
        print("Grade F")
    print(marks[i])
    i +=1
num = [2,3,4,5,6,7]
i =0
while i<len(num):
    num[i] = num[i]*2
    print(num[i])
    i +=1
i =0
while i<len(num):
    num[i] = num[i]+1
    print(num[i])
    i +=1
i = 0
while i<len(num):
    num[i] = num[i]-2
    print(num[i])
    i+=1
num = [2,3,4,5,6,7]
i =0
while i<len(num):
    num[i] = num[i]/2
    print(num[i])
    i+=1
nums = [1,2,3,4,5,6]
i = 0
while i<len(nums):
    print(nums[i]*2)
    i+=1
nums = [1,2,3,4,5,6]
new_nums = []   
i = 0
while i<len(nums):
    if nums[i]%2 == 0:
        new_nums.append(nums[i])
    i+=1
print("Original:",nums)
print("New_List:",new_nums)
nums = [num for num in range(1,6)]
print(nums)
nums = [ i for i in range(1,9,2)]
print(nums)
nums = [i*2 for i in range(1,7)]
print(nums)
nums = [i+3 for i in range(1,5)]
print(nums)
nums = [i*i for i in range(1,5)]
print(nums)
name = "Ahmad"
names = [i for i in name]
print(names)
name = "Osama"
result = [i for i in name]
print(result)
data = ["Ahmad", "Osama", "AbuBakar"]
new_data = [i for i in data]
print(new_data)
data = [21, 20,22]
new_data = [i for i in data]
print(new_data)
nums = [1,2,3,4,5]
new_nums = [i for i in nums if i%2==0]
print("Even:",new_nums)
new_nums = [i for i in nums if i%2!=0]
print("Odd",new_nums)
new_nums = ["Even" if i%2==0 else "Odd" for i in nums]
print(new_nums)
name = input("Enter a name:")
result = ["Login Successfully" if name == "Ahmad" else "Invalid name" for i in name]
print(result[0])
names = ["ahmad",  "OSAMA", "AbUbAkAr"]
result = [name.upper() for name in names]
print(result)
result = [name.lower() for name in names]
print(result)
result = [name.isupper() for name in names]
print(result)
result = [name.islower() for name in names]
print(result)
result = [name.swapcase() for name in names]
print(result)
result = [name.count("a") for name in names]
print(result)
data = ["Ahmad", "Osama", "AbuBakar"]
result = [i for i in data if len(i)<6]
print(result)
result = [i for i in data if len(i)>5]
print(result)
nums = [55,66,77,88,99]
result = [i for i in nums if i>55 and i<99]
print(result)
day = [input("Enter a day:")]
result = ["Weekend" if i=="Sunday" or i=="Saturday" else "Weekday" for i in day]
print(result[0])
data = [i for i in range(10,1,-1)]
print(data)
def square(num):
    return num*num
num = [1,2,3]
result = [square(num) for num in num]
print(result)
def sum(num,num2):
    return num+num2
num = [2,3,4]
num2 = [2,3,4]
result = [sum(num,num) for num in num]
print(result)
def multiply(num):
    return num*num
nums = [2,3]
result = [multiply(num) for num in nums if num%2==0]
print(result)
data = [i for row in [[1,2],[3,4]] for i in row]
print(data)
result = [i for row in [[2,4],[6,8]] for i in row]
print(result)
data = [i*2 for row in [[1,2],[3,4]] for i in row]
print(data)
data = [i+2 for row in [[2,3],[4,5]] for i in row]
print(data)
nums = [1,2,3,4,5,6,7,8,9]
result = ["Large" if num>5 else "Small" if num<5 else "Equal" for num in nums]
print(result)
nums = [-1, -2, -3, -4, -5]
result = [abs(i) for i in nums]
print(result)
nums = [abs(i) for i in range(5,0,-1)]
print(nums)
nums = [type(i) for i in range(1,5)]
print(nums)
data = ["Ahmad", 21, "Osama", 20]
result = [type(i) for i in data]
print(result)
""" Tuple with loops and conditional statements:
Tuple unpacking, Extended unpacking, Join two tuples, Repeat tuple, Nested tuple:
Access individual values:
Tuple to List:
List to Tuple:
Using List Methods:"""
data = ("Ahmad", 21, "Osama", 20)
for i in data:
    print(i)
for i in range(len(data)):
    print(data[i])
data = (1,2,3,4,5,6)
for i in data:
    if i%2 ==0:
        print("Even:",i)
    else:
        print("Odd:",i)
marks = (49,59,69,79,89,99)
for i in marks:
    if i == 69:
        continue
    if i == 89:
        break
    if 50<= i <60:
        print("Grade D",i)
    elif 60<= i <70:
        print("Grade C",i)
    elif 70<= i <80:
        print("Grade B",i)
    elif 80<= i <90:
        print("Grade A",i)
    elif 90<= i <100:
        print("Grade A+",i)
    else:
        print("Grade F",i)
marks = (49,59,69,79,89,99)
i = 0
while i<len(marks):
    if marks[i] == 69:
        i +=1
        continue
    if marks[i] == 89:
        break
    if 50<= marks[i] <60:
        print("Grade D",marks[i])
    elif 60<= marks[i] <70:
        print("Grade C",marks[i])
    elif 70<= marks[i] <80:
        print("Grade B",marks[i])
    elif 80<= marks[i] <90:
        print("Grade A",marks[i])
    elif 90<= marks[i] <100:
        print("Grade A+",marks[i])
    else:
        print("Grade F",marks[i])
    i +=1
data = ("Ahmad", 21, "Osama", 20)
i =len(data)-1
while i>=0:
    print(data[i])
    i-=1
data = (2,3,4,5)
i =0
while i<len(data):
    if data[i]%2==0:
        print("Even:",data[i])
    else:
        print("Odd:",data[i])
    i+=1
print("Loop Finished")
data = ("Ahmad", 21, "Osama", 20)
print("Ahamd" not in data)
print(22 in data)
data = (21,22,23)
x,y,z = data
print(tuple([x, y, z]))
data = ("Ahmad", "Osama", "Abubakar", "AhmadRaja")
a,b,c,d = data
print(a)
print(b)
print(c)
print(d)
print(a, b, c, d)
print(tuple([a, b, c, d]))
s,*f,t = data
print(s)
print(tuple([f,t]))
data = ("Ahmad", 21)
data1 =("Osama", 20)
result = data + data1
print(result)
data = (2, 4, 6)
print(data*2)
data = ((1,2),(3,4))
print(data[0])
print(data[1])
print(data[0][0])
print(data[0][1])
print(data[1][0])
print(data[1][1])
for i in data:
    print(i)
data = ("Ahmad", "Osama", 21, 20)
new_list = list(data)
print(new_list)
data = (21, 22, 23, 24, 25)
new_list = list(data)
print(new_list)
print(list(data))
data = ["Ahamd", "Osama", 21, 20]
new_tuple = tuple(data)
print(new_tuple)
data = ["apple", "banana", "orange"]
print(tuple(data))
data = (21, 22, 23)
new_data = list(data)
new_data.extend([24, 25])
data = tuple(new_data)
print(data)
data = ("Ahmad", "AbuBakar", "Osama", "AhamdRaja")
new_data =list(data)
new_data.reverse()
data = tuple(new_data)
print(data)
data = ("Ahmad", "AbuBakar", "Osama", "AhamdRaja")
new_data =list(data)
new_data.sort()
data = tuple(new_data)
print(data)
data = ("Ahmad", "AbuBakar", "Osama", "AhamdRaja", "Ali")
new_data =list(data)
new_data.remove("Ali")
data = tuple(new_data)
print(data)
# String formating nad f-string:
name = "Ahmad"
age = 21
hight = 5.9
print("My name is \"%s\" and my age is \'%d\' \nAnd hight is \'%f\'"%(name, age, hight))
print("My name is \"{}\" and my age is \'{}\ \nAnd hight is \'{}\'".format(name,age,hight))
print("My name is \"{0}\" and my age is \'{1}\' \nAnd hight is \'{2}\'".format(name,age,hight))
print("\"{0}\" is a student. \"{1}\" study in UNI.\nHe is \'{2}\' years old".format(name, name, age))
name = "Ahmad"
age = 21
hight = 5.9
print(f"My name is \"{name}\".I'm \'{age}\' years old. \nAnd my hight is\'{hight}\'")
num1 = 20
num2 = 10
print(f"Total sum = \'{num1 + num2}\'")
print(f"Total sub = \'{num1 - num2}\'")
print(f"Total multiply = \'{num1*num2}\'")
def square(num):
    return num*num
num =2
print(f"The square of {num} is \'{square(num)}\'")
def sum(num1,num2):
    return num1 + num2
num1= 2
num2 =3
print(f"The sum of \'{num1}\' + \'{num2}\' is \'{sum(num1,num2)}\'")
num = 123456
print(f"\'{num:,}\'")
num = 1234567890
print(f"\'{num:,}\'")
num = 0.89
print(f"{num:2%}")
name = "Ahmad"
print(f"{name:<10}")
print(f"{name:>20}")
print(f"{name:^15}")
num = 99.234
print(f"{num:.2f}")
num =457
print(f"{num:09}")
data = {"name" :"Ahmad", "age": 21}
print(f"name :{data["name"]}")
print(f"Age :{data["age"]}")
data = ["Ahmad", "AbuBakar", "Osama", "AhmadRaja"]
print(f"First student is \"{data[0]}\"")
print(f"Second student is \"{data[1]}\"")
print(f"Third student is \"{data[2]}\"")
print(f"Fourth student in {{data}} is \"{data[3]}\"")
# Doc String:
def sum(num1, num2):
    """The addition of two numbers is"""
    return num1 + num2
print(sum.__doc__)
print(sum(2,3))
def square(num):
    """The square of  number is"""
    return num*num
print(square.__doc__)
print(square(2))
# Recursion
def num(n):
    if n == 0:
        return
    print(n)
    num(n -1)
num(5)
def num(n):
    if n ==6:
        return
    print(n)
    num(n+1)
num(1)
def num(n):
    if n>5:
        return
    print(n)
    num(n+1)
num(1)
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n*factorial(n-1)
print(factorial(5))
def factorial(num):
    if num ==0 or num ==1:
        return 1
    return num*factorial(num - 1)
print(factorial(10))
def sum(num):
    if num == 0:
        return 0
    return num+sum(num-1)
print(sum(5))
def multiply(num):
    if num == 5:
        return 5
    return num * multiply(num+1)
print(multiply(2))
def divide(num):
    if num == 8:
        return 8
    return num / divide(num+1)
print(divide(2))
def fibonacci(num):
    if num <=1:
        return num
    return fibonacci(num-1) + fibonacci(num-2)
print(fibonacci(0))
print(fibonacci(1))
print(fibonacci(2))
print(fibonacci(3))
print(fibonacci(4))
print(fibonacci(5))




