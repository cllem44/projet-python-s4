from tkinter import *
from random import randint

def bataille_navale(app):
    class JeuBatailleNavale:
        #classe définie pour éviter un nombre de variables globales importantes
        def __init__(self):
            self.grille = None
            self.grille_J1 = None
            self.grille_J2 = None
            self.bateaux = None
            self.bateaux_J1 = None
            self.bateaux_J2 = None
            self.boutons_J1 = None
            self.boutons_J2 = None
            self.tour_joueur = 1
            self.cpt_coule = 0
            self.cpt_coule_duo = [0, 0]
            self.mode = None
            self.frame_button = None
            self.frame_button_J1 = None
            self.frame_button_J2 = None
            self.nb_coup_solo = 0
            
        def creer_Grille(self,nb_j):
            taille = 8 if nb_j == 1 else 6
            return [['~' for _ in range(taille)]for _ in range (taille)]
        
        def placer_bateaux(self,taille,taille_grille):
            max_coord = taille_grille-1
            choice = randint(0,1)
            bateau = []

            #Bateau placé à l'horizontale
            if choice == 0:
                x = randint(0,max_coord)
                y = randint(0,max_coord-taille+1)
                for i in range(taille):
                    bateau.append([x,y+i])
            
            #Bateau placé à la verticale
            else:
                x = randint(0,max_coord-taille+1)
                y = randint(0,max_coord)
                for i in range(taille):
                    bateau.append([x+i,y])
            
            return bateau
        
        def verifier_Bateaux(self,b2,b3,b4,taille_grille):
            for val in b3:
                if val in b2:
                    b3 = self.placer_bateaux(3,taille_grille)
            
            for val in b4:
                if val in b3 or val in b2:
                    b4 = self.placer_bateaux(4,taille_grille)
            
            return b2,b3,b4
        
        def est_Coule(self,bateau,grille,mode):
            if mode == 'DUO':
                self.cpt_coule_duo[self.tour_joueur-1]+=1
            else:
                self.cpt_coule+=1
            
            return all(grille[x][y]=='+' for x,y in bateau)
        
        def verifier_tir(self,tir,grille,bateaux,boutons):
            for bateau in bateaux.values():
                if tir in bateau:              
                    grille[tir[0]][tir[1]] = '+'
                    if self.est_Coule(bateau,grille,self.mode):
                        for val in bateau:
                            boutons [val[0]][val[1]].config(text='',bg='green')
                        return 'Coulé'
                    return 'Touché'
                
            grille[tir[0]][tir[1]] = 'o'
            return 'Raté'

        def tirer_case_solo(self,x,y,boutons):
            if self.nb_coup_solo >= 40:
                self.defaite()
                self.nb_coup_solo = 0
                return
            
            self.nb_coup_solo += 1

            if self.grille[x][y] != '~':
                return
            
            tir = [x,y]
            
            resultat = self.verifier_tir(tir,self.grille,self.bateaux,boutons)
            couleurs = {'Touché':('+','red'),'Raté':('o','blue'),'Coulé':('','green')}

            texte,couleur = couleurs[resultat]
            boutons[x][y].config(text=texte,bg=couleur)

            label_info.config(text=f'{resultat}\nTir(s) restants : {40-self.nb_coup_solo}')
            if self.cpt_coule == 9:
                self.victoire(0)

        def tirer_case_duo(self,x,y,boutons,grille_cible,bateaux_cible):
            tir = [x,y]

            if grille_cible[x][y] != '~':
                return
            
            resultat = self.verifier_tir(tir,grille_cible,bateaux_cible,boutons)
            couleurs = {'Touché':('+','red'),'Raté':('o','blue'),'Coulé':('','green')}
            texte,couleur = couleurs[resultat]
            boutons[x][y].config(text=texte,bg=couleur)

            if self.tour_joueur == 1:
                self.tour_joueur = 2
                #label_tour.config(text='Tour du joueur 2')
            else:
                self.tour_joueur = 1
                #label_tour.config(text='Tour du joueur 1')
            label_info.config(text=f'Résultat:{resultat}')
            self.changer_grille_active(activer_J2=(self.tour_joueur==2))
            if 9 in self.cpt_coule_duo:
                self.victoire(self.cpt_coule_duo.index(9)+1)

        def changer_grille_active(self,activer_J2):
            for ligne in self.boutons_J1:
                for b in ligne:
                    b.config(state=NORMAL if activer_J2 else DISABLED)
        
            for ligne in self.boutons_J2:
                for b in ligne:
                    b.config(state=DISABLED if activer_J2 else NORMAL)
        
        def victoire(self,num_gagnant):
            label_info.config(text=f'VICTOIRE {"JOUEUR " + str(num_gagnant) if num_gagnant else ""}!')
            bouton_quitter = Button(Frame_Princ,text='QUITTER',bg='black',fg='blue',width=4,height=2,command=ecran_bienvenue)
            bouton_quitter.grid(row=8,column=1)

        def defaite(self):
            label_info.config(text=f'DEFAITE !')
            bouton_quitter = Button(Frame_Princ,text='QUITTER',bg='black',fg='blue',width=6,height=2,command=ecran_bienvenue)
            bouton_quitter.grid(row=8,column=1,columnspan=2)

            
        
        def jeu_solo(self):
            self.mode = 'SOLO'
            self.cpt_coule = 0
            self.grille = self.creer_Grille(1)
            b2,b3,b4 = self.verifier_Bateaux(self.placer_bateaux(2,8),self.placer_bateaux(3,8),self.placer_bateaux(4,8),8)
            self.bateaux = {'bateaux2':b2,'bateaux3':b3,'bateaux4':b4}
            self.creer_plateau_solo()
        
        def jeu_duo(self,frame):
            self.mode = 'DUO'
            self.cpt_coule_duo = [0,0]
            self.grille_J1 = self.creer_Grille(2)
            self.grille_J2 = self.creer_Grille(2)
            b2_J1,b3_J1,b4_J1 = self.verifier_Bateaux(self.placer_bateaux(2,6),self.placer_bateaux(3,6),self.placer_bateaux(4,6),6)
            b2_J2,b3_J2,b4_J2 = self.verifier_Bateaux(self.placer_bateaux(2,6),self.placer_bateaux(3,6),self.placer_bateaux(4,6),6)
            self.bateaux_J1 = {'bateaux2':b2_J1,'bateaux3':b3_J1,'bateaux4':b4_J1}
            self.bateaux_J2 = {'bateaux2':b2_J2,'bateaux3':b3_J2,'bateaux4':b4_J2}
            self.creer_plateaux_duo(frame)
        
        def creer_plateau_solo(self):
            boutons = []
            self.frame_button = Frame(Frame_Princ,background='#000000')
            self.frame_button.grid(row=1,column=1)
            for i in range(8):
                ligne = []
                for j in range(8):
                    b=Button(self.frame_button,text='~',bg='black',fg='white',width=4,height=2,command=lambda x=i,y=j:self.tirer_case_solo(x,y,boutons))
                    b.grid(row=i,column=j)
                    ligne.append(b)
                boutons.append(ligne)
        
        def creer_plateaux_duo(self,frame):
            self.boutons_J1 = []
            self.boutons_J2 = []
    
            self.frame_button_J1 = Frame(frame, background='#000000')
            self.frame_button_J1.grid(row=2, column=1)
            label_J1 = Label(frame, text='Grille Joueur 1', bg='#000000', fg='cyan')
            label_J1.grid(row=1, column=1)
    
            self.frame_button_J2 = Frame(frame, background='#000000')
            self.frame_button_J2.grid(row=4, column=1)
            label_J2 = Label(frame, text='Grille Joueur 2', bg='#000000', fg='orange')
            label_J2.grid(row=3, column=1)
    
            for i in range(6):
                ligne = []
                for j in range(6):
                    b = Button(self.frame_button_J1, text='~', bg='black', fg='white', width=4, height=2,command=lambda x=i, y=j: self.tirer_case_duo(x, y, self.boutons_J1, self.grille_J1, self.bateaux_J1))
                    b.grid(row=i, column=j)
                    ligne.append(b)
                self.boutons_J1.append(ligne)
    
            for i in range(6):
                ligne = []
                for j in range(6):
                    b = Button(self.frame_button_J2, text='~', bg='black', fg='white', width=4, height=2,command=lambda x=i, y=j: self.tirer_case_duo(x, y, self.boutons_J2, self.grille_J2, self.bateaux_J2))
                    b.grid(row=i, column=j)
                    ligne.append(b)
                self.boutons_J2.append(ligne)
    
            self.changer_grille_active(activer_J2=False)
        
        def creer_boutons(self,frame,grille_cible,bateaux_cible,ligne):
            boutons = []
            f = Frame(frame,background='#000000')
            f.grid(row = ligne,column=1)

            for i in range(6):
                l = []
                for j in range(6):
                        b=Button(f,text='~',bg='black',fg='white',width=4,height=2,command=lambda x=i,y=j,g=grille_cible,d=bateaux_cible:self.tirer_case_duo(x,y,boutons,g,d))
                        b.grid(row=i,column=j)
                        l.append(b)
                boutons.append(l)
            return boutons

    jeu = JeuBatailleNavale()

    def choix_nb_j():
        if choix.get() == 'SOLO':
            Frame_Bienvenue.destroy()
            jeu.jeu_solo()
        else:
            Frame_Bienvenue.destroy()
            jeu.jeu_duo(Frame_Princ)

    def ecran_bienvenue():
        global Frame_Bienvenue,choix,label_info
        for widget in Frame_Princ.winfo_children():
            widget.destroy()


        Frame_Bienvenue = Frame(Frame_Princ,background="#000000")
        Frame_Bienvenue.grid(row=2,column=1)

        label_bienvenue = Label(Frame_Bienvenue,background="black",fg = "blue",font=("Calibri", 15,"bold"))
        label_bienvenue.config(text='Bienvenue dans le jeu de bataille navale')
        label_bienvenue.grid(row=0,column=1)

        bouton_valider = Button(Frame_Bienvenue,text='VALIDER',bg='black',fg='blue',font=("Calibri", 12), width=10,command=choix_nb_j)
        bouton_valider.grid(row=4,column=1)

        label_info = Label(Frame_Princ,background="#000000",fg = "white",font=("Calibri", 12,"bold"))
        label_info.grid(row=7,column=1)
        label_info.config(text='')

        choix = StringVar()
        i = 2
        for kchoix in ('SOLO','DUO'):
            Radiobutton(Frame_Bienvenue,text=kchoix,value=kchoix,variable=choix,background="#000000",fg='blue',anchor="w",height=2).grid(row=i,column=1)
            i+=1
        choix.set("SOLO")

        

    Frame_Princ = Frame(app,background="#000000")
    Frame_Princ.pack()

    Frame_Bienvenue = Frame(Frame_Princ,background="#000000")
    Frame_Bienvenue.grid(row=2,column=1)

    label_bienvenue = Label(Frame_Bienvenue,background="black",fg = "blue",font=("Calibri", 15,"bold"))
    label_bienvenue.config(text='Bienvenue dans le jeu de bataille navale')
    label_bienvenue.grid(row=0,column=1)

    label_info = Label(Frame_Princ,background="#000000",fg = "white",font=("Calibri", 12,"bold"))
    label_info.grid(row=7,column=1)


    bouton_valider = Button(Frame_Bienvenue,text='VALIDER',bg='black',fg='blue',font=("Calibri", 12), width=10,command=choix_nb_j)
    bouton_valider.grid(row=4,column=1)

    choix = StringVar()
    i = 2
    for kchoix in ('SOLO','DUO'):
        Radiobutton(Frame_Bienvenue,text=kchoix,value=kchoix,variable=choix,background="#000000",fg='blue',anchor="w",height=2).grid(row=i,column=1)
        i+=1
    choix.set("SOLO")

    return Frame_Princ