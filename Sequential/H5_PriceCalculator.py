total = 0
count = 1

while True:
    price = float(input(f"Enter the price of the {count} item: "))
    quantity = int(input(f"Enter the quantity of the {count} item: "))

    total += price * quantity

    choice = input("Do you want to enter another item? (yes/no): ")
    print(f"Choice entered = [{choice}]")

    if choice.strip().lower() == "no":
        break
    count += 1

print("Total Price:", int(total))