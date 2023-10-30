"""
Guitars
Estimate: 40 minutes
Actual: 44 minutes
"""

CURRENT_YEAR = 2023
VINTAGE_AGE = 50


class Guitar:
    """Guitar class"""

    def __init__(self, name="", year=0, cost=0):
        """Initialise Guitar object."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return Guitar as a string"""
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def get_age(self):
        """Get the age of a Guitar"""
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        """Determine if a Guitar is vintage based on its age"""
        return self.get_age() >= VINTAGE_AGE
