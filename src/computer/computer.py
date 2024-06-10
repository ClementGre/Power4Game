import copy
from math import inf

import numpy


def trouve_consecutifs(i, j, joueur, grid):
    """
    fonction qu trouve

    Parameters
    ----------
    i : enrier
    j : entier
    joueur : entier

    grid : TYPE
        DESCRIPTION.

    Returns
    -------
    TYPE
        DESCRIPTION.

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
    l_joueur = trouve_tout_les_consectifs2(grid, 1)
    l_ordi = trouve_tout_les_consectifs2(grid, 2)
    score = 0

    if type(l_joueur) == list:
        for se in l_joueur:
            nombre = len(se)
            if nombre == 3:
                score = score - 1000
            if nombre == 2:
                score = score - 100

    else:
        return l_joueur

    if type(l_ordi) == list:
        for se2 in l_ordi:
            nombre2 = len(se2)
            if nombre2 == 3:
                score = score + 100
            if nombre2 == 2:
                score = score + 10


    else:
        return l_ordi

    return score


def drop_piece(grid, colonne, piece):
  
  if grid[0, colonne] != 0:
      return numpy.zeros((2, 2))  
  
  #Cas dernière ligne
  elif grid[5, colonne] == 0:
      grid[5,colonne] = piece
      
  
      
  #Cas autres lignes
  else: 
       for ligne in range(5):
              if grid[ligne, colonne] == 0 and grid[ligne + 1, colonne] != 0:
               grid[ligne,colonne] = piece
      
               break
       
  
  return grid


def create_all_childs(grid, piece):

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
    l = []
    if depth == 0 or score(node) == 10000 or score(node) == -10000:
        return score(node)

    if maximizingPlayer:
        value = -inf
        l_childs = create_all_childs(node, 1)
        for child in l_childs:
            value = max(value, alphabeta(child, depth - 1, a, b, False, n))

            if depth == n:
                l.append((child, value))
                # print(l[-1][0], l[-1][1])

            if value > b:
                break  # (* β cutoff *)
            a = max(a, value)

        if depth == n:
            return (l)


    else:
        value = inf
        l_childs = create_all_childs(node, 2)
        for child in l_childs:
            value = min(value, alphabeta(child, depth - 1, a, b, True, n))

            if value < a:
                break  # (* α cutoff *)
            b = min(b, value)

    return value


def coup_a_jouer(l):
    l2 = [0]
    k = 0
    mini = -inf
    
    for tup in l:
        
        score = tup[1]
        
        if score > mini:
            if l2!= []:
                colone_a_jouer = l2[-1]
                mini = score
 
    
 
        
        k = k + 1
        l2.append(k)
        
    
        
    
    return (colone_a_jouer, mini)



def check_coup_a_jouer(tup, depth, grid):
    colone, mini = tup
    i = 0

    if mini == -10000:
        while mini == -10000:
            
            #print('arrivé')
            l = alphabeta(grid, depth - i, -inf, inf, True, depth - i)
            
            #print(i, mini)
            colone, mini = coup_a_jouer(l)
            i = i + 1
    

    
    return colone



def get_computer_play_column(difficulty, grid, is_player_red):
    """Renvoie la colonne jouée par l'ordinateur en fonction de la difficulté et de la grille actuelle.
    Développé par : Elie et Maxence
    :param difficulty: La difficulté de l'ordinateur, de 1 à 4
    :type difficulty: int
    :param grid: La grille actuelle contenant
    :type grid: numpy array grid: numpy array de taille 6x7 contenant des entiers :
        0: case vide
        1: joueur rouge
        2: joueur jaune
    :return: La colonne jouée par l'ordinateur
    """

    # if is_player_red:
    #     new_grid = numpy.zeros((6, 7))
    #     for i in range(6):
    #         for j in range(7):
    #             if grid[i][j] == 1:
    #                 new_grid[i][j] = 2
    #             elif grid[i][j] == 2:
    #                 new_grid[i][j] = 1
    #     grid = new_grid

    l = alphabeta(grid, difficulty, -inf, inf, True, difficulty)
    #x = coup_a_jouer(l)
    x = check_coup_a_jouer(coup_a_jouer(l), difficulty, grid)
    print(x)
    
    print("Grid:", grid)
    print("Computer playing in:", x)
    return x
