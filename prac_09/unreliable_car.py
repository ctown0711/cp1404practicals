from car import Car
from random import randint


class UnreliableCar(Car):
    """Unreliable Car class"""

    def __init__(self, name, fuel, reliability):
        """Initialise UnreliableCar object"""
        super().__init__(name, fuel)
        self.reliability = reliability

    def __str__(self):
        """Return a string suited to the UnreliableCar object"""
        return f"{super().__str__()} Reliability: {self.reliability}"

    def drive(self, distance):
        """Drive an UnreliableCar"""
        if randint(0, 100) >= self.reliability:
            distance = 0
        return super().drive(distance)
