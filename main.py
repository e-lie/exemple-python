from carte import Carte
from paquet import Paquet
from random import shuffle

carte1 = Carte("AS", "TREFLE")
# carte1.valeur = "truc"
print(carte1.points)
print(carte1)


paquet = Paquet()
print(paquet)

shuffle(paquet)

for carte in Carte("AS", "CARREAU"):
    print(carte)