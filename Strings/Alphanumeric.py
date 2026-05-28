sentence = input("Enter the sentence:").split(" ")
for i in sentence:
    if(i.isalpha() or i.isdigit()): continue
    else: print(i)
