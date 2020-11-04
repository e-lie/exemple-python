


class InvalidCardColor(ValueError):
    pass

class InvalidCardValue(ValueError):
    pass

class Carte:
    """Represente une carte à jouer
    classique d'un jeu de 52 carte."""

    couleurs_valides = ["TREFLE", "CARREAU", "COEUR", "PIQUE"]
    valeurs_valides = ["AS"] + [ str(valeur) for valeur in range(2, 11) ] + ["VALET", "DAME", "ROI"]

    def __init__(self, valeur:str, couleur:str) -> None:
        self.valeur = valeur
        if couleur not in Carte.couleurs_valides:
            raise InvalidCardColor()

        self._valeur = valeur
        self._couleur = couleur

    @property
    def valeur(self):
        self._valeur

    @valeur.setter
    def valeur(self, valeur_carte):
        if valeur_carte not in Carte.valeurs_valides:
            raise InvalidCardValue()
        self._valeur = valeur_carte

    @property
    def points(self) -> int:
        return Carte.valeurs_valides.index(self._valeur) + 1

    def __repr__(self):
        return f"<Carte {self._valeur} de {self._couleur}>"

    def __eq__(self, autre_carte):
        return self._couleur == autre_carte._couleur and self._valeur == autre_carte.valeur

    def __iter__(self):
        return IterateurDeCarte(Carte.valeurs_valides, Carte.couleurs_valides, self)


class IterateurDeCarte:

    def __init__(self, valeurs_valides, couleurs_valides, carte):
        self.valeurs_valides = valeurs_valides
        self.couleurs_valides = couleurs_valides
        self.serie_des_cartes = [Carte(valeur, couleur) for valeur in valeurs_valides
                                            for couleur in couleurs_valides]
        self.index = self.serie_des_cartes.index(carte)

    def __next__(self):
        if self.index+1 == len(self.serie_des_cartes):
            raise StopIteration
        return self.serie_des_cartes[self.index+1]

    def __iter__(self):
        return self
        


