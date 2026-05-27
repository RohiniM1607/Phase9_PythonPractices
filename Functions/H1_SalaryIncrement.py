def calculate_increment(salary, rating):
    incrementedSalary = None
    if rating >= 1 and rating <= 4:
        incrementedSalary = salary + (salary * 0.10)

    elif rating >= 4.1 and rating <= 7:
        incrementedSalary = salary + (salary * 0.25)

    elif rating >= 7.1 and rating <= 10:
        incrementedSalary = salary + (salary * 0.30)

    return incrementedSalary

salary = int(input("Enter the Salary "))
rating = float(input("Enter the appraisal rating "))
result = calculate_increment(salary, rating)
print(result)