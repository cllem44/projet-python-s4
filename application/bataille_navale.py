from tkinter import *
from random import randint

def creer_Grille():
    return[['~' for _ in range(8)]for _ in range (8)]

#grille=creer_Grille()

def afficher_Grille(grille):
    for ligne in grille:
        for val in ligne:
            print(val,end=' ')
        print()
        
def placerBateaux2():
    choice = randint(0,1)  #0 horizontal/1 vertical
    bateaux2 = []
    if choice==0:
        x = randint(0,7)
        y = randint(0,6)
        bateaux2.append([x,y])
        bateaux2.append([x,y+1])
    else:
        x = randint(0,6)
        y = randint(0,7)
        bateaux2.append([x,y])
        bateaux2.append([x,y+1])
    return bateaux2

def placerBateaux3():
    choice = randint(0,1)
    bateaux3 = []
    if choice==0:
        x = randint(0,7)
        y = randint(0,5)
        bateaux3.append([x,y])
        bateaux3.append([x,y+1])
        bateaux3.append([x,y+2])
        
    else:
        x = randint(0,5)
        y = randint(0,7)
        bateaux3.append([x,y])
        bateaux3.append([x+1,y])
        bateaux3.append([x+2,y])
    return bateaux3

def placerBateaux4():
    choice = randint(0,1)
    bateaux4 = []
    if choice==0:
        x = randint(0,7)
        y = randint(0,4)
        bateaux4.append([x,y])
        bateaux4.append([x,y+1])
        bateaux4.append([x,y+2])
        bateaux4.append([x,y+3])
        
    else:
        x = randint(0,4)
        y = randint(0,7)
        bateaux4.append([x,y])
        bateaux4.append([x+1,y])
        bateaux4.append([x+2,y])
        bateaux4.append([x+3,y])
    return bateaux4

#b2=placerBateaux2()
#b3=placerBateaux3()
#b4=placerBateaux4()

def verifierBateaux(bateaux2,bateaux3,bateaux4):
    chevauche = True
    while chevauche:
        chevauche = False
        for val in bateaux4:
            if val in list(bateaux2) or val in list(bateaux3):
                bateaux4 = list(placerBateaux4())
                chevauche = True
                break
    chevauche = True
    while chevauche:
        chevauche = False
        for val in bateaux3:
            if val in list(bateaux2) or val in list(bateaux4):
                bateaux3 = list(placerBateaux3())
                chevauche = True
                break
    return bateaux2,bateaux3,bateaux4
    

#bateaux = verifierBateaux(b2,b3,b4)
#dicBateaux = {'Bateaux2':bateaux[0],'Bateaux3':bateaux[1],'Bateaux4':bateaux[2]}

def estCoule(bateau,grille):
    return all(grille[x][y]=='+' for x,y in bateau)

def verifierTir(tir,grille,dicBateaux):
    for bateau in dicBateaux.values():
        if tir in bateau:
            if grille[tir[0]][tir[1]]=='+':
                return 'Déjà touché'
            
            elif estCoule(bateau,grille):
                return 'Coulé'
            else:
                grille[tir[0]][tir[1]] = '+'
                return 'Touché'
            
    grille[tir[0]][tir[1]] = 'o'
    return 'Raté'

grille = creer_Grille()


bateaux2_1 = placerBateaux2()
bateaux3_1 = placerBateaux3()
bateaux4_1 = placerBateaux4()
bateaux_1 = verifierBateaux(bateaux2_1,bateaux3_1,bateaux4_1)
bateaux2_1 = bateaux_1[0]
bateaux3_1 = bateaux_1[1]
bateaux4_1 = bateaux_1[2]
dicBateaux_1 = {'bateaux2':bateaux2_1,'bateaux3':bateaux3_1,'bateaux4':bateaux4_1}
boutons = []


#----Interface-----

fenetre = Tk()
fenetre.title("MAP")
fenetre.iconbitmap("img/logo.ico")
fenetre.geometry("400x640")
fenetre.config(background="#000000")

Frame_Princ = Frame(fenetre,background="#000000")
Frame_Princ.pack()

Frame_Button = Frame(Frame_Princ,background='#000000')
Frame_Button.pack(anchor='center')

label_info = Label(Frame_Princ,background="#000000",fg = "white",font=("Calibri", 12,"bold"))
label_info.pack(anchor='center')


for i in range(8):
    ligne = []
    for j in range(8):
        b=Button(Frame_Button,text='~',bg='black',fg='white',width=4,height=2,command=lambda x=i,y=j:tirerCase(x,y))
        b.grid(row=i,column=j)
        ligne.append(b)
    boutons.append(ligne)

def tirerCase(x,y):
    tir = [x,y]
    resultat = verifierTir(tir,grille,dicBateaux_1)
    if resultat=='Touché':
        boutons[x][y].config(text='+',bg='red')
        label_info.config(text='Touché')

    elif resultat=='Raté':
        boutons[x][y].config(text='o',bg='blue')
        label_info.config(text='Raté')

    elif resultat=='Déjà touché':
        boutons[x][y].config(bg='orange')
        label_info.config(text='Déjà touché')

    elif resultat=='Coulé':
        boutons[x][y].config(text='+',bg='green')
        label_info.config(text='Coulé')


fenetre.mainloop()

"""Faire une mémoire des scores, choix d'un jeux à un ou deux joueurs, nombre de coups limité, changer le designs des boutons"""