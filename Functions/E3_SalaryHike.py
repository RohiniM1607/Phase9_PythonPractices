oldSalary = float(input("Enter old salary per month: "))
hike = float(input("Enter hike percentage: "))
newSalary = oldSalary + (oldSalary * hike / 100)
print("New Salary after hike:", newSalary)