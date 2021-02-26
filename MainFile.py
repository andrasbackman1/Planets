import csv
from Simulation import simulator
from Animate import animator
from PlanetObj import Planet

def main():
    names = []
    planet = input("Enter planet: ")    
    while planet != "":
        names.append(planet)
        planet = input("Enter another planet (press enter to continue): ")
    
    Objects = []
    for object in names:
        Objects.append(Planet(object)) # Creates list of type planet object with a pointer
    
    Anim = animator()
    simulator.Iterator(Objects, 300)
    Anim.run(Objects)

if __name__ == "__main__":
    main()