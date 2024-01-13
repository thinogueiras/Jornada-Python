import flet as ft
from datetime import datetime


def main(page):
    chat_date = datetime.now().strftime('%d/%m/%Y')
    title = ft.Text(f"ChAt Da GaLeRa: {chat_date}")

    chat = ft.Column()

    def send_message_in_tunnel(informations):
        chat.controls.append(ft.Text(informations))
        page.update()

    page.pubsub.subscribe(send_message_in_tunnel)

    def send_message(event):
        message_time = datetime.now().strftime('%H:%M')
        message_field_text = f"{username.value} - {message_time}: \n{message_field.value}"

        if message_field.value == "":
            pass
        else:
            page.pubsub.send_all(f'{message_field_text}')

        message_field.value = ""
        message_field.focus()
        page.update()

    send_button = ft.ElevatedButton("Enviar", on_click=send_message)

    message_field = ft.TextField(
        label="Escreva a sua mensagem aqui", on_submit=send_message, autofocus=True)

    def enter_chat_button(event):
        popup.open = False
        page.remove(start_button)

        page.add(chat)

        message_line = ft.Row([message_field, send_button])

        page.add(message_line)

        joined_chat_text = f"{username.value} entrou no chat..."
        page.pubsub.send_all(joined_chat_text)

        page.update()

    username = ft.TextField(label="Escreva seu nome",
                            on_submit=enter_chat_button, autofocus=True)

    popup = ft.AlertDialog(
        open=False,
        modal=True,
        title=ft.Text("Bem-vindo ao Bate Papo Python"),
        content=username,
        actions=[ft.ElevatedButton("Entrar", on_click=enter_chat_button)])

    def start_chat(event):
        page.dialog = popup
        popup.open = True
        page.update()

    start_button = ft.ElevatedButton(
        "Iniciar Chat", on_click=start_chat, autofocus=True)

    page.add(title)
    page.add(start_button)


ft.app(main, view=ft.WEB_BROWSER)
