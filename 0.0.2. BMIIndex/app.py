# BMI Index app

height = float(input("Input your height in meters: "))
weight = float(input("Input your weight in kilograms: "))

bmi_index = weight / (height * height)

print(f"Your BMI Index is {format(bmi_index, ".2f")}.")