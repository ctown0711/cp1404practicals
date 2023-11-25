"""Taxi Simulator Program"""

from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi

MENU = f"q)uit, c)hoose taxi, d)rive"


def main():
    """Run Taxi Simulator"""
    current_taxi = None
    bill_to_date = 0.0
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    print("Lets drive!")
    print(MENU)
    menu_choice = input(">>> ").upper()
    while menu_choice != "Q":
        if menu_choice == "D":
            if current_taxi is None:
                print("You need to choose a taxi before you can drive")
            else:
                distance = int(input("Drive how far? "))
                current_taxi.start_fare()
                current_taxi.drive(distance)
                print(f"Your {current_taxi.name} trip cost you ${current_taxi.get_fare():.2f}")
                bill_to_date += current_taxi.get_fare()
        elif menu_choice == "C":
            print("Taxis available:")
            print_taxis(taxis)
            taxi_choice = int(input("Choose taxi: "))
            try:
                current_taxi = taxis[taxi_choice]
            except IndexError:
                print("Invalid taxi choice")
        else:
            print("Invalid option")
        print(f"Bill to date: ${bill_to_date:.2f}")
        print(MENU)
        menu_choice = input(">>> ").upper()
    print(f"Total trip cost: ${bill_to_date:.2f}\nTaxis are now:")
    print_taxis(taxis)


def print_taxis(taxis):
    """Print a list of the available taxis"""
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")


main()
