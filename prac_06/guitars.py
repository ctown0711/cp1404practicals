"""
Guitars
Estimate: 40 minutes
Actual:  44 minutes
"""

from guitar import Guitar

guitars = []
guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))
name = input("Name: ")
while name != "":
    year = int(input("Year: "))
    cost = float(input("Cost: $"))
    guitar = Guitar(name, year, cost)
    guitars.append(guitar)
    print(f"{guitar} added.")
    name = input("Name: ")
print("These are my guitars:")
name_format_width = max(len(guitar.name) for guitar in guitars)
for i, guitar in enumerate(guitars, 1):
    vintage_string = ""
    if guitar.is_vintage():
        vintage_string = " (vintage)"
    print(f"Guitar {i}: {guitar.name:>{format_name}} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage_string}")
