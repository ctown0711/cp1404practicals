"""Silver service taxi class"""

from taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Silver service taxi class"""
    flagfall = 4.50

    def __init__(self, name, fuel, fanciness):
        """Initialise a Silver service taxi object"""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km *= fanciness

    def __str__(self):
        """Return a string of a silver service taxi object"""
        return f"{super().__str__()} plus flagfall of ${self.flagfall:.2f}"

    def get_fare(self):
        """Get the fare of a silver service taxi object"""
        return super().get_fare() + self.flagfall
