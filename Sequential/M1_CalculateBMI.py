weight = float(input("Enter the weight: "))
height = float(input("Enter the Height: "))
if(weight > 0 and height > 0):
    BMI = weight / (height*height)
    print("BMI: {:.2f}".format(BMI))
else:
    print("Negative values not allowed to find BMI")