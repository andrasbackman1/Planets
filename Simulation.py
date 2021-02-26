import numpy as np
from numpy.linalg import norm
from scipy.constants import G
from random import randint
"""
Constructor initiates the space and the iterator (with associated methods).
    
    #######
    For when I forget, I used a bunch of static methods because it centralizes the data to the objects.
    This class us only suposed to function as a storage fascility for the methods.
    And I think it will be easier to use them so that I dont need to track who self is all the time.
    ########

"""
class simulator(object):
    """
    Attributes:
        Timestep
        Planets (as iterable/tuple)

    Instance Methods:
        Constructor
        CheckKineticEnergy
    
    Class Methods:
        UpdatePositions
        Iterator
        GenerateAcceleration
        GenerateVelocitie
        GenerateNewPosition
        SumVectors
    """

    def __init__(self):
        return None

    @staticmethod
    def CheckKineticEnergy(planets):
        """
        Inputs:
            all planets
        Does:
            EK_Total = sum of 0.5mv**2
        returns:
            EK_Total
        """
        def Calc_Ek(velocity, mass):
            return 0.5*mass*(norm(velocity))**2
        
        E_kTotal = 0
        for object in planets:
            E_k += Calc_Ek(object.velocity, object.mass)
        
        return E_kTotal

    @staticmethod
    def UpdatePositions(planets, timestep):
        """
        input:(is activated by FuncAnimate in Animate class)
            planets (as an iterable)
        does:
            calls on iterator
            calls to generate EK every n timesteps
        returns:
            positions (as an iterable)
        """
        #if randint(0, 10) == 1: # Prints the total kinetic energy every ~10 iterations
            #print(simulator.CheckKineticEnergy(planets))

        planets = simulator.Iterator(planets, timestep) #is an np array
        return planets
        

    @staticmethod
    def Iterator(planets, timestep):
        """
        Input:
            Planets (as an iterable)
        Does:
            call on three class methods for each planet:
                Generate Accelerations
                Generate Velocities
                Generate new positions
        Returns:
            planets
        """
        for planet in planets:
            new_acceleration = np.zeros((2,))
            for planet2 in planets:
                if planet2 is not planet:
                    new_acceleration += simulator.GenerateAcceleration(planet, planet2) # Not needed for 2 body case but here for the future
            planet.UpdateAcceleration(new_acceleration)
            
        
        for planet in planets:
            # I am aware I am "breaking" the suggested order but these two 
            # only depend on one object's state, not the other's.
            new_velocity = simulator.GenerateVelocity(planet, timestep)
            planet.UpdateVelocity(new_velocity)
            
            new_position = simulator.GenerateNewPositions(planet, timestep)
            planet.UpdatePosition(new_position)
        return planets
        

    @staticmethod
    def GenerateAcceleration(planet1, planet2):
        """
        Input:
            Two planet instances
        Does:
            a1(t+dt) = -G*(m2/norm(r21)**3)*r21 
        returns:
            a(t+dt) (Planet 1's as a vector)
        """

        r21 = planet1.position - planet2.position # Vectors
        new_acceleration = -G*(planet2.mass)/(norm(r21)**3)*r21
        
        return new_acceleration
        

    @staticmethod
    def GenerateVelocity(planet, timestep):
        """
        Input:
            Two Planet Instances
        Does:
            v(t+dt) = v(t)+a(t)dt
        returns:
            v(t+dt) (as a vector)
        """
        new_velocity = planet.velocity + planet.acceleration*timestep
        return new_velocity

    @staticmethod
    def GenerateNewPositions(planet, timestep):
        """
        Input:
            Planet Instance
        Does:
            r(t+dt)=r(t)+v(t+dt)dt
        Returns:
            r(t+dt) (as a vector)
        """
        new_position = planet.position + planet.velocity*timestep
        return new_position
        

def main():
    return None

if __name__ == "__main__":
    main()