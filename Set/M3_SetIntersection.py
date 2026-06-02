set1 = set(map(int, input("Enter first set elements: ").split()))
set2 = set(map(int, input("Enter second set elements: ").split()))

common = set1.intersection(set2)

print("Common elements:", common)