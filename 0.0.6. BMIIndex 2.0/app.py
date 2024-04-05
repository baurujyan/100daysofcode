# BMI Index app

height = float(input("Input your height in meters: "))
weight = float(input("Input your weight in kilograms: "))

bmi_index = weight / (height * height)

print(f"Your BMI Index is {format(bmi_index, ".2f")}.")
if bmi_index < 18.5:
    print("You are underweight.")
elif bmi_index < 25:
    print("You have a normal weight.")
elif bmi_index < 30:
    print("You are slightly overweight.")
elif bmi_index < 35:
    print("You are obese.")
else:
    print("You are clinically obese.")