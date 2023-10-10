colour_to_code = {"Black": '#000000', "Brown": '#a52a2a', "Emerald": '#50c878',
                  "FerrariRed": '#ff2800', "GoldenYellow": '#ffdf00', "GreenLizard": 'a7f432',
                  "Iceberg": '71a6d2', "Lavender": 'e6e6fa', "Magenta": 'ff00ff', "OrangePeel": 'ff9f00'}

colour_choice = input("Enter colour name: ").title().replace(' ', '')
while colour_choice != "":
    try:
        print(f"{colour_choice} - {colour_to_code[colour_choice]}")
    except KeyError:
        print("Invalid Colour Choice")
    colour_choice = input("Enter colour name: ").title().replace(' ', '')
