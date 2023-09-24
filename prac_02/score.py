"""
CP1404/CP5632 - Practical
Determine grading based on score
"""
import random


def main():
    """Print grade based on score"""
    score = float(input("Enter score: "))
    while score < 0 or score > 100:
        print("Invalid score")
        score = float(input("Enter score: "))
    print(determine_grade(score))
    random_score = random.randint(0, 100)
    print(random_score)
    print(determine_grade(random_score))


def determine_grade(score):
    """Calculate grading"""
    if score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


main()
