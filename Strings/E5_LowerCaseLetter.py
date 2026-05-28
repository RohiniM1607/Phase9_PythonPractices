word = input("Enter the word:")
lower=''
upper=''
for i in word:
    if(i.islower()):
        lower=lower+i
    else:
        upper=upper+i
print(lower+upper)
