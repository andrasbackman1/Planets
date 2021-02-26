import csv
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from Simulation import simulator
from PlanetObj import Planet
"""
Data is updated continously with the animation

"""

class animator():
    """
    Attributes:
        Timesteps

    Methods:
        Constructor
        init(self)
        GenerateInitialState
        run
    """
    def __init__(self):
        with open("SimulationParameters.csv", "r") as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == "Timesteps":
                    self.timesteps = row[1]
                elif row[0] == "Timestep":
                    self.timestep = row[1]

        

    def init(self):
        """
        Does:
            not sure
        Returns:
            self.patches
        """
        return self.patches

    def GenerateInitialState(self, _):
        """
        Inputs:
            Planets Initial Positions
        Returns:
            patches (as an iterable)
        """
        Patches = []
        for planet in planets:
            Patches.append(plt.Circle((planet.position[0], planet.position[1]), 300000, color = "r", animated = True))
        
        return Patches

    def animate(self, planets):
        print(planets)
        UpdatedPlanets = simulator.UpdatePositions(planets, self.timesteps)
        
        for i in range(len(UpdatedPlanets)):
            planetPosition = UpdatedPlanets[i].position
            patch = self.patches[i]
            patch.center = (planetPosition[0], planetPosition[1])
        
        return self.patches 
        

    def run(self, planets):
        """
        Input:
            self
        Does:
            creates the figure/axes
            calls on GenerateInitial State

            calls for FuncAnimation
            with simulation.iterate method
        """
        fig = plt.figure()
        ax = plt.axes()

        self.patches = self.GenerateInitialState(planets)

        for patch in self.patches:
            ax.add_patch(patch)
        
        #Axes setup
        ax.axis("scaled")
        ax.set_xlim(-10**7, 10**7)
        ax.set_ylim(-10**7, 10**7)

        anim = FuncAnimation(fig, self.animate, init_func = self.init, frames = self.timesteps,
                             repeat = True, interval = 50, blit = True)

        plt.show()


