def moyenne():
    note1 = input("saisisez la premiéres note")
    note2 = input("saisisez la seconde note")
    note3 = input("saisisez la troisieme note")

    result = float(note1) + float(note2) + float(note3)
    division = result / 3

    moyenne_etudiant = division

    if moyenne_etudiant >= 15 and moyenne_etudiant <= 20:
        print("Trés bon élève")
    elif moyenne_etudiant <=14 and moyenne_etudiant >=11:
        print("Bon élève")
    elif moyenne_etudiant >=8 and moyenne_etudiant <=10:
        print("Élève moyen")
    elif moyenne_etudiant >=0 and moyenne_etudiant <=7:
        print("Élève devant faires des efforts")
    return moyenne_etudiant


print(moyenne())

