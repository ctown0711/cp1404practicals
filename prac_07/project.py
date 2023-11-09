"""
Project class
"""
from datetime import datetime


class Project:
    """Represent information about a project"""

    def __init__(self, name="", date="", priority=0, cost_estimate=0.0, completion_percent=0):
        """Initialise a project object"""
        self.name = name
        self.date = date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percent = completion_percent

    def __str__(self):
        """Return string representation of a Project"""
        return (f"{self.name}, start: {self.date}, priority {self.priority},"
                f" estimate: ${self.cost_estimate}, completion: {self.completion_percent}%")

    def __lt__(self, other):
        return self.priority < other.priority

    def __gt__(self, other):
        return self.date > other.date
