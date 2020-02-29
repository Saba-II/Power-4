def graphics():
    print('===========================================================')
    print('')
    print('                      Puissance 4')
    print('                       + Made +')
    print('                          By   ')
    print('           Dimitri + Tristan + Yaël + Yoann ')
    print('')
    print('===========================================================')
    print('')
    print('')

def grille_vide():
    Gril = [[0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0]]
    return Gril

def affiche(gril) :
    for lig in gril :
        for i in lig :
            if i == 0 :
                print("|.",end="")
            if i == 1 :
                print("|X",end="")
            if i == 2 :
                print("|0",end="")
        print("|")

def match_nul(gril):
    result = 0
    for i in range(6):
        if gril[0][i] == 0 :
            result += 1
    if result != 0 :
        return "False"
    elif result == 0 :
        return "True"

def coup_possible(gril, col):
    for i in gril :
        if i[col] == 0 :
            return "True"
        else :
            return "False"

def diag_bas(gril, j, lig, col):
    result = 0
    for i in range(3):
        if gril[lig+i][col-i] == j:
            result += 1
    if result >= 4:
        return "True"
    else:
        return "False"

def diag_haut(gril, j, lig, col):
    result=0
    for i in range(3):
        if gril[lig+i][col+i]==j:
            result+=1
    if result>=4:
        return "True"
    else:
        return "False"

def victoire(gril, j, lig, col):
    if lig < 2 and col < 6 :
        if diag_bas(gril, j, lig, col) == "True" or diag_haut(gril, j, lig, col) == "True" or vert(gril, j, lig, col) == "True":
            return "True"
    elif lig < 5 and col < 3:
        if horiz(gril, j, lig, col) == "True":
            return "True"
    else:
        return "False"

def jouer(gril, j, col):
    lig = 0
    if coup_possible(gril, col) == "True":
        for i in range(6):
            if gril[5 - i][col] == 0:
                gril[5 - i][col] = j
                lig = 5 - i
                if victoire(gril, j, lig, col) == "True":
                    return affiche(gril)
                else:
                    return gril
    elif match_nul(gril) == "True":
        return "Match nul.", affiche(gril)

def vert(gril, j, lig, col):
    result = 0
    for i in range(3):
        if gril[lig+i][col] == j:
            result += 1
    if result>=4 :
        return "True"
    else:
        return "False"

def horiz(gril, j, lig, col):
    result=0
    for i in range(3):
        if gril[lig][col+i]==j:
            result+=1
    if result>=4:
        return "True"
    else:
        return "False"
horiz(grille_vide(), 1, 3, 0)

def ui(gril):
    n_col = "|0|1|2|3|4|5|6|"
    print(n_col)
    print("...............")
    affiche(gril)
    print("---------------")

def power4():
    graphics()
    ui(grille_vide())
    run = True
    y = grille_vide()
    while run == True :
        c1 = int(input("Joueur 1 > "))
        c2 = int(input("Joueur 2 > "))
        x = jouer(y, 1, c1)
        y = jouer(x, 2, c2)
        ui(x)
power4()
