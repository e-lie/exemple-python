
couleurs_valides = ["TREFLE", "CARREAU", "COEUR", "PIQUE"]
valeurs_valides = [ str(valeur) for valeur in range(1, 11) ] + ["VALET", "DAME", "ROI"]

class Carte:
    """Represente une carte à jouer
    classique d'un jeu de 52 carte."""

    def __init__(self, valeur:str, couleur:str) -> None:
        self.valeur = valeur
        self.couleur = couleur

    def points(self) -> int:
        return couleurs_valides.index(self.valeur) + 1


if __name__ == "__main__":
    pass