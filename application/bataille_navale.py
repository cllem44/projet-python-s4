from tkinter import *
from random import randint

#Créer la grille de jeu
def creer_Grille():
    return[['~' for _ in range(8)]for _ in range (8)]

#Place les bateaux avec des coordonnées x et y
def placer_bateaux(taille):
    choice = randint(0,1)
    bateau = []

    if choice == 0:
        x = randint(0,7)
        y = randint(0,7-taille+1)
        for i in range(taille):
            bateau.append([x,y+i])
    else:
        x = randint(0,7-taille+1)
        y = randint(0,7)

        for i in range (taille):
            bateau.append([x+i,y])
    
    return bateau

#Vérifie si les bateaux se chevauchent ou non puis les replace en tant qu'il se chevauchent
def verifierBateaux(bateaux2,bateaux3,bateaux4):
    chevauche = True
    while chevauche:
        chevauche = False
        for val in bateaux3:
            if val in bateaux2:
                bateaux3 = placer_bateaux(3)
                chevauche = True
                break

    chevauche = True
    while chevauche:
        chevauche = False
        for val in bateaux4:
            if val in bateaux2 or val in bateaux3:
                bateaux4 = placer_bateaux(4)
                chevauche = True
                break

    return bateaux2,bateaux3,bateaux4


def estCoule(bateau,grille):
    return all(grille[x][y]=='+' for x,y in bateau)

def verifierTir(tir,grille,dicBateaux,boutons):
    for bateau in dicBateaux.values():
        if tir in bateau:              
            grille[tir[0]][tir[1]] = '+'
            if estCoule(bateau,grille):
                for val in bateau:
                    boutons [val[0]][val[1]].config(text='',bg='green')
                return 'Coulé'
            else:
                return 'Touché'
            
    grille[tir[0]][tir[1]] = 'o'
    return 'Raté'

def tirerCase(x,y,boutons):
    tir = [x,y]
    resultat = verifierTir(tir,grille,dicBateaux_1,boutons)
    couleurs = {'Touché':('+','red'),'Raté':('o','blue'),'Coulé':('','green')}

    texte,couleur = couleurs[resultat]
    boutons[x][y].config(text=texte,bg=couleur)

    label_info.config(text=resultat)

def tirer_case_duo(x,y,boutons,grille_cible,dicBateaux_cible):
    global tour_joueur

    tir = [x,y]

    if grille_cible[x][y] != '~':
        return
    
    resultat = verifierTir(tir,grille_cible,dicBateaux_cible,boutons)
    couleurs = {'Touché':('+','red'),'Raté':('o','blue'),'Coulé':('','green')}
    texte,couleur = couleurs[resultat]
    boutons[x][y].config(text=texte,bg=couleur)

    if tour_joueur == 1:
        tour_joueur = 2
        label_info.config(text=f'Résultat:{resultat}--Tour du joueur 2')
        label_tour.config(text='Tour du joueur 2')
        changer_grille_active(boutons_J1,boutons_J2,activer_J2 = True)

    else:
        tour_joueur = 1
        label_info.config(text=f'Résultat:{resultat}--Tour du joueur 1')
        label_tour.config(text='Tour du joueur 1')
        changer_grille_active(boutons_J1,boutons_J2,activer_J2 = False)
    
def changer_grille_active(boutons_J1,boutons_J2,activer_J2):
    for ligne in boutons_J1:
        for b in ligne:
            b.config(state=NORMAL if activer_J2 else DISABLED)
    
    for ligne in boutons_J2:
        for b in ligne:
            b.config(state=DISABLED if activer_J2 else NORMAL)



def creer_plateaux_boutons(frame):
    boutons = []
    for i in range(8):
        ligne = []
        for j in range(8):
            b=Button(frame,text='~',bg='black',fg='white',width=4,height=2,command=lambda x=i,y=j:tirerCase(x,y,boutons))
            b.grid(row=i,column=j)
            ligne.append(b)
        boutons.append(ligne)
    return boutons


def creer_plateaux_boutons_duo(frame,grille_cible,dicBateaux_cible):
    boutons = []
    for i in range(8):
        ligne = []
        for j in range(8):
            b=Button(frame,text='~',bg='black',fg='white',width=4,height=2,command=lambda x=i,y=j,g=grille_cible,d=dicBateaux_cible,bref=[]:tirer_case_duo(x,y,boutons,g,d))
            b.grid(row=i,column=j)
            ligne.append(b)
        boutons.append(ligne)
    return boutons


def choix_nb_joueur():
    global nb_joueur

    nb_joueur = choix.get()

    if nb_joueur == 'SOLO':
        Frame_Bienvenue.destroy()

        Frame_Button = Frame(Frame_Princ,background='#000000')
        Frame_Button.grid(row=1,column=1)

        boutons = creer_plateaux_boutons(Frame_Button)
 
        jeu_solo()
    
    else:
        Frame_Bienvenue.destroy()
        jeu_duo()

