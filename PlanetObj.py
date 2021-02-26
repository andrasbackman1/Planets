import csv
import numpy as np

"""
Planet instances are objects intended to only store information about itself.
Methods only exist to change or return attributes.
"""

class Planet(object):
    """
    Attributes:
        Identity
        mass

        (vectors)
        Acceleration
        Velocity
        Position (from origin)

    Methods:
        constructor
        UpdateAttribute
        ReturnAttribute
    """
    

    def __init__(self, name):
        """
        Input:
            Identity
        Does:
            calls generate inital state
        Returns:
            None
        """

        self.name = name
        with open("ParameterData.csv", "r") as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == self.name:
                    self.mass = float(row[1])
                    self.position = np.array([row[2], row[3]], dtype = "float64")
                    self.velocity = np.array([row[4], row[5]], dtype = "float64")
                    self.acceleration = np.array([row[6], row[7]], dtype = "float64")

    def UpdateAcceleration(self, newAcceleration):
        """
        Input: (velocity, acceleration, or position)
            new attribute
            attribute values
        Returns:
            None
        """
        self.acceleration = newAcceleration
        return None

    def UpdateVelocity(self, newVelocity):
        self.velocity = newVelocity
        return None

    def UpdatePosition(self, newPosition):
        self.position = newPosition
        return None

def main():
    Planet("Phobos")

if __name__ == "__main__":
    main()