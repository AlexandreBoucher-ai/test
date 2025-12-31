# ON FAIT UN TOWER DEFENCE

# Ici, on définit l'affichage et le déplacement des énnemies
# Remarque: ici les ennemies sont définies comme des éléments de l'affichage (et n,ont comme un individu différent)

# affichage est la "map"
# difficulty = easy seulement pour l'instant
def affichage(difficulty):
    # on essaye une grille 18 par 9
    # le path est arbitraire et fix pour l'instant
    rec = ''
    # difficulty 'easy' seul disponible pour l'instant
    if difficulty == 'easy':
        for i in range(9):
            # espace vide = 2e case
            if i == 0:
                rec += '-' + ' ' + '-' * 16 + '\n'

            # espace vide = 2e case
            if i == 1:
                rec += '-' + ' ' + '-' * 16 + '\n'

            # espace vide = 2e à 9e cases
            if i == 2:
                rec += '-' + ' ' * 9 + '-' * 8 + '\n'

            # espace vide = 9e case
            if i == 3:
                rec += '-' * 9 + ' ' + '-' * 8 + '\n'

            # espace vide = 9e case
            if i == 4:
                rec += '-' * 9 + ' ' + '-' * 8 + '\n'

            # espace vide = 9e case
            if i == 5:
                rec += '-' * 9 + ' ' + '-' * 8 + '\n'

            # espace vide = 9e case
            if i == 6:
                rec += '-' * 9 + ' ' + '-' * 8 + '\n'

            # espace vide = 9e à 17e case
            if i == 7:
                rec += '-' * 9 + ' ' * 8 + '-' + '\n'

            # espace vide = 17e case
            if i == 8:
                rec += '-' * 16 + ' ' + '-' + '\n'
        return rec  
# test
print(affichage('easy'))





# on code l'affichage mais sous forme de matrice
# car c'est une forme plsu pratique pour moi
import numpy


# affichage doit être issue de la fonction affichage
def matrice(affichage):
    liste = list(affichage.replace('\n', ''))
    matrice = numpy.array(liste)
    # on veut une matrice 9 lignes et 18 colonnes (2 dimension)
    return matrice.reshape(9, 18)
#test
print(matrice(affichage('easy')))
print((matrice(affichage('easy'))[3, 4]))





# maintenant on code les déplacements des ennemies

# on va utiliser la fonction sleep de time, qui suspend le programme pendant x seconde
# (lecture du programme est mis sur pause pendant x seconde)
import time

# move modifie la matrice avec le déplacement de l'ennemie
# temps est un input de int
# voir utilité de temps plus bas
# sinon, matrice est l'objet retourner par la fonction matrice
def move(matrice ,temps):
        # en même temps qu'on code le déplacement, on code le temps entre chaque move dans cette fonction
        # 1 tick = à chaque fois que l'énoncé if de la boucle est lu
        # donc pour chaque tic, on ajoute x temps de pause avec sleep
        # remarque: chaque tic est un déplacement, et non juste une lecture de la boucle
        # np.shape retourne les dimension de la matrice (pour easy, 9 par 18)
        for x, y in numpy.ndindex(matrice.shape):
            # temps permet de faire un nb arbitraire d'itération
            # si temps > nb d'élément dans la matrice, alors
            # l'itération sera arrêter lorsqu'on aura parcouru tout les élément de la matrice
            if temps >= 0:
                temps = temps - 1
                if matrice[x, y] == ' ':
                    # si c'est un espace vide et donc qu'il y a un déplacement,
                    # on rajoute donc un délai de 1 seconde (0.01 pour les tests temporaires)
                    time.sleep(0.01)
                    # * représente l'énemie
                    matrice[x, y] = '*'
        # on retourne la matrice modifié après x temps ou après avoir parcour tout les éléments de la matrice  
        return matrice
# test
a = matrice(affichage('easy'))
b = move(a, 999)
print(b)