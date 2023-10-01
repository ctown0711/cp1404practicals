"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur? When an input that isn't an integer is entered (1.5, abc)
2. When will a ZeroDivisionError occur? When a user tries to divide by (denominator) Zero
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator == 0:
        print("Cannot divide by zero!")
        numerator = int(input("Enter the numerator: "))
        denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
print("Finished.")
