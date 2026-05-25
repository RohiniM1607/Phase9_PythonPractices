import math
a = float(input("Enter the length of side a: "))
b = float(input("Enter the length of side b: "))
c = float(input("Enter the length of side c: "))
if(a+b>c and a+c>b and b+c>a):
    s = (a+b+c)/2
    print("Area of triangle: ", math.sqrt(s*(s-a)*(s-b)*(s-c)))
else:
    print("Doesn't form valid triangle")