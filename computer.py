import copy
from math import inf

import numpy
import numpy as np


def trouve_consecutifs(i, j, joueur, grid):
    """
    Trouve les éléments consécutifs pour un joueur donné à partir d'une position (i, j) dans la grille.

    Parameters
    ----------
    i : int
        Position verticale dans la grille.
    j : int
        Position horizontale dans la grille.
    joueur : int
        Le numéro du joueur (1 ou 2).
    grid : numpy.ndarray
        La grille de jeu, un tableau 2D de taille 6x7.

    Returns
    -------
    list or int
        Une liste de listes de tuples représentant les coordonnées des éléments consécutifs trouvés, 
        ou un entier représentant une situation gagnante (-10000 ou 10000).
    """
    l = []
    l2 = []
    for nb in range(-1, 2):
        if i + nb >= 0 and i + nb < len(grid):
            for nb2 in range(-1, 2):
                if j + nb2 < len(grid[0]) and j + nb2 >= 0:  
                    if nb != 0 or nb2 != 0:
                        l2.append([(nb, nb2), grid[i + nb][j + nb2]])
                        
    for val in l2:
        nb, nb2 = val[0]
        if val[1] == joueur: 
            l.append([(i, j), (i + nb, j + nb2)])
            if i + 2 * nb >= 0 and i + 2 * nb < len(grid):
                if j + 2 * nb2 < len(grid[0]) and j + 2 * nb2 >= 0:
                    if grid[i + 2 * nb][j + 2 * nb2] == joueur:
                        l.pop()
                        l.append([(i, j), (i + nb, j + nb2), (i + 2 * nb, j + 2 * nb2)])
                        if i + 3 * nb >= 0 and i + 3 * nb < len(grid):
                            if j + 3 * nb2 < len(grid[0]) and j + 3 * nb2 >= 0:
                                if grid[i + 3 * nb][j + 3 * nb2] == joueur:
                                    if joueur == 1:
                                        return -10000
                                    else: 
                                        return 10000
    return l


def trouve_tout_les_consectifs2(grid, joueur):
    """
    Trouve tous les éléments consécutifs pour un joueur donné dans la grille.

    Parameters
    ----------
    grid : numpy.ndarray
        La grille de jeu, un tableau 2D de taille 6x7.
    joueur : int
        Le numéro du joueur (1 ou 2).

    Returns
    -------
    list or int
        Une liste de sets représentant les coordonnées des éléments consécutifs trouvés,
        ou un entier représentant une situation gagnante (-10000 ou 10000).
    """
    l = []
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == joueur:
                l_consectifs_i_j = trouve_consecutifs(i, j, joueur, grid)
                if type(l_consectifs_i_j) == list:
                    if l_consectifs_i_j != []:
                        for l_tups in l_consectifs_i_j:
                            k = 0
                            trouve = False
                            while k < len(l) and trouve == False:
                                if set(l_tups) == l[k] or set(l_tups).issubset(l[k]):
                                    trouve = True
                                    k = k - 1
                                k = k + 1
                            if k == len(l):
                                l.append(set(l_tups))
                            k = 0
                else:
                   



                    return l_consectifs_i_j
    return l


def score(grid):
    """
    Calcule le score de la grille actuelle.

    Parameters
    ----------
    grid : numpy.ndarray
        La grille de jeu, un tableau 2D de taille 6x7.

    Returns
    -------
    int
        Le score de la grille.
    """
    l_joueur = trouve_tout_les_consectifs2(grid, 1)
    l_ordi = trouve_tout_les_consectifs2(grid, 2)
    score = 0
    
    if type(l_joueur) == list:
        for se in l_joueur:
            nombre = len(se)
            if nombre == 3:
                score -= 15
            if nombre == 2:
                score -= 4
    else:
        return l_joueur
    
    if type(l_ordi) == list:    
        for se2 in l_ordi:
            nombre2 = len(se2)
            if nombre2 == 3:
                score += 100
            if nombre2 == 2:
                score += 10
    else:
        return l_ordi
    
    return score


def drop_piece(grid, colonne, piece):
    """
    Ajoute une pièce dans une colonne donnée de la grille.

    Parameters
    ----------
    grid : numpy.ndarray
        La grille de jeu, un tableau 2D de taille 6x7.
    colonne : int
        La colonne où ajouter la pièce.
    piece : int
        Le numéro de la pièce (1 pour le joueur, 2 pour l'ordinateur).

    Returns
    -------
    numpy.ndarray
        La grille mise à jour.
    """
    if grid[0, colonne] != 0:
        return numpy.zeros((2, 2))
    
    elif grid[5, colonne] == 0:
        grid[5, colonne] = piece
    else:
        for ligne in range(5):
            if grid[ligne, colonne] == 0 and grid[ligne + 1, colonne] != 0:
                grid[ligne, colonne] = piece
                break
    return grid


