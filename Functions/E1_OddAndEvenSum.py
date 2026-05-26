def sumOfOddandEven(n):
    even=0
    odd=0
    for i in range(0, n+1):
        if(i%2==0):
            even+=i
        else:
            odd+=i
    
    print("Even sum: ", even)
    print("Odd sum: ", odd)
    
num = int(input("Enter the range: "))
sumOfOddandEven(num)