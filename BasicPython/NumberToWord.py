def split_digits(num, number):
    for i in num:
        number.append(int(i))

def numToWords(number):
    num = {0: 'zero' , 1:'one', 2:'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine'}
    for i in number:
        print(num[i], end=' ')

num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")
num3 = input("Enter the third number: ")
number = []
split_digits(num1, number)
split_digits(num2, number)
split_digits(num3, number)
print(number)
numToWords(number)