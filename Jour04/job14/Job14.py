def est_separateur(c):
    separateurs = [' ', ',', '.']
    return c in separateurs

def my_long_word(longueur, chaine):
    mot_actuel = ''
    mots_long = ''
    longueur_actuelle = 0

    for caractere in chaine:
        if not est_separateur(caractere):
            mot_actuel += caractere
            longueur_actuelle += 1
        else:
            if longueur_actuelle > longueur:
                mots_long += mot_actuel + ' '
            mot_actuel = ''
            longueur_actuelle = 0

    # Vérifie le dernier mot si la phrase ne se termine pas par un séparateur
    if longueur_actuelle > longueur:
        mots_long += mot_actuel

    return mots_long

resultat = my_long_word(5, "La peur est le chemin vers le côté obscur, la peur mène à la colère, la colère mène à la haine, la haine mène à la souffrance")
print("Output :", resultat)