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


# Pour le user (et donc les input), on définit le système de coordonné
# En fait, on les simplifies, pour que le input soit de (1,1) à (9,18)
# donc on prend la matrice en argument
def coordonnés(matrice):
    pass







# maintenant on code les déplacements des ennemies

# on va utiliser la fonction sleep de time, qui suspend le programme pendant x seconde
# (lecture du programme est mis sur pause pendant x seconde)
import time

# move modifie la matrice avec le déplacement de l'ennemie
# temps est un input de int
# voir utilité de temps plus bas
# sinon, matrice est l'objet retourner par la fonction matrice
def move(matrice, temps):
        # on définie la valeur none comme valeur initile de à vider (voir après)
        àvider = None
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
                    # on remplace la position précédente par vide (si il y avait)
                    if àvider != None:
                        matrice[àvider] = ' '
                    # on place * à la nouvelle position
                    matrice[x, y] = '*'
                    # on enregistre comme la prochaine position à vider (lorsque l'énoncé if sera éxécuté à nouvea)
                    àvider = x, y
        # on retourne la matrice modifié après x temps ou après avoir parcour tout les éléments de la matrice  
        return matrice
# test
a = matrice(affichage('easy'))
b = move(a, 50)
print(b)


# on défini les conditions de défaites
# prend en argument la matrice actiuel
def loss(matrice):
        # si l'élément de la dernière ligne et de l'avant dernière colonne est un ennemie
        if matrice[-1, -2] == '*':
            return 'Loss'
        






# On défini le placement des tower

# on défini un nouvelle classe d'erreur qui sera utilisé après
class PlacementError(Exception):
    pass

# prende la matrice actuelle en argument
def place(matrice):
    # on boucle jusqu'à ce que l'énoncé try ne soulève aucune erreur
    while True:
        try:
            # on demande ce qu'on veut en entré
            x = int(input('Donner une coordonné entre 0 et 8 en x: '))
            y = int(input('Donner une coordonné entre 0 et 17 en y: '))
            # erreur si ne donnes pas dans l'intervalles
            if x < 0 or x > 8:
                raise ValueError
            if y < 0 or y > 17:
                raise ValueError
            # erreur si pas une case '-'
            if matrice[x,y] != '-':
                raise PlacementError
        except TypeError:
            print("Vous n'avez pas donner un nombre")
        except ValueError:
            print("Une de vos valeurs est hors de l'intervalle")
        except PlacementError:
            print("Vous devez choisir une case libre '-'")
        # une fois qu'aucune exception n'est soulevé
        else:
            # On place la tower au coordonné focntionnel
            matrice[x, y] = 'X'
            # mettre fin au while lorsqu'il n'y a pu d'exception
            break
    return matrice




    



# on défini comment une tower tue un enemie via des classes
import math



class Bad():
    def __init__(self):
        # De base, il n'y a aucun ennemie, donc pos est nul
        self.pos = None
    
    # pour la position de l'ennemie, on utilise la matrice actuelle
    def position(self, matrice):
        # where renvoies tout les indices de positions où il y a un *
        # where renvoies des tuples pour chaque * trouvé
        pos = numpy.where(matrice == '*')
        # attention, where retourne (array([x]), array([y])), il faut donc convertir en int
        # coords assemble dans une liste l'ensemble des pos où il y a un *
        # suffit de faire coords[0] pour avoir le premier point etc...
        coords = []
        for x, y in zip(*pos):
            coords.append((int(x), int(y)))
        return coords
# test
a = matrice(affichage('easy'))
b = move(a, 50)
c = Bad()
print(c.position(b))



class Tower():
    def __init__(self):
        # pour l'instant, on impose un range de rayon 3 à chaque tower
        self.range = 3
    # distance est la distance de l'ennemie par rapport à la tower
    def kill(self):
        pass



