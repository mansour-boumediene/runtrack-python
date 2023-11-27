


def calcul():
    nombre_marche = int(input("Quelle est le nombre de marche ? "))
    hauteur_marche = float(input("Quelle est l'hauteur de la marche ? ")) / 100
    c = nombre_marche * hauteur_marche
    jour = 5
    semaine = 7
    monter_descente = c * 2
    c_j = monter_descente * jour
    s_j = c_j * semaine
    return  print("Pour", nombre_marche, "nombre de marches de ", hauteur_marche,"cm, le gardien parcourt", c_j and s_j,"métre par semaine ")


print(calcul())





