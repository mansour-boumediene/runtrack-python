def my_liste(liste):
    taille = 0
    for _ in liste:
        taille += 1
    return taille

def tri_croissant(liste):
    n = my_liste(liste)
    for i in range(n - 1):
        indice_min = i
        for j in range(i + 1, n):
            if liste[j] < liste[indice_min]:
                indice_min = j
        liste[i], liste[indice_min] = liste[indice_min], liste[i]

    return liste

ma_liste = [124, 95, 2, 12, 191]
resultat = tri_croissant(ma_liste)
print("Liste triée dans l'ordre croissant :", resultat)
