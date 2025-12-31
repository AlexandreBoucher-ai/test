# ici on programme l'évolution du temps

# on va utiliser la fonction sleep de time, qui suspend le programme pendant x seconde
# (lecture du programme est mis sur pause pendant x seconde)
import time

# 1 tick = une lecture de l'énoncé de la boucle for
# donc pour chaque tic, on ajoute x temps de pause avec sleep
# on définie arbitrairement 999 tics maximales pour l'instant
for i in range(999):
    # chaque tic = 1 seconde
    time.sleep(1)