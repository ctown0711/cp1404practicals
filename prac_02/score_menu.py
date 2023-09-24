"""
Menu program gets score, determines grade, and prints as many asterisks as score
"""


def main():
    """Menu program to get score, determine grade, and print asterisks based on score"""
    score = get_valid_score()
    print(f"(G)et Score\n(P)rint result\n(S)how stars\n(Q)uit")
    menu_choice = input(">>> ").title()
    while menu_choice != 'Q':
        if menu_choice == 'G':
            score = get_valid_score()
        elif menu_choice == 'P':
            grade = determine_grade(score)
            print(grade)
        elif menu_choice == 'S':
            print_stars(score)
        else:
            print('Invalid Menu Choice')
        print(f"(G)et Score\n(P)rint result\n(S)how stars\n(Q)uit")
        menu_choice = input(">>> ").title()
    print("Farewell")


def print_stars(score):
    """Print stars times score"""
    print(score * '*')


def get_valid_score():
    """Get a valid score input"""
    score = int(input("Score 0 - 100: "))
    while score < 0 or score > 100:
        print("Invalid Score 0 - 100")
        score = int(input("Score 0 - 100: "))
    return score


def determine_grade(score):
    """Calculate grading"""
    if score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


main()
