def oddSum(lowerbound, upperbound):
    odd_sum = 0
    for i in range(lowerbound, upperbound + 1):
        if i % 2 != 0:
            odd_sum += i
    return odd_sum


def evenSum(lowerbound, upperbound):
    even_sum = 0
    for i in range(lowerbound, upperbound + 1):
        if i % 2 == 0:
            even_sum += i
    return even_sum

lowerbound = int(input("Enter lower bound: "))
upperbound = int(input("Enter upper bound: "))
odd_total = oddSum(lowerbound, upperbound)
even_total = evenSum(lowerbound, upperbound)
difference = abs(odd_total - even_total)

print("The sum of odd numbers from", lowerbound, "to", upperbound, "is:", odd_total)
print("The sum of even numbers from", lowerbound, "to", upperbound, "is:", even_total)
print("The absolute difference between the two sums is:", difference)