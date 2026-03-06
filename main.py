from tkinter import *

def changerDanemark():
    can1.create_rectangle(0,0,400,370,width = 0,fill = "#ff0000")
    can1.create_rectangle(140,0,180,370,width = 0,fill = "#ffffff")
    can1.create_rectangle(0,165,400,205,width = 0,fill = "#ffffff")
def changerBahamas():
    can1.create_rectangle(0,0,400,123,width=0,fill ="#00c8ff")
    can1.create_rectangle(0,123,400,246,width=0,fill ="#eaff00")
    can1.create_rectangle(0,246,400,370,width=0,fill ="#00c8ff")
    can1.create_polygon(200,185,0,0,0,370,width=0,fill ="#000000")
def changerFrance():
    can1.create_rectangle(0,0,133,370,width = 0, fill ="#0056eb")
    can1.create_rectangle(133,0,266,370,width = 0, fill ="#ffffff")
    can1.create_rectangle(266,0,400,370,width = 0, fill ="#ff0000")
def changerAllemagne():
    can1.create_rectangle(0,0,400,123,width=0,fill ="#000000")
    can1.create_rectangle(0,123,400,246,width=0,fill ="#ff0000")
    can1.create_rectangle(0,246,400,370,width=0,fill ="#c6b500")
def changerOlympique():
    can1.create_rectangle(0,0,400,370,fill="#ffffff")
    can1.create_oval(40,100,140,200,outline="#00c8ff",width=5)
    can1.create_oval(90,150,190,250,outline="#eaff00",width=5)
    can1.create_oval(150,100,250,200,outline="#000000",width=5)
    can1.create_oval(200,150,300,250,outline="#00ff26",width=5)
    can1.create_oval(260,100,360,200,outline="#ff0000",width=5)

fenetre = Tk()
fenetre.title("TP1 - Les drapeaux")
fenetre.geometry("400x400")

fenetre.minsize(300,300)

can1 = Canvas(fenetre,bg="#FFFFFF",height=370,width=400)
can1.pack(side=TOP)
can1.create_rectangle(0,0,400,370,fill="#c1c1c1")
bt1 = Button(fenetre,text='Quitter',command=fenetre.destroy) 
bt1.pack(side=RIGHT)
bt2 = Button(fenetre,text='Danemark',bg = "#ffffff",fg ="black",width=7,command=changerDanemark) 
bt2.place(x=180,y=385,anchor="center",width=70)
bt3 = Button(fenetre,text='Bahamas',bg = "#ffffff",fg ="black",width=7,command=changerBahamas) 
bt3.place(x=110,y=385,anchor="center",width=70)
bt4 = Button(fenetre,text='Allemagne',bg = "#ffffff",fg ="black",width=7,command=changerAllemagne) 
bt4.place(x=40,y=385,anchor="center",width=70)
bt5 = Button(fenetre,text='France',bg = "#ffffff",fg ="black",width=7,command=changerFrance) 
bt5.place(x=245,y=385,anchor="center",width=60)
bt6 = Button(fenetre,text='Olympique',bg = "#ffffff",fg ="black",width=7,command=changerOlympique) 
bt6.place(x=307,y=385,anchor="center",width=65)
fenetre.mainloop()