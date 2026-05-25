def Square(side):
    print("Area of Square: ", side*side)

def Circle(radius):
    print("Area of Circle: ", 3.14*radius*radius)

def Rectangle(length, breadth):
    print("Area of Rectangle: ", length*breadth)

while True:
    print("Menu")
    print("1. Area of Square: ")
    print("2. Area of Circle: ")
    print("3. Area of Rectangle: ")
    print("4. Exit")
    choice = int(input("Enter the choice: "))

    if choice == 1:
        side = int(input("Enter the sides of square: "))
        Square(side)

    elif choice == 2:
        radius = int(input("Enter the radius of circle: "))
        Circle(radius)

    elif choice == 3:
        length = int(input("Enter the length of rectangle: "))
        breadth = int(input("Enter the breadth of rectangle: "))
        Rectangle(length, breadth)

    elif choice == 4:
        break

    else:
        print("Wrong choice")