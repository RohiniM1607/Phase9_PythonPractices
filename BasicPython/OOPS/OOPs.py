class MyClass:
    def display1():
        print("Welcome")
    def display2(self):
        print("Welcome")
    def display3(self, name):
        print("Welcome",name)

    
print(MyClass)

myObj1 = MyClass()
print(myObj1)
myObj2 = MyClass()
print(myObj2)

//myObj1.display1()
myObj1.display2()
myObj1.display3('Rohini')

#Class Member
class MyClass:
    x = 5 #State
    def display(self): #Behaviour
        print("I am inside the function")

obj = MyClass()
print('State: ', obj.x)
print('Behaviour: ' )
obj.display()

#init method
class MyClass:
    def __init__(self, name):
        self.name = name
    def __init__(self, age):
        self.age = age
    def sayHi(self):
        print("Hello, My name is ", self.age)

obj = MyClass("Rohini")
obj = MyClass(23)
obj.sayHi()

class Circle:
    def __init__(self, radius=1.0, color='red'):
        self.radius = radius
        self.color = color
    def getRadius(self):
        return self.radius
    def getColor(self):
        return self.color
    def setRadius(self, radius):
        self.radius=radius
    def setColor(self, color):
        self.color = color
    def getArea(self):
        return 3.14159*self.radius*self.radius
    def __str__(self):
        return f"Circle[radius={self.radius}, color={self.color}]"
    
circle1 = Circle()
print(circle1)

circle2 = Circle(2.5)
print(circle2)

circle3 = Circle(3.5, 'Blue')
print(circle3)


class Circle:
    def __init__(self, radius=1.0, color='red'):
        self.radius = radius
        self.color = color
    @classmethod
    def withRadius(cls, radius):
        return cls(radius)
    def withRadiusandColor(cls, radius, color):
        return cls(radius, color)
    def getRadius(self):
        return self.radius
    def getColor(self):
        return self.color
    def getArea(self):
        return 3.14159*self.radius*self.radius
    def __str__(self):
        return f"Circle[radius={self.radius}, color={self.color}]"
circle1 = Circle()
print(circle1)

circle2 = Circle(2.5)
print(circle2)

circle3 = Circle(3.5, 'Blue')
print(circle3)

class Circle:
    def __init__(self, *args):
        if len(args) == 0:
            self.radius = 1.0
            self.color = "red"
        elif len(args) == 1:
            self.radius = args[0]
            self.color = "red"
        elif len(args) == 2:
            self.radius = args[0]
            self.color = args[1]
        else:
            raise ValueError("Too many arguments")
    def getRadius(self):
        return self.radius
    def getColor(self):
        return self.color 



#Access Specifier
class Student:
    def __init__(self):
        self.name = "Shon"
        self.__age = 39
obj = Student()
print(obj.name)
print(obj.__age)

class Student:
    def __init__(self):
        self._name = "Python"
    def _funName(self):
        return "Method here"
class Subject(Student):
    pass
obj = Student()
obj1 = Subject()
print(obj._name)
print(obj._funName)
print(obj1._name)
print(obj1._funName)

class Student:
    def __init__(self, name, age):
        self.name = name
        self.__age = age
    def get_age(self):
        return self.__age
    def set_age(self, age):
        self.__age = age
stud = Student('Mary', 14)
print('Name: ', stud.name, stud.get_age())
stud.set_age(16)
print('Name: ', stud.name, stud.get_age())