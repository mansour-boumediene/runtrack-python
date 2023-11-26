def tri_croissant(liste):

    n = 0
    while n < (taille_liste(liste) - 1):
        m = 0
        while m < (taille_liste(liste) - 1):
            if liste[m] > liste[m + 1]:

                temp = liste[m]
                liste[m] = liste[m + 1]
                liste[m + 1] = temp
            m += 1
        n += 1

def taille_liste(liste):

    taille = 0
    for _ in liste:
        taille += 1
    return taille

def arrondir_liste(liste):

    arrondis = []
    for nombre in liste:
        nombre_arrondi = int(nombre + 0.5) if nombre >= 0 else int(nombre - 0.5)
        arrondis.append(nombre_arrondi)
    return arrondis


ma_liste = [22.4, 4.0, 16.22, 9.10, 11.00, 12.22, 14.20, 5.20, 17.50]

liste_arrondie = arrondir_liste(ma_liste)

tri_croissant(liste_arrondie)

print("Liste arrondie et triée dans l'ordre croissant :", liste_arrondie)