from uuid import uuid4          #permet de génèrer un id aélatoire pour chaque utilisateur
from nicegui import ui          #permer de créer les éléments de l'interface web

messages = []                   #stocke les msg envoyés sous forme de tuples

@ui.refreshable                 #rafraîchit automatiquement la page
def chat_messages(own_id):
    for user_id, avatar, text in messages:
        ui.chat_message(avatar=avatar, text=text, sent=user_id==own_id)         #afficher chaque msg dans une bulle en affichant à droite les miens et à gauche les autres

@ui.page('/')
def index():
    ui.add_css('body {background-color: red;}')
    def send():
        messages.append((user, avatar, text.value))
        chat_messages.refresh()
        text.value = ''

    user = str(uuid4())
    avatar = "https://img.freepik.com/psd-gratuit/illustration-realiste-voiture_23-2151227624.jpg?semt=ais_hybrid&w=740&q=80"
    with ui.column().classes('w-full items-stretch'):
        chat_messages(user)

    with ui.footer().classes('bg = red'):
        with ui.row().classes('w-full items-center'):
            with ui.avatar():
                ui.image(avatar)
            text = ui.input(placeholder='Votre message') \
                .props('rounded outlined').classes('flex-grow') \
                .on('keydown.enter', send)

ui.run()