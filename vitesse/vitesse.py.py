"""
Calcule de la vitesse
"""

class Physique:
    def __init__(self, longueur, temps):
        self.longueur = longueur
        self.temps = temps

    def vitesse(self):
        return self.longueur / self.temps
    
physique = Physique(25, 5)

print(f"La vitesse est {physique.vitesse()}")