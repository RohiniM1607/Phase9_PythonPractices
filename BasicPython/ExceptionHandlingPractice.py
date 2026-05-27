try:
    a = int(input("Enter the a value: "))
    b = int(input("Enter the b value: "))
    c = a/b
except NameError:
    print("This is Value Error")
except ZeroDivisionError:
    print("Can't divide by zero")
else:
    print("After division: ",c)

