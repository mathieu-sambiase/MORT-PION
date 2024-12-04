""" interface.py
 Ce module gère tout l'affichage et l'interface utilisateur du jeu Tic Tac Toe
 Il contient les fonctions pour afficher le plateau, les menus et gérer l'écran"""

def effacer_ecran():
    """Nettoie l'écran du terminal pour une meilleure lisibilité
    Utilise les codes ANSI qui fonctionnent sur la plupart des terminaux modernes"""
    print("\033[H\033[J", end="")

def afficher_plateau(plateau):
    """Affiche le plateau de jeu avec un design ASCII art élégant
    
    Args:
        plateau (list): Une liste de 9 éléments représentant l'état du jeu
                       Chaque case contient soit 'X', 'O' ou un espace ' '
    
    Le plateau est affiché avec des bordures stylisées et une mise en page claire"""
    effacer_ecran()
    print("\n╔═══════════════════╗")
    print("║     TIC TAC TOE   ║")
    print("╚═══════════════════╝\n")
    print(f" {plateau[0]} │ {plateau[1]} │ {plateau[2]} ")
    print("───┼───┼───")
    print(f" {plateau[3]} │ {plateau[4]} │ {plateau[5]} ")
    print("───┼───┼───")
    print(f" {plateau[6]} │ {plateau[7]} │ {plateau[8]} \n")

def afficher_menu_principal():
    """Affiche le menu principal du jeu avec les différentes options disponibles
    Utilise un design encadré pour une meilleure présentation"""
    effacer_ecran()
    print("\n╔═══════════════════════════╗")
    print("║      MENU PRINCIPAL       ║")
    print("╚═══════════════════════════╝\n")
    print("1. Joueur contre Joueur")
    print("2. Joueur contre IA")
    print("3. Quitter")

def afficher_menu_difficulte():
    """Affiche le menu de sélection du niveau de difficulté pour le mode IA
    Présente les trois niveaux disponibles et l'option de retour"""
    effacer_ecran()
    print("\n╔═══════════════════════════╗")
    print("║    NIVEAU DE DIFFICULTÉ   ║")
    print("╚═══════════════════════════╝\n")
    print("1. Facile")
    print("2. Moyen")
    print("3. Difficile")
    print("4. Retour")