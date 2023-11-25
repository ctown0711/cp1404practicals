"""Band Class"""


class Band:
    """Band class"""

    def __init__(self, name=""):
        """Initialise band object"""
        self.name = name
        self.musicians = []

    def __str__(self):
        """Return a string representation of the band"""
        return f"{self.name} {', '.join([str(musician) for musician in self.musicians])}"

    def add(self, musician):
        """Add a band member"""
        self.musicians.append(musician)

    def play(self):
        """Return a string representation of the band playing"""
        return '\n'.join([musician.play() for musician in self.musicians])
