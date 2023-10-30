"""
Guitars
Estimate: 40 minutes
Actual: 44 minutes
"""

from guitar import Guitar

guitars = [Guitar("Gibson L-5 CES", 1922, 16035.40), Guitar("Fender Stratocaster", 2014, 765.4)]
gibson = Guitar("Gibson L-5 CES", 1922, 16035.40)
fender = Guitar("Fender Stratocaster", 2014, 765.4)
print(f"{gibson.name} get_age() - Expected 101. Got {gibson.get_age()}")
print(f"{fender.name} get_age() - Expected 9. Got {fender.get_age()}")
print(f"{gibson.name} is_vintage() - Expected True. Got {gibson.is_vintage()}")
print(f"{fender.name} is_vintage() - Expected False. Got {fender.is_vintage()}")
