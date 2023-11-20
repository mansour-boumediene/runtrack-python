investisement_Initial = int(input(" Montant a investir "))

Calc_Taux = float(input("taux"))

Taux_Rendement_Annuel = (investisement_Initial) /100 * float(Calc_Taux) + (investisement_Initial)

Augmentation_Montant = (investisement_Initial) + 5000

Augmentation_Rendement = Taux_Rendement_Annuel /100 * 20

diminuTion_rendement = Augmentation_Rendement *10 /100

print(Taux_Rendement_Annuel)
print(Augmentation_Montant)
print(Augmentation_Rendement)
print(diminuTion_rendement)