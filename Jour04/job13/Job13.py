my_liste = [10, 20, 30, 40, 40, 30, 20, 10, 60, 60, 70]

def delete_doublons(liste):
    liste_sans_doublons = []
    for element in liste:
        if element not in liste_sans_doublons:
            liste_sans_doublons.append(element)
    return liste_sans_doublons

resultat = delete_doublons(my_liste)
print("Liste sans doublons :", resultat)
