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
        Objects.append(Planet(object))
    
    Anim = animator()
    Anim.run(Objects)

if __name__ == "__main__":
    main()