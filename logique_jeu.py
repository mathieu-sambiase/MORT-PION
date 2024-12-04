# logique_jeu.py
# Ce module contient toutes les fonctions essentielles pour la logique du jeu
# Il gère les règles, les mouvements et la validation du jeu

def verifier_victoire(plateau, joueur):
    """Vérifie si un joueur a gagné la partie
    
    Args:
        plateau (list): État actuel du plateau de jeu
        joueur (str): Symbole du joueur ('X' ou 'O')
    
    Returns:
        bool: True si le joueur a gagné, False sinon
    
    Vérifie toutes les combinaisons gagnantes possibles :
    - 3 lignes horizontales
    - 3 lignes verticales
    - 2 diagonales"""
    combinaisons = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # horizontales
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # verticales
        [0, 4, 8], [2, 4, 6]              # diagonales
    ]
    return any(all(plateau[i] == joueur for i in combo) for combo in combinaisons)

def plateau_plein(plateau):
    """Vérifie si le plateau est complètement rempli (match nul)
    
    Args:
        plateau (list): État actuel du plateau
    
    Returns:
        bool: True si aucune case n'est vide, False sinon"""
    return ' ' not in plateau

def cases_disponibles(plateau):
    """Identifie toutes les cases encore jouables
    
    Args:
        plateau (list): État actuel du plateau
    
    Returns:
        list: Liste des indices des cases vides
    
    Utilise une compréhension de liste pour plus d'efficacité"""
    return [i for i, case in enumerate(plateau) if case == ' ']

def mouvement_joueur(plateau, nom):
    """Gère la saisie et la validation du coup d'un joueur
    
    Args:
        plateau (list): État actuel du plateau
        nom (str): Nom du joueur actuel
    
    Returns:
        int: Position valide choisie par le joueur (0-8)
    
    Inclut la gestion des erreurs pour les entrées invalides"""
    while True:
        try:
            position = int(input(f"{nom}, choisissez une case (1-9): ")) - 1
            if 0 <= position <= 8 and plateau[position] == ' ':
                return position
            print("Case invalide ou déjà occupée. Réessayez.")
        except ValueError:
            print("Veuillez entrer un nombre entre 1 et 9.")