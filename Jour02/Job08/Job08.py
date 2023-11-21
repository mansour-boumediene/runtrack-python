a = int(input("entrée la longueur du côté 1"))
b = int(input("entrée la longueur du côté 2"))
c = int(input("entrée la longueur du côté 3"))


if a <= b + c and b <= a + c and c <= a + b:
    print("construction d'un triangle possible")
    
else: 
    print("construction impossible, changez les valeurs ")