def create_all_childs(grid, piece):
    """
    Crée tous les enfants possibles en ajoutant une pièce dans chaque colonne.

    Parameters
    ----------
    grid : numpy.ndarray
        La grille de jeu, un tableau 2D de taille 6x7.
    piece : int
        Le numéro de la pièce (1 pour le joueur, 2 pour l'ordinateur).

    Returns
    -------
    list
        Liste des grilles enfants.
    """
    l = []
    l_originals = []
    for j in range(7):
        l_originals.append(copy.deepcopy(grid))
    for i in range(7):
        child = drop_piece(l_originals[i], i, piece)
        if child.any():
            l.append(child)
    return l


def alphabeta(node, depth, a, b, maximizingPlayer, n):
    """
    Algorithme Alpha-Beta pour déterminer le meilleur coup.

    Parameters
    ----------
    node : numpy.ndarray
        La grille de jeu actuelle.
    depth : int
        La profondeur actuelle de l'algorithme.
    a : float
        La valeur alpha pour l'élagage alpha-beta.
    b : float
        La valeur beta pour l'élagage alpha-beta.
    maximizingPlayer : bool
        True si c'est le tour du joueur maximisant, False sinon.
    n : int
        La profondeur initiale de l'algorithme.

    Returns
    -------
    int or list
        Le score de la grille ou une liste des meilleurs coups et leurs scores.
    """
    l = []
    if depth == 0 or score(node) == 10000 or score(node) == -10000:
        return score(node)
    
    if maximizingPlayer:
        value = -inf
        l_childs = create_all_childs(node, 2)
        for child in l_childs:
            value = max(value, alphabeta(child, depth - 1, a, b, False, n))
            if value > b:
                break  # β cutoff
            a = max(a, value)
            if depth == n:
                l.append((child, value))
        if depth == n:
            return l
    else:
        value = inf
        l_childs = create_all_childs(node, 1)
        for child in l_childs:
            value = min(value, alphabeta(child, depth - 1, a, b, True, n))
            if value < a:
                break  # α cutoff
            b = min(b, value)
    return value


def coup_a_jouer(l, grid):
    """
    Détermine la colonne à jouer en fonction de la liste des coups et de leurs scores.

    Parameters
    ----------
    l : list
        Liste des coups et de leurs scores.
    grid : numpy.ndarray
        La grille de jeu actuelle.

    Returns
    -------
    tuple
        La colonne à jouer et le score correspondant.
    """
    l2 = [0]
    k = 0
    max_score = -inf
    for tup in l:
        maxi = tup[1]
        if maxi > max_score:
            colone_a_jouer = l2[-1]
            max_score = maxi
        if k + 1 < 6:
            if grid[0, k + 1] != 0:
                k += 1
        k += 1
        l2.append(k)
    return (colone_a_jouer, max_score)


def check_coup_a_jouer(tup, depth, grid):
    """
    Vérifie et ajuste le coup à jouer en fonction de la profondeur et de la grille actuelle.

    Parameters
    ----------
    tup : tuple
        Le coup à jouer et le score correspondant.
    depth : int
        La profondeur initiale de l'algorithme.
    grid : numpy.ndarray
        La grille de jeu actuelle.

    Returns
    -------
    int
        La colonne à jouer.
    """
    colone, mini = tup
    i = 0
    if mini == -10000:
        while mini == -10000:
            l = alphabeta(grid, depth - i, -inf, inf, True, depth - i)
            colone, mini = coup_a_jouer(l, grid)
            i += 1
    return colone


def get_computer_play_column(difficulty, grid, is_player_red):
    """
    Renvoie la colonne jouée par l'ordinateur en fonction de la difficulté et de la grille actuelle.

    Parameters
    ----------
    difficulty : int
        La difficulté de l'ordinateur, de 1 à 4.
    grid : numpy.ndarray
        La grille actuelle contenant les pièces.
    is_player_red : bool
        Indique si le joueur est rouge.

    Returns
    -------
    int
        La colonne jouée par l'ordinateur.
    """
    l = alphabeta(grid, difficulty, -inf, inf, True, difficulty)
    x = check_coup_a_jouer(coup_a_jouer(l, grid), difficulty, grid)
    return x
