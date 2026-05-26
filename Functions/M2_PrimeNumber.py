def isPrime(num):
    if num < 2:
        return False

    for i in range(2, num):
        if num % i == 0:
            return False

    return True

def printPrimeNumbers(x, y):
    if x > y:
        print("Provide valid input")
    else:
        for i in range(x, y + 1):
            if isPrime(i):
                print(i, end=" ")

x = int(input("Enter the starting number: "))
y = int(input("Enter the ending number: "))
printPrimeNumbers(x, y)