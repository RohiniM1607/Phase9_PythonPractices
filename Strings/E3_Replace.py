StrWithSymbol = input("Enter the string with special symbols:")
for i in StrWithSymbol:
    if(i.isalnum()): continue
    else: StrWithSymbol=StrWithSymbol.replace(i,"#")
print(StrWithSymbol)
