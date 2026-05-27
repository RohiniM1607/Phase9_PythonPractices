t = [] #Empty list
print(t)
t = [1,2,3,4,5] #List of integer
print(t)
t = [1,2.3,'ABC'] #List with mixed type
print(t)
t = [1,2,'ABC', [4, 'xyz'], 8] #Nested list
print(t)

#Constructor list()
t = list()
print(t)
str = 'aeiou'
t = list(str)
print(t)

del t[3]  #Delete individual item
print(t)

# del t   #Delete entire list
# print(t)


list1 = ['Red', 'Green', 'Blue', 'Black', 'Red'] #Iterating the element of list using range and len function
for i in range(len(list1)):
    print(list1[i], end=' ')

list1 = [1,8638,4252,23,35978]
list1.sort()
print(list1)
list1.sort(reverse=True)
print(list1)

list1 = ['Tiger', 'Zebra', 'Lion', 'Deer', 'Panda', 'Elephant', 'Cat', 'Mouse', 'Dog']
list1.sort()
print(list1)
list1.sort(reverse=True)
print(list1)

listA = []
n = int(input("Enter the number of elements in the list: "))
for i in range(0, n):
    print("Enter element No-{}".format(i+1))
    element = int(input())
    listA.append(element)
print("The entered list is ", listA)

listB = []
n = int(input("Enter number of elements in list: "))
listB = input("Enter the list elements seperated by comma: ").split(',')
print(listB)

listC = list(map(eval, input("Enter the List elements seperated by space: ").split()))
print("The entered list\n", listC)

ele = [x**2 for x in range(5) if(x%2==0)]
print(ele)

def increment(list2):
    for i in range(0, len(list2)):
        list2[i]+=5
    print("Reference of list inside function", id(list2))

list1 = [1,2,3,4,5]
print("Reference of list in Main", id(list1))
print("The list before the function call")
print(list1)
increment(list1)
print("The list after the function call")
print(list1)

def increment(list2):
    print("Id of list inside function before assignmen: ", id(list2))
    list2=[1,2,3,4,5]
    for i in range(0, len(list2)):
        list2[i]+=5
    print("Reference of list inside function", id(list2))
    print(list2)

list1 = [10,20,30,40,50]
print("Reference of list in Main", id(list1))
print("The list before the function call")
print(list1)
increment(list1)
print("The list after the function call")
print(list1)