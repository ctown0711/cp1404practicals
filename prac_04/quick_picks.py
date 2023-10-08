import random

MINIMUM_VALUE = 1
MAXIMUM_VALUE = 45
TOTAL_NUMBERS = 6

number_of_quick_picks = int(input("How many quick picks? "))

for i in range(number_of_quick_picks):
    quick_picks = []
    for j in range(TOTAL_NUMBERS):
        random_number = random.randint(MINIMUM_VALUE, MAXIMUM_VALUE)
        while random_number in quick_picks:
            random_number = random.randint(MINIMUM_VALUE, MAXIMUM_VALUE)
        quick_picks.append(random_number)
        quick_picks.sort()
    print(' '.join(f"{number:2}" for number in quick_picks))