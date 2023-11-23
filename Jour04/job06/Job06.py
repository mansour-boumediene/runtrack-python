L = [1, 2, 3, 4, 5]
print(L)
l = len(L)
aux = L[0]
L[0] = L[l-1]
L[l-1] = aux
print (L)