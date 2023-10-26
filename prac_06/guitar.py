"""
Guitars
Estimate: 40 minutes
Actual: 44 minutes
"""


class Guitar:
    """Guitar class"""
    def __init__(self, name="", year=0, cost=0):
        """Initialise Guitar object."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return Guitar as a string"""
        return f"{self.name}, ({self.year}) : ${self.cost:,}"

    def get_age(self):
        """Get the age of a Guitar"""
        return 2023 - self.year

    def is_vintage(self):
        """Determine if a Guitar is vintage based on its age"""
        return self.get_age() >= 50
