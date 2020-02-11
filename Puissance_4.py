def grille_vide():
    Gril = [[0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0]]
    return Gril

def affiche(gril):
    for lig in gril:
        for i in lig:
            if i==0:
                print("|.",end="")
            if i==1:
                print("|X",end="")
            if i==2:
                print("|0",end="")
        print("|")

affiche(grille_vide())
