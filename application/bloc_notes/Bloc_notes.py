import customtkinter as ctk
from tkinter import *
from tkinter import filedialog, ttk, messagebox
import os

def creer_bloc_notes(app):

    def creer_note(nom_note):
        os.makedirs('application/bloc_notes', exist_ok=True)
        with open(f'application/bloc_notes/{nom_note}.txt', 'w', encoding='utf-8') as f:
            f.write('')
        maj_liste_notes()

    def afficher_valeur():
        valeur_saisie = nom_bloc_note_champ.get()
        if valeur_saisie.strip():
            creer_note(valeur_saisie)
            nom_bloc_note_champ.delete(0, END)

    def affiche_note(nom_note):
        chemin = f'application/bloc_notes/{nom_note}.txt'
        if not os.path.exists(chemin):
            return
        with open(chemin, 'r', encoding='utf-8') as f:
            contenu = f.read()
        zone_texte.config(state="normal")
        zone_texte.delete("1.0", END)
        zone_texte.insert("1.0", contenu)
        note_ouverte.set(nom_note)
        label_note_active.config(text=f"📄 {nom_note}")

    def sauvegarder_note():
        nom = note_ouverte.get()
        if not nom:
            return
        contenu = zone_texte.get("1.0", END)
        with open(f'application/bloc_notes/{nom}.txt', 'w', encoding='utf-8') as f:
            f.write(contenu)

    def supprimer_note():
        nom = note_ouverte.get()
        if not nom:
            return
        confirm = messagebox.askyesno("Supprimer", f"Supprimer la note « {nom} » ?")
        if not confirm:
            return
        os.remove(f'application/bloc_notes/{nom}.txt')
        zone_texte.delete("1.0", END)
        note_ouverte.set("")
        label_note_active.config(text="Aucune note ouverte")
        maj_liste_notes()

    def maj_liste_notes():
        liste_notes.delete(0, END)
        os.makedirs('application/bloc_notes', exist_ok=True)
        for fichier in sorted(os.listdir('application/bloc_notes')):
            if fichier.endswith('.txt'):
                liste_notes.insert(END, fichier.replace('.txt', ''))

    def on_selection(event):
        selection = liste_notes.curselection()
        if selection:
            nom = liste_notes.get(selection[0])
            affiche_note(nom)

    # ── Frame principale ───────────────────────────────────────────────────────

    frame_bloc_note = Frame(app, background="#962F2F")
    frame_bloc_note.grid(row=0, column=0, sticky="nsew")
    frame_bloc_note.grid_columnconfigure(0, weight=1)  # colonne gauche (liste)
    frame_bloc_note.grid_columnconfigure(1, weight=3)  # colonne droite (texte)
    frame_bloc_note.grid_rowconfigure(2, weight=1)

    # ── Colonne gauche : création + liste ──────────────────────────────────────

    # Champ nom
    nom_bloc_note_champ = Entry(master=frame_bloc_note, bg="white",
                                font=("Arial", 11), justify="center")
    nom_bloc_note_champ.grid(column=0, row=0, sticky="ew", padx=10, pady=(10, 3))

    # Bouton créer
    bouton_valider = Button(master=frame_bloc_note, text="+ Créer",
                            font=("Arial", 10), command=afficher_valeur,
                            bg="#6d1f1f", fg="white", relief="flat")
    bouton_valider.grid(column=0, row=1, sticky="ew", padx=10, pady=(0, 5))

    # Liste des notes
    liste_notes = Listbox(master=frame_bloc_note, font=("Arial", 11),
                          bg="white", selectbackground="#c0392b",
                          selectforeground="white", relief="flat")
    liste_notes.grid(column=0, row=2, sticky="nsew", padx=10, pady=(0, 5))
    liste_notes.bind("<<ListboxSelect>>", on_selection)

    # Boutons sauvegarder / supprimer
    frame_boutons = Frame(frame_bloc_note, bg="#962F2F")
    frame_boutons.grid(column=0, row=3, sticky="ew", padx=10, pady=(0, 10))
    frame_boutons.grid_columnconfigure(0, weight=1)
    frame_boutons.grid_columnconfigure(1, weight=1)

    bouton_save = Button(master=frame_boutons, text="💾",
                         font=("Arial", 13), command=sauvegarder_note,
                         bg="#6d1f1f", fg="white", relief="flat")
    bouton_save.grid(row=0, column=0, sticky="ew", padx=(0, 2))

    bouton_suppr = Button(master=frame_boutons, text="🗑",
                          font=("Arial", 13), command=supprimer_note,
                          bg="#4a0f0f", fg="white", relief="flat")
    bouton_suppr.grid(row=0, column=1, sticky="ew", padx=(2, 0))

    # ── Colonne droite : zone de texte ─────────────────────────────────────────

    label_note_active = Label(frame_bloc_note, text="Aucune note ouverte",
                              bg="#962F2F", fg="white", font=("Arial", 10, "italic"))
    label_note_active.grid(column=1, row=0, sticky="w", padx=(0, 10), pady=(10, 0))

    cadre_texte = Frame(frame_bloc_note, bg="#962F2F")
    cadre_texte.grid(column=1, row=1, rowspan=3, sticky="nsew", padx=(0, 10), pady=(3, 10))
    cadre_texte.grid_columnconfigure(0, weight=1)
    cadre_texte.grid_rowconfigure(0, weight=1)

    scroll_v = Scrollbar(cadre_texte, orient="vertical")
    scroll_v.grid(row=0, column=1, sticky="ns")

    zone_texte = Text(cadre_texte, font=("Arial", 11), wrap="word",
                      undo=True, relief="flat", yscrollcommand=scroll_v.set)
    zone_texte.grid(row=0, column=0, sticky="nsew")
    scroll_v.config(command=zone_texte.yview)

    # ── État ───────────────────────────────────────────────────────────────────

    note_ouverte = StringVar(value="")
    maj_liste_notes()

    return frame_bloc_note


if __name__ == "__main__":
    app = ctk.CTk()
    app.title("Prototype")
    app.iconbitmap("img/logo.ico")
    app.geometry("640x400")
    app.resizable(width=False, height=False)
    app.grid_rowconfigure(0, weight=1)
    app.grid_columnconfigure(0, weight=1)
    creer_bloc_notes(app)
    app.mainloop()