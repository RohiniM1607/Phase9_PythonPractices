List = [1,2,3,4,5]

while True:
    print("List Operation Menu")
    print("1. Append an element")
    print("2. Insert an element")
    print("3. Append a list to the given list")
    print("4. Modify an existing element")
    print("5. Delete an existing element from its position")
    print("6. Delete an existing element with a given value")
    print("7. Sort the list in ascending order")
    print("8. Sort the list in descending order")
    print("9. Display the list")
    print("10. Exit")

    choice = int(input("Enter the choice: "))
    if choice == 1:
        element = int(input("Enter the element to append: "))
        List.append(element)

    elif choice == 2:
        position = int(input("Enter the position to insert: "))
        element = int(input("Enter the element to insert: "))
        List.insert(position, element)

    elif choice == 3:
        list = list(input("Enter the list element with Space seperated :").split())
        List.extend(list)

    elif choice == 4:
        position = int(input("Enter the position to modify the element: "))
        element = int(input("Enter the element to modify in the existing list: "))
        List[position] = element

    elif choice == 5:
        position = int(input("Enter the position to delete: "))
        List.pop(position)

    elif choice == 6:
        value = int(input("Enter the element to delete: "))
        List.remove(value)

    elif choice == 7:
        List.sort()

    elif choice == 8:
        List.sort(reverse=True)

    elif choice == 9:
        print("List Elements:",List)

    elif choice == 10:
        print("Exiting the Program!!..")
        break

    else:
        print("Invalid choice.. Try again!!")
