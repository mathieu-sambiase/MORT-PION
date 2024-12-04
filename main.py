# main.py
# Point d'entrée principal du jeu Tic Tac Toe
# Coordonne les différents modules et gère le flux du jeu

import time
from interface import *
from logique_jeu import *
from ia import mouvement_ia

def mode_deux_joueurs():
    """Gère une partie entre deux joueurs humains
    
    Permet à deux joueurs de s'affronter en alternant les tours
    Le premier joueur utilise 'X' et le second 'O'"""
    plateau = [' '] * 9
    joueur1 = input("\nNom du Joueur 1 (X): ")
    joueur2 = input("Nom du Joueur 2 (O): ")
    tour = 0
    
    while True:
        afficher_plateau(plateau)
        joueur_actuel = joueur1 if tour % 2 == 0 else joueur2
        symbole = 'X' if tour % 2 == 0 else 'O'
        
        position = mouvement_joueur(plateau, joueur_actuel)
        plateau[position] = symbole
        
        if verifier_victoire(plateau, symbole):
            afficher_plateau(plateau)
            print(f"\nFélicitations {joueur_actuel} ! Vous avez gagné ! 🎉")
            break
            
        if plateau_plein(plateau):
            afficher_plateau(plateau)
            print("\nMatch nul ! 🤝")
            break
            
        tour += 1
    
    input("\nAppuyez sur Entrée pour continuer...")

def mode_ia():
    """Gère une partie contre l'ordinateur
    
    Permet au joueur d'affronter l'IA avec trois niveaux de difficulté
    Le joueur utilise toujours 'X' et l'IA utilise 'O'"""
    while True:
        afficher_menu_difficulte()
        difficulte = input("\nChoisissez le niveau (1-4): ")
        
        if difficulte in ["1", "2", "3"]:
            plateau = [' '] * 9
            nom_joueur = input("\nVotre nom: ")
            
            while True:
                afficher_plateau(plateau)
                
                # Tour du joueur humain
                position = mouvement_joueur(plateau, nom_joueur)
                plateau[position] = 'X'
                
                if verifier_victoire(plateau, 'X'):
                    afficher_plateau(plateau)
                    print(f"\nFélicitations {nom_joueur} ! Vous avez gagné ! 🎉")
                    break
                
                if plateau_plein(plateau):
                    afficher_plateau(plateau)
                    print("\nMatch nul ! 🤝")
                    break
                
                # Tour de l'IA
                print("\nL'IA réfléchit...")
                time.sleep(0.5)  # Pause pour simuler la réflexion
                position = mouvement_ia(plateau, difficulte, 'O', 'X')
                plateau[position] = 'O'
                
                if verifier_victoire(plateau, 'O'):
                    afficher_plateau(plateau)
                    print("\nL'IA a gagné ! 🤖")
                    break
                
                if plateau_plein(plateau):
                    afficher_plateau(plateau)
                    print("\nMatch nul ! 🤝")
                    break
            
            input("\nAppuyez sur Entrée pour continuer...")
            break
        
        elif difficulte == "4":
            break
        
        else:
            print("Choix invalide. Veuillez réessayer.")
            time.sleep(1)

def jouer():
    """Fonction principale qui lance le jeu
    
    Gère la boucle principale du jeu et le menu de sélection
    Permet de choisir entre les différents modes de jeu"""
    while True:
        afficher_menu_principal()
        choix = input("\nVotre choix (1-3): ")
        
        if choix == "1":
            mode_deux_joueurs()
        elif choix == "2":
            mode_ia()
        elif choix == "3":
            print("\nMerci d'avoir joué ! Au revoir !")
            break
        else:
            print("Choix invalide. Veuillez réessayer.")
            time.sleep(1)

if __name__ == "__main__":
    jouer()