import random

# Création de la grille 3x3
def creer_grille():
    return [[' ' for _ in range(3)] for _ in range(3)]

def afficher_grille(grille):
    for ligne in grille:
        print(" | ".join(ligne))
        print("-" * 9)

def convertir_en_coordonnees(nombre):
    nombre -= 1
    return nombre // 3, nombre % 3

def est_vide(grille, ligne, colonne):
    return grille[ligne][colonne] == ' '

def jouer_coup(grille, ligne, colonne, symbole):
    if est_vide(grille, ligne, colonne):
        grille[ligne][colonne] = symbole
        return True
    return False

def verifier_victoire(grille, symbole):
    return any(all(cell == symbole for cell in ligne) for ligne in grille) or \
           any(all(grille[i][col] == symbole for i in range(3)) for col in range(3)) or \
           all(grille[i][i] == symbole for i in range(3)) or \
           all(grille[i][2 - i] == symbole for i in range(3))

def est_plein(grille):
    return all(cell != ' ' for ligne in grille for cell in ligne)

def ia_jouer_coup(grille, symbole):
    coups_possibles = [(i, j) for i in range(3) for j in range(3) if est_vide(grille, i, j)]
    if coups_possibles:
        ligne, colonne = random.choice(coups_possibles)
        jouer_coup(grille, ligne, colonne, symbole)

def joueur_contre_joueur(grille):
    joueur_actuel = 'X'
    while True:
        afficher_grille(grille)
        choix = input(f"Joueur {joueur_actuel}, choisissez un nombre entre 1 et 9 : ")
        if not choix.isdigit() or not (1 <= int(choix) <= 9):
            print("Veuillez entrer un nombre valide entre 1 et 9.")
            continue
        ligne, colonne = convertir_en_coordonnees(int(choix))
        if jouer_coup(grille, ligne, colonne, joueur_actuel):
            if verifier_victoire(grille, joueur_actuel):
                afficher_grille(grille)
                print(f"Félicitations, joueur {joueur_actuel} a gagné !")
                break
            elif est_plein(grille):
                afficher_grille(grille)
                print("Le jeu est un match nul !")
                break
            joueur_actuel = 'O' if joueur_actuel == 'X' else 'X'
        else:
            print("La case est déjà occupée. Veuillez choisir une autre case.")

def joueur_contre_ia(grille):
    joueur = 'X'
    ia = 'O'
    while True:
        afficher_grille(grille)
        if joueur == 'X':
            choix = input(f"Joueur {joueur}, choisissez un nombre entre 1 et 9 : ")
            if not choix.isdigit() or not (1 <= int(choix) <= 9):
                print("Veuillez entrer un nombre valide entre 1 et 9.")
                continue
            ligne, colonne = convertir_en_coordonnees(int(choix))
            if jouer_coup(grille, ligne, colonne, joueur):
                if verifier_victoire(grille, joueur):
                    afficher_grille(grille)
                    print("Félicitations, vous avez gagné !")
                    break
                elif est_plein(grille):
                    afficher_grille(grille)
                    print("Le jeu est un match nul !")
                    break
                joueur, ia = ia, joueur
            else:
                print("La case est déjà occupée. Veuillez choisir une autre case.")
        else:
            ia_jouer_coup(grille, ia)
            if verifier_victoire(grille, ia):
                afficher_grille(grille)
                print("L'IA a gagné, vous avez perdu !")
                break
            elif est_plein(grille):
                afficher_grille(grille)
                print("Le jeu est un match nul !")
                break
            joueur, ia = ia, joueur

def menu():
    grille = creer_grille()
    while True:
        choix = input("Choisissez le mode de jeu : 1 pour Joueur contre Joueur, 2 pour Joueur contre IA, 0 pour quitter : ")
        if choix == '1':
            joueur_contre_joueur(grille)
            break
        elif choix == '2':
            joueur_contre_ia(grille)
            break
        elif choix == '0':
            print("Merci d'avoir joué !")
            break
        else:
            print("Choix invalide, veuillez réessayer.")

if __name__ == "__main__":
    menu()
