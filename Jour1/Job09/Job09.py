nom = "chips"
prix_unitaire = 2
quantite_en_stock = 30



print(f" produit: {nom}, prix unitaire: {prix_unitaire} , quantité en stock: {quantite_en_stock}")

QuantiteOfUsers = input(" Veuillez Saisir la quantité de produits")

ajout_produit = int(QuantiteOfUsers) + quantite_en_stock

prix = int(prix_unitaire) * int(QuantiteOfUsers)
prix_inflation = prix /100 * 10 + prix

while QuantiteOfUsers > str(quantite_en_stock):
        ajout_produit = quantite_en_stock
        break

print("Le produit est un paquet de " + nom + " le prix unitaire est de " + str(prix_unitaire) + " € ")
print("Le prix aprés inflation est de " + str(prix_inflation) + " € " + " et la quantité en stock est de " +
      str(quantite_en_stock) +
      " paquets")