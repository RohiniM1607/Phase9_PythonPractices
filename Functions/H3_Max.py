def findMax(*numbers):
    maximum = numbers[0]

    for num in numbers:
        if num > maximum:
            maximum = num

    return maximum

result1 = findMax(25, 12, 18, 30)
print("maximum value among four integers:", result1)

result2 = findMax(8, 15, 22, 17, 12)
print("maximum value among five integers:", result2)