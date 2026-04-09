from tkinter import *

def creer_morpion(app):
    def creergrille():
        can1.create_line(10,10,388,10)
        can1.create_line(10,120,388,120)
        can1.create_line(10,230,388,230)
        can1.create_line(10,340,388,340)
        can1.create_line(10,10,10,340)
        can1.create_line(136,10,136,340)
        can1.create_line(262,10,262,340)
        can1.create_line(388,10,388,340)

    def dessinerforme(x,y,k):
        if k % 2 == 1:
            can1.create_line(x-50,y-50,x+50,y+50,width=5,fill="#FF0000")
            can1.create_line(x+50,y-50,x-50,y+50,width=5,fill="#FF0000")
        else:
            can1.create_oval(x-50,y-50,x+50,y+50,width=5,outline="#3C00FF")

    def verifier_victoire():
        for i in range(3):
            if l2[i][0] == l2[i][1] == l2[i][2] != 0:
                return l2[i][0]
        for i in range(3):
            if l2[0][i] == l2[1][i] == l2[2][i] != 0:
                return l2[0][i]
        if l2[0][0] == l2[1][1] == l2[2][2] != 0:
            return l2[0][0]
        if l2[0][2] == l2[1][1] == l2[2][0] != 0:
            return l2[0][2]
        return None

    def afficher_resultat(message):
        affiche = Toplevel(frame_morpion_general)
        affiche.title("Résultat")
        affiche.geometry("300x150")
        ecran = Label(affiche, text=message, fg="blue", font=("Arial", 14))
        ecran.pack()

    def dessiner(event):
        nonlocal k, l, l2
        x = event.x
        y = event.y
        for i in range(3):
            if (x-i*126) <= 126 and 10 <= (x-i*126) <= 390:
                for j in range(3):
                    if (y-j*110) <= 110 and 10 <= (y-j*110) <= 340:
                        if [(10+i*126+63),(10+j*110+55)] not in l:
                            k += 1
                            dessinerforme((10+i*126+63),(10+j*110+55),k)
                            l.append([(10+i*126+63),(10+j*110+55)])
                            if k % 2 == 0:
                                l2[j][i] = "O"
                            else:
                                l2[j][i] = "X"
                            gagnant = verifier_victoire()
                            if gagnant:
                                afficher_resultat(f"Bravo Joueur {gagnant}\nTu as gagné")
                                can1.unbind('<Button-1>')
                                return
                            if k == 9:
                                afficher_resultat("Match nul !")
                                can1.unbind('<Button-1>')
                                return

    def rejouer():
        nonlocal k, l, l2
        can1.delete("all")
        creergrille()
        k = 0
        l = []
        l2 = [[0 for _ in range(3)] for _ in range(3)]
        can1.bind('<Button-1>', dessiner)

    k = 0
    l = []
    l2 = [[0 for _ in range(3)] for _ in range(3)]

    frame_morpion_general = Frame(app, background="#000000")
    frame_morpion_general.grid(row=0, column=0, sticky="nsew")
    frame_morpion_general.grid_propagate(False)
    frame_morpion_general.grid_rowconfigure(0, weight=1)
    frame_morpion_general.grid_rowconfigure(1, weight=0)
    frame_morpion_general.grid_columnconfigure(0, weight=1)


    can1 = Canvas(master=frame_morpion_general, bg="#F5FC95", width=400)
    can1.grid(row=0, column=0, columnspan=2,sticky="nsew")

    bt2 = Button(frame_morpion_general, text='Rejouer', command=rejouer)
    bt2.grid(row=1, column=0, padx=10, pady=10, sticky="ew")

    creergrille()
    can1.bind('<Button-1>', dessiner)
    return frame_morpion_general


if __name__ == "__main__":
    app = Tk()
    app.title("Prototype")
    #app.iconbitmap("img/logo.ico")
    app.geometry("400x700")
    app.resizable(width=False, height=False)
    app.grid_rowconfigure(0, weight=1)
    app.grid_columnconfigure(0, weight=1)
    creer_morpion(app)
    app.mainloop()