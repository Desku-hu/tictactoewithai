import os
import time
import sys
def kiiras(lista):
    print()
    for i in range(len(lista)):
        for index in range(len(lista[i])):
            if index!=len(lista[i])-1:
                print(lista[i][index], end=" | ")
            else:
                print(lista[i][index])
        if i!=2:
            print("----------")
        else:
            print()
nyert=None
def leellenorzes(lista):
    valami=None
    if lista[0][0]!=" ":
        if lista[0][0]==lista[0][1] and lista[0][0]==lista[0][2]:
            nyert=lista[0][0]
            valami=True
            print("Az", nyert, "nyert.")
            return True
        if lista[0][0]==lista[1][0] and lista[0][0]==lista[2][0]:
            nyert=lista[0][0]
            valami=True
            print("Az", nyert, "nyert.")
            return True
        if lista[0][0]==lista[1][1] and lista[0][0]==lista[2][2]:
            nyert=lista[0][0]
            valami=True
            print("Az", nyert, "nyert.")
            return True
    if lista[0][1]!=" ":
        if lista[0][1]==lista[1][1] and lista[0][1]==lista[2][1]:
            nyert=lista[0][1]
            valami=True
            print("Az", nyert, "nyert.")
            return True
    if lista[0][2]!=" ":
        if lista[0][2]==lista[1][2] and lista[0][2]==lista[2][2]:
            nyert=lista[0][2]
            valami=True
            print("Az", nyert, "nyert.")
            return True
        if lista[0][2]==lista[1][1] and lista[0][2]==lista[2][0]:
            nyert=lista[0][2]
            valami=True
            print("Az", nyert, "nyert.")
            return True
    if lista[1][0]!=" ":
        if lista[1][0]==lista[1][1] and lista[1][0]==lista[1][2]:
            nyert=lista[1][0]
            valami=True
            print("Az", nyert, "nyert.")
            return True
    if lista[2][0]!=" ":
        if lista[2][0]==lista[2][1] and lista[2][0]==lista[2][2]:
            nyert=lista[2][0]
            valami=True
            print("Az", nyert, "nyert.")
            return True
    benne=False
    for i in lista:
        ittvane=False
        for v in i:
            if v==" ":
                benne=True
    if benne==False and valami!=True:
        return 0

    
vissza=None
def jatekos():
    adatok=[[" "," "," "],[" "," "," "],[" "," "," "]]
    index=0
    xvagyy="O"
    vissza=False
    while True:
        sikeres=False
        if xvagyy=="O":
            xvagyy="X"
        elif xvagyy=="X":
            xvagyy="O"
        adat=[]
        kiiras(adatok)
        while sikeres!=True:
            try:
                jo=False
                indexe=0
                while jo!=True:
                    if indexe!=0:
                        print("Valamit nem írtál be jól. Próbáld meg újra.")
                    print("Hova rakod az", xvagyy, end="-et? ")
                    hovaxet=input("")
                    adat=[int(hovaxet[0])-1, int(hovaxet[-1])-1]
                    indexe+=1
                    if adatok[int(hovaxet[0])-1][int(hovaxet[-1])-1]==" ":
                        jo=True
                break
            except ValueError or IndexError or adatok[int(hovaxet[0])][int(hovaxet[-1])]!=" ":
                if hovaxet=="vissza":
                    vissza=True
                    break
                print("Valamit nem írtál be jól. Próbáld meg újra.")
        if vissza==True:
            os.system('cls')
            break
        adatok[adat[0]][adat[-1]]=xvagyy
        if leellenorzes(adatok)==True:
            kiiras(adatok)
            break
        elif leellenorzes(adatok)==0:
            kiiras(adatok)
            print("A meccs döntetlen lett.")
            break

def evaluate(board):
    for row in board:
        if row.count("O") == 3:
            return 10
        elif row.count("X") == 3:
            return -10

    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] == "O":
            return 10
        elif board[0][col] == board[1][col] == board[2][col] == "X":
            return -10

    if board[0][0] == board[1][1] == board[2][2] == "O" or board[0][2] == board[1][1] == board[2][0] == "O":
        return 10
    elif board[0][0] == board[1][1] == board[2][2] == "X" or board[0][2] == board[1][1] == board[2][0] == "X":
        return -10

    return 0

def minimax(board, depth, is_maximizing):
    score = evaluate(board)

    if score == 10:
        return score - depth

    if score == -10:
        return score + depth

    if " " not in [cell for row in board for cell in row]:
        return 0

    if is_maximizing:
        best = -1000
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "O"
                    best = max(best, minimax(board, depth + 1, not is_maximizing))
                    board[i][j] = " "
        return best

    else:
        best = 1000
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "X"
                    best = min(best, minimax(board, depth + 1, not is_maximizing))
                    board[i][j] = " "
        return best

def find_best_move(board):
    best_val = -1000
    best_move = (-1, -1)

    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "O"
                move_val = minimax(board, 0, False)
                board[i][j] = " "
                if move_val > best_val:
                    best_move = (i, j)
                    best_val = move_val

    return best_move

def robotresz(lista):
    move = find_best_move(lista)
    return move

def robot():
    adatok=[[" "," "," "],[" "," "," "],[" "," "," "]]
    index=0
    while True:
        xvagyy=input("Melyik betűvel akarsz lenni?(O, X) ")
        if xvagyy=="O" or xvagyy=="X":
            index=True
        if index==True:
            break
        else:
            print("Valamit rosszul írtál be. Próbáld meg újra")
    vissza=False
    while True:
        sikeres=False
        adat=[]
        kiiras(adatok)
        while sikeres!=True:
            try:
                print("Hova rakod az", xvagyy, end="-et? ")
                hovaxet=input("")
                adat=[int(hovaxet[0])-1, int(hovaxet[-1])-1]
                break
            except ValueError or IndexError:
                if hovaxet=="vissza":
                    vissza=True
                    break
                print("Valamit nem írtál be jól. Próbáld meg újra.")
        if vissza==True:
                os.system('cls')
                break
        adatok[adat[0]][adat[-1]]=xvagyy
        if leellenorzes(adatok)==True:
            kiiras(adatok)
            break
        elif leellenorzes(adatok)==0:
            kiiras(adatok)
            print("A meccs döntetlen lett.")
            break
        visszakapott=robotresz(adatok)
        if xvagyy=="X":
            adatok[int(visszakapott[0])][int(visszakapott[-1])]="O"
        elif xvagyy=="O":
            adatok[int(visszakapott[0])][int(visszakapott[-1])]="X"
        if leellenorzes(adatok)==True:
            kiiras(adatok)
            break
        elif leellenorzes(adatok)==0:
            kiiras(adatok)
            print("A meccs döntetlen lett.")
            break


szeretnelmegegyet=1
while True:
    if szeretnelmegegyet!=1 and vissza!=True:
        szeretnelmegegyet=input("Szeretnél mégegyet játszani? ")
        if szeretnelmegegyet=="nem":
            break
        os.system('cls')
    melyiketszeretned=input("Robottal játszasz? ")
    if melyiketszeretned=="igen":
        robot()
        szeretnelmegegyet=None
    elif melyiketszeretned=="nem":
        jatekos()
        szeretnelmegegyet=None
    elif melyiketszeretned=="harmadik":
        robotresz(1)