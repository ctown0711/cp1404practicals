from guitar import Guitar

FILENAME = "guitars.csv"

in_file = open(FILENAME)
guitars = []
in_file.readline()
for line in in_file:
    parts = line.strip().split(',')
    guitar = Guitar(parts[0], parts[1], float(parts[2]))
    guitars.append(guitar)
for guitar in guitars:
    print(guitar)
guitars.sort()
for guitar in guitars:
    print(guitar)