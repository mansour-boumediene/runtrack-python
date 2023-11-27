def new_letter(lettre, clef):
    numbers = ord(lettre) + clef
    if numbers > 122:
        numbers -= 26
    return chr(numbers)

def cesar(message, clef):
    chiffrage = ""
    for lettre in message:
        if lettre == " ":
            chiffrage += " "
        else: chiffrage += new_letter(lettre, clef)
    return chiffrage

message = str(input("Entrée votre message "))
clef = int(input("Entrée votre clef"))

print(cesar(message, clef))



