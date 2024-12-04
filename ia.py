# ia.py
# Module d'intelligence artificielle pour le jeu
# Implémente l'algorithme Minimax avec élagage Alpha-Beta pour une IA optimale

import random

def evaluer_plateau(plateau, ia, humain):
    """Évalue la situation actuelle du plateau
    
    Args:
        plateau (list): État actuel du plateau
        ia (str): Symbole de l'IA ('O')
        humain (str): Symbole du joueur humain ('X')
    
    Returns:
        int: Score de l'évaluation
             1 = victoire de l'IA
            -1 = victoire du joueur
             0 = match nul ou partie en cours"""
    from logique_jeu import verifier_victoire
    if verifier_victoire(plateau, ia):
        return 1
    if verifier_victoire(plateau, humain):
        return -1
    return 0

def minimax(plateau, profondeur, est_maximisant, ia, humain, alpha, beta):
    """Implémentation de l'algorithme Minimax avec élagage Alpha-Beta
    
    Args:
        plateau (list): État actuel du plateau
        profondeur (int): Niveau de profondeur dans l'arbre de recherche
        est_maximisant (bool): True si c'est le tour de l'IA
        ia (str): Symbole de l'IA
        humain (str): Symbole du joueur
        alpha (float): Meilleur score pour le maximisant
        beta (float): Meilleur score pour le minimisant
    
    Returns:
        int: Meilleur score possible pour le joueur actuel
    
    L'élagage Alpha-Beta permet de réduire considérablement
    le nombre de branches explorées tout en garantissant
    le même résultat optimal"""
    from logique_jeu import plateau_plein, cases_disponibles
    
    score = evaluer_plateau(plateau, ia, humain)
    if score != 0:
        return score
    if plateau_plein(plateau):
        return 0
    
    if est_maximisant:
        meilleur_score = float('-inf')
        for position in cases_disponibles(plateau):
            plateau[position] = ia
            score = minimax(plateau, profondeur + 1, False, ia, humain, alpha, beta)
            plateau[position] = ' '
            meilleur_score = max(score, meilleur_score)
            alpha = max(alpha, score)
            if beta <= alpha:
                break  # Élagage Alpha
        return meilleur_score
    else:
        meilleur_score = float('inf')
        for position in cases_disponibles(plateau):
            plateau[position] = humain
            score = minimax(plateau, profondeur + 1, True, ia, humain, alpha, beta)
            plateau[position] = ' '
            meilleur_score = min(score, meilleur_score)
            beta = min(beta, score)
            if beta <= alpha:
                break  # Élagage Beta
        return meilleur_score

def mouvement_ia(plateau, difficulte, ia_symbole, joueur_symbole):
    """Détermine le prochain coup de l'IA selon le niveau de difficulté
    
    Args:
        plateau (list): État actuel du plateau
        difficulte (str): Niveau choisi ("1"=Facile, "2"=Moyen, "3"=Difficile)
        ia_symbole (str): Symbole de l'IA ('O')
        joueur_symbole (str): Symbole du joueur ('X')
    
    Returns:
        int: Position choisie par l'IA
    
    Trois niveaux de difficulté :
    - Facile : Coups complètement aléatoires
    - Moyen : 70% de coups optimaux, 30% aléatoires
    - Difficile : Toujours le meilleur coup possible"""
    from logique_jeu import cases_disponibles
    
    cases_dispo = cases_disponibles(plateau)
    
    if difficulte == "1":  # Facile
        return random.choice(cases_dispo)
    
    elif difficulte == "2":  # Moyen
        if random.random() < 0.7:  # 70% de chance de jouer intelligemment
            meilleur_score = float('-inf')
            meilleur_coup = random.choice(cases_dispo)
            
            for position in cases_dispo:
                plateau[position] = ia_symbole
                score = minimax(plateau, 0, False, ia_symbole, joueur_symbole, float('-inf'), float('inf'))
                plateau[position] = ' '
                
                if score > meilleur_score:
                    meilleur_score = score
                    meilleur_coup = position
            
            return meilleur_coup
        else:  # 30% de chance de jouer aléatoirement
            return random.choice(cases_dispo)
    
    else:  # Difficile - IA imbattable
        meilleur_score = float('-inf')
        meilleur_coup = random.choice(cases_dispo)
        
        for position in cases_dispo:
            plateau[position] = ia_symbole
            score = minimax(plateau, 0, False, ia_symbole, joueur_symbole, float('-inf'), float('inf'))
            plateau[position] = ' '
            
            if score > meilleur_score:
                meilleur_score = score
                meilleur_coup = position
        
        return meilleur_coup