print("Welcome to the Body Mass Index Calculator")

height = float(input("Please enter your height (cm): "))
weight = float(input("Now enter your weight (kg): "))

height_meters = height / 100

BMI = round(weight / (height_meters**2), 2)

print(f"BMI: {BMI}")
print("Your result is:", end=" ")

if BMI < 18.5:
    print("Underweight")
elif BMI <= 24.9:
    print("Normal")
elif 25 <= BMI <= 29.9:
    print("Overweight")
else:
    print("Obesity")

