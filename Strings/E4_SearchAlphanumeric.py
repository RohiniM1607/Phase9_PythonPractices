str1 = input("Enter the string: ").split()
for word in str1:
    if word.isalnum() and any(ch.isdigit() for ch in word):
        print(word)