def jeu_solo():
    global grille,dicBateaux_1
    grille = creer_Grille()
    bateaux2_1 = placer_bateaux(2)
    bateaux3_1 = placer_bateaux(3)
    bateaux4_1 = placer_bateaux(4)
    bateaux_1 = verifierBateaux(bateaux2_1,bateaux3_1,bateaux4_1)
    dicBateaux_1 = {'bateaux2':bateaux_1[0],'bateaux3':bateaux_1[1],'bateaux4':bateaux_1[2]}


def jeu_duo():
    global grille_J1,grille_J2,dicBateaux_J1,dicBateaux_J2
    global boutons_J1,boutons_J2,tour_joueur,label_tour

    tour_joueur = 1

    grille_J1 = creer_Grille()
    grille_J2 = creer_Grille()

    bateau2_J1 = placer_bateaux(2)
    bateau3_J1 = placer_bateaux(3)
    bateau4_J1 = placer_bateaux(4)
    bateaux_J1 = verifierBateaux(bateau2_J1,bateau3_J1,bateau4_J1)
    dicBateaux_J1 = {'bateaux2':bateaux_J1[0],'bateaux3':bateaux_J1[1],'bateaux4':bateaux_J1[2]}

    bateau2_J2 = placer_bateaux(2)
    bateau3_J2 = placer_bateaux(3)
    bateau4_J2 = placer_bateaux(4)
    bateaux_J2 = verifierBateaux(bateau2_J2,bateau3_J2,bateau4_J2)
    dicBateaux_J2 = {'bateaux2':bateaux_J2[0],'bateaux3':bateaux_J2[1],'bateaux4':bateaux_J2[2]}

    label_tour = Label(Frame_Princ, text='Tour du Joueur 1',background='#000000', fg='yellow', font=("Calibri", 12, "bold"))
    label_tour.grid(row=0,column=1)

    label_J1 = Label(Frame_Princ, text='Grille Joueur 1', background='#000000',fg='cyan', font=("Calibri", 10, "bold"))
    label_J1.grid(row=1, column=1)

    Frame_Button_J1 = Frame(Frame_Princ, background='#000000')
    Frame_Button_J1.grid(row=2, column=1)

    label_J2 = Label(Frame_Princ, text='Grille Joueur 2', background='#000000',fg='orange', font=("Calibri", 10, "bold"))
    label_J2.grid(row=3, column=1)

    Frame_Button_J2 = Frame(Frame_Princ, background='#000000')
    Frame_Button_J2.grid(row=4, column=1)

    boutons_J1 = creer_plateaux_boutons_duo(Frame_Button_J1, grille_J1, dicBateaux_J1)
    boutons_J2 = creer_plateaux_boutons_duo(Frame_Button_J2, grille_J2, dicBateaux_J2)

    changer_grille_active(boutons_J1, boutons_J2, activer_J2=False)

#----Interface-----

fenetre = Tk()
fenetre.title("MAP")
fenetre.iconbitmap("img/logo.ico")
fenetre.geometry("400x640")
fenetre.config(background="#000000")

Frame_Princ = Frame(fenetre,background="#000000")
Frame_Princ.pack()

Frame_Bienvenue = Frame(Frame_Princ,background="#000000")
Frame_Bienvenue.grid(row=2,column=1)

label_bienvenue = Label(Frame_Bienvenue,background="black",fg = "blue",font=("Calibri", 15,"bold"))
label_bienvenue.config(text='Bienvenue dans le jeu de bataille navale')
label_bienvenue.grid(row=0,column=1)

label_info = Label(Frame_Princ,background="#000000",fg = "white",font=("Calibri", 12,"bold"))
label_info.grid(row=6,column=1)


bouton_valider = Button(Frame_Bienvenue,text='VALIDER',bg='black',fg='blue',font=("Calibri", 12), width=10,command=choix_nb_joueur)
bouton_valider.grid(row=4,column=1)

choix = StringVar()
i = 2
for kchoix in ('SOLO','DUO'):
    Radiobutton(Frame_Bienvenue,text=kchoix,value=kchoix,variable=choix,background="#000000",fg='blue',anchor="w",height=2).grid(row=i,column=1)
    i+=1
choix.set("SOLO")



fenetre.mainloop()

"""Faire une mémoire des scores, choix d'un jeux à un ou deux joueurs, nombre de coups limité, changer le designs des boutons"""
"""Avancement: raccourcissement code mode solo(fini), revoir l'affichage des grilles pour le mode duo, refaire des fonctions pour construire un grille plus 
petite etc"""