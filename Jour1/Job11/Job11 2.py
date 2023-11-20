ch = input("saisir mot avec ou sans e")
cr = "e"
lc = len(ch)
i = 0
t = 0

while i < lc:
    if ch[i] == cr:
        t = 1
    i = i + 1


if t == 1:
 print("le caractère ", cr, " est présent ")

else:
 print("le caractére est introuvable" )