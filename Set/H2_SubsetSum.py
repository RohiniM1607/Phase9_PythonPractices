from itertools import combinations
def subset_sum_to_target(input_set, target_sum):
    elements = list(input_set)
    result = []
    for r in range(1, len(elements) + 1):
        for combo in combinations(elements, r):
            if sum(combo) == target_sum:
                result.append(set(combo))
    return result
input_set = set(map(int, input("Enter set elements: ").split()))
target_sum = int(input("Enter target sum: "))
print(subset_sum_to_target(input_set, target_sum))