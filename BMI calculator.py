def calculate_bmi(weight, height_cm):
    height_m = height_cm / 100  # Convert height from cm to meters
    bmi = weight / (height_m ** 2)
    return bmi

def interpret_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"

# Get user input
weight = float(input("Enter your weight in kilograms: "))
height_cm = float(input("Enter your height in centimeters: "))

# Calculate BMI
bmi = calculate_bmi(weight, height_cm)

# Interpret BMI
category = interpret_bmi(bmi)

# Display the result
print(f"Your BMI is {bmi:.2f}. You are classified as: {category}.")
