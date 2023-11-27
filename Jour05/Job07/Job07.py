
note_sudents = int(input("entrée note"))

if note_sudents < 0 or note_sudents > 100:
    ValueError:print("La note doit se trouver entre 0 et 100")

elif note_sudents < 40:
   print("Échec au test")
elif note_sudents >= 40:
   print("Réussite au test")



def arrondir_note(note):
    prochain_multiple_de_5 = (note // 5 + 1) * 5
    if prochain_multiple_de_5 - note < 3:
        return prochain_multiple_de_5
    else:
        return note

print(arrondir_note(note_sudents))





