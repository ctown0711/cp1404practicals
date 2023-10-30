"""
Guitars
Estimate: 40 minutes
Actual:  44 minutes
"""

from guitar import Guitar

guitars = []  # Not sure if this is whats expected since we're given .append code in the practical
guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))
name = input("Name: ")
while name != "":
    year = int(input("Year: "))
    cost = float(input("Cost: $"))
    guitars.append(Guitar(name, year, cost))
    print(f"{name} ({year}) : ${cost} added.")
    name = input("Name: ")
print("These are my guitars:")
format_name = max(len(name) for guitar in guitars)
for i, guitar in enumerate(guitars, 1):
    vintage_string = ""
    if guitar.is_vintage():
        vintage_string = " (vintage)"
    print(f"Guitar {i}: {guitar.name:{format_name}} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage_string}")
