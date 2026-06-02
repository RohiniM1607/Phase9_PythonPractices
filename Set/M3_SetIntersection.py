set1 = set(map(int, set1.split()))

common = set.intersection(set1)
output = len(common)

print(output)
