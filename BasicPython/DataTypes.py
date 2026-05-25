num1 = 10
print(type(num1))
num2 = -23
print(type(num2))
var1 = True
print(type(var1))
str1 = "Rohini"
print(str1)
list1 = [5,43,5, "Rohini", 45.4, True]
print(list1)
tuple1 = (32, 435.34, "SDg", False)
print(tuple1)
set1 = {1,34.42, "dg", True, True, 1}
print(set1)
print(tuple1)
list1 = [24]
set1 = {1}
tuple1 = (45)

print(list1)
print(set1)
print(tuple1)

var = None
print(type(var))
print(var)

student = {"name": "Alice", "age": 24, "Grade": "A"}
print(student)

x = (1==True)
y=(1==False)
a = True+10
b = False +5

print(a)
print(b)
print(x)
print(y)

print("Identity operator")
num1 = 5
num2 = num1
print(num1 is not num2)
print(id(num1))

#Explicit Type conversion
num1 = 10
num2 = 20
num3 = num1 + num2
print(num3)
print(type(num3))
num4 = float(num1+num2)
print(num4)
print(type(num4))

#Input and Output
fname = input("Enter your first name: ")
age = input("Enter your age: ")
print("First name is",fname,"and Age is ",age)
#Formatting with f
print(f"First name is {fname} and age is {age}")
#Seperator and end parameter
print(f"First name is {fname}",f" age is {age}", sep=",", end=".\n")
print(1, 2, 3, sep=",", end=".\n")
print(type(fname))
print(type(age))