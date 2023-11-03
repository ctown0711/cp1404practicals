from guitar import Guitar

FILENAME = "guitars.csv"

in_file = open(FILENAME)
guitars = []
for line in in_file:
    parts = line.strip().split(',')
    guitar = Guitar(parts[0], int(parts[1]), float(parts[2]))
    guitars.append(guitar)
name = input("Name: ")
while name != "":
    year = int(input("Year: "))
    cost = float(input("Cost: $"))
    guitar = Guitar(name, year, cost)
    guitars.append(guitar)
    print(f"{guitar} added.")
    name = input("Name: ")
print("These are my guitars:")
guitars.sort()
out_file = open("guitar.csv", 'w')
for guitar in guitars:
    print(guitar)
    print(f"{guitar.name},{guitar.year},{guitar.cost}", file=out_file)

