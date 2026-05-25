mark = int(input("Enter the mark: "))
if mark > 90:
    print("Grade O")
elif mark >= 81 and mark <= 90:
    print("Grade A")
elif mark >= 71 and mark <= 80:
    print("Grade B")
elif mark >= 61 and mark <= 70:
    print("Grade C")
elif mark >= 50 and mark <= 60:
    print("Grade D")
else:
    print("Grade F")


num = int(input("Enter the number: "))
fact = 1
if num < 0:
    print("Not defined")
elif num == 0:
    fact = 1
    print(fact)
else:
    for i in range(1, num + 1):
        fact = fact * i
    print(fact)

n = int(input("Enter the value of n: "))
i = 1
sum = 0
while i<= n:
    num = int(input("Enter the number: "))
    if num == -1:
        break
    else:
        sum = sum + num
    i = i+1
print("The sum of user inpt is ", sum)


#Nested Loop Statement
l = int(input("Enter Lower limit value: "))
u = int(input("Enter upper limit value: "))
print("The prime numbers between", l,"and", u, "are")
for num in range(l, u+1):
    if num > 1 :
        for i in range(2, num):
            if(num % i) == 0:
                break
        else:
            print(num)


for I in 'Smart clif':
        if I == 'r':
                pass
        print(I, end=',')