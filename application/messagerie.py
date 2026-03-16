from uuid import uuid4          #permet de génèrer un id aélatoire pour chaque utilisateur
from nicegui import ui          #permer de créer les éléments de l'interface web
import tkinter as tk
from tkinterweb import HtmlFrame
import threading

messages = []                   #stocke les msg envoyés sous forme de tuples

@ui.refreshable                 #rafraîchit automatiquement la page
def chat_messages(own_id):
    for user_id, avatar, text in messages:
        ui.chat_message(avatar=avatar, text=text, sent=user_id==own_id)         #afficher chaque msg dans une bulle en affichant à droite les miens et à gauche les autres

@ui.page('/')
def index():
    ui.add_css('body {background-color: blue ;}')
    def send():
        messages.append((user, avatar, text.value))
        chat_messages.refresh()
        text.value = ''

    user = str(uuid4())
    avatar = f"https://api.dicebear.com/7.x/bottts/svg?seed={user}"
    with ui.column().classes('w-full items-stretch'):
        chat_messages(user)

    with ui.footer().classes('bg = blue'):
        with ui.row().classes('w-full items-center'):
            with ui.avatar():
                ui.image(avatar)
            text = ui.input(placeholder='Votre message') \
                .props('rounded outlined').classes('flex-grow') \
                .on('keydown.enter', send)

def start_server():
    ui.run(host='127.0.0.1', port=8080)

threading.Thread(target=start_server, daemon=True).start()





fenetre = tk.Tk()
fenetre.title("Chat")
fenetre.geometry("640x400")

frame = HtmlFrame(fenetre)
frame.pack(fill = 'both',expand = True)

frame.load_website("http://127.0.0.1:8080")

fenetre.mainloop()
