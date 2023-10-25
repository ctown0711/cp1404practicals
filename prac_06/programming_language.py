"""
Programming Language
Estimate: 25 minutes
Actual: 29 minutes
"""


class ProgrammingLanguage:

    def __init__(self, name="", typing="", reflection="", year=0):
        """Initialise a ProgrammingLanguage object."""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        """Return string of a ProgrammingLanguage object"""
        return f"{self.name}, {self.typing}, Reflection={self.reflection}, First appeared in {self.year}"

    def is_dynamic(self):
        """Determine if language is dynamically typed."""
        return self.reflection

