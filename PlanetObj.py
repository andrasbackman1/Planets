import csv
import numpy as np
from math import atan, pi

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
        self.printed = False
        self.name = name
        with open("ParameterData.csv", "r") as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == self.name:
                    self.mass = float(row[1])
                    self.position = np.array([row[2], row[3]], dtype = "float64")
                    self.velocity = np.array([row[4], row[5]], dtype = "float64")
                    self.acceleration = np.array([row[6], row[7]], dtype = "float64")
        self.originalPosition = self.position.copy()
        self.countSteps = 0

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

    def UpdatePosition(self, newPosition, timestep):
        self.countSteps += 1
        
        theta = atan(newPosition[1]/newPosition[0])
        if self.name != "Mars" and self.printed is False:
            if theta >= 0 and theta <= 0.1 and self.countSteps > 5:
                OrbPeriod = self.countSteps*(timestep[0])*1.15741*10**(-5)*2
                print("{object}'s orbital period is: {period} days".format(object = self.name, period = round(OrbPeriod,4)))
                self.printed = True  
        
        self.position = newPosition
        return None

def main():
    Planet("Phobos")

if __name__ == "__main__":
    main()