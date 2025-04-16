import math

# Gets the input from the user
def getUserInput():
    weight = float(input("Enter your weight in lbs: "))
    height = float(input("Enter your height in inches: "))
    return height, weight

# Performs the BMI calculation using the user's height and weight
def getBMI(height, weight):
    BMI = (weight * 703) / pow(height, 2)
    print(f"Your BMI is: {BMI:.2f}")

h, w = getUserInput() # Store the height in 'h' and weight in 'w' after calling getUserInput()
getBMI(h, w)          # Call getBMI() while passing in the user's input