age = int(input("Enter the age: "))
if(age<=0):
    print("Invalid Age")
elif(age<=10):
    print("Cartoon Club")
elif(age>10 and age<20):
    print("Teens Club")
else:
    print("Not Allowed")
