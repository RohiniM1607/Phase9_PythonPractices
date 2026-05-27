def calculate_salary(oldSalary, hike):
    newSalary = oldSalary + (oldSalary * hike / 100)
    return newSalary

oldSalary = float(input("Enter old salary per month: "))
hike = float(input("Enter hike percentage: "))

newSalary = calculate_salary(oldSalary, hike)

print("New Salary after hike:", newSalary)