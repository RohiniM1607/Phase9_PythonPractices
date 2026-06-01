name = input("Enter customer name: ")
items = int(input("Enter number of items: "))
if items < 10:
    price = 12
elif items < 100:
    price = 10
else:
    price = 7

total_cost = items * price

print(name, total_cost)