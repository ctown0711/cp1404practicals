"""
Project class
"""


class Project:

    def __init__(self, name="", date=0, priority=0, cost_estimate=0.0, completion_percent=0.0):
        self.name = name
        self.date = date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percent = completion_percent

    def __str__(self):
        return (f"{self.name}, start: {self.date}, priority {self.priority},"
                f" estimate: ${self.cost_estimate}, completion: {self.completion_percent}%")