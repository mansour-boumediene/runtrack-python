def triangle(taille):
    for i in range(taille):
        spaces = ' ' * (taille - i - 1)

        if i == 0:
         print(spaces + '_')
        elif i == taille - 1:
            print('/' + '_' * (2 * i) + '\\')
        else:
            print(spaces + '/' + ' ' * (2 * i) + '\\')

height = int(input("Entrez la hauteur du triangle : "))

triangle(height)





