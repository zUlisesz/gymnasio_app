import flet as ft

def build(page: ft.Page):
    return ft.View(
        route="/config",
        controls=[
            ft.AppBar(title=ft.Text("Configuración"), center_title=True),
            ft.Text("Configuraciones de la aplicación", size=18),
            ft.Container(height=20),
            ft.Switch(label="Notificaciones", value=True),
            ft.Switch(label="Modo oscuro", value=True),
            ft.Container(height=40),
            ft.ElevatedButton(
                "Volver", icon=ft.icons.ARROW_BACK,
                on_click=lambda e: page.go("/home")
            ),
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )