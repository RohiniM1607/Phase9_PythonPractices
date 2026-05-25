str = 'Good Day'
print(str.upper())
print(str.lower())
print(str.find('o'))
print(str.find('o', 4))
print(str.find('od'))
print(str.replace('Good', 'Happy'))
print(str.count('o'))
print(str.capitalize())
print(str.isalnum())
print(str.isalpha())
print(str.endswith('day'))
print(str.startswith('Good'))

n = input("Enter String: ")

if n == n[::-1]:
    print(n,"is palindrome string")
else:
    print(n,"is not a palindrome string")

string = input("Enter the String: ")
digit = 0
letter = 0
for s in string:
    if s.isnumeric():
        digit+=1
    elif s.isalpha():
        letter+=1
    else:
        pass
print("Total letters: ", letter)
print("Total digit: ", digit)