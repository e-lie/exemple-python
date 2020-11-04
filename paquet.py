from carte import Carte

class Paquet:

    def __init__(self):
        self._cartes = [Carte(valeur, couleur) for valeur in Carte.valeurs_valides
                        for couleur in Carte.couleurs_valides]

    def __getitem__(self, index):
        return self._cartes[index]

    def __setitem__(self, index, carte):
        self._cartes[index] = carte
    
    def __len__(self):
        return len(self._cartes)

    def __repr__(self):
        return str(self._cartes)

    def __iter__(self):
        return iter(self._cartes)