# BMI Calculator - by Rishika Future AIML Engineer

weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))

bmi = weight / (height * height)

print("\nYour BMI is:", round(bmi, 2))

if bmi < 18.5:
    print("You are Underweight")
elif bmi < 24.9:
    print("You are Normal weight - Perfect")
elif bmi < 29.9:
    print("You are Overweight")
else:
    print("You are Obese - konjam care pannu")