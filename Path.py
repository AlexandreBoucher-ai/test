# Ici, on définit l'affichage et le path

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
                rec += '-' + '*' + '-' * 16 + '\n'

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


print(affichage('easy'))

