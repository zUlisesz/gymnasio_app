import flet as ft

def build(page: ft.Page):
    return ft.View(
        route="/home",
        controls=[
            ft.Text("🏠 Home", size=28, weight= ft.FontWeight.BOLD),
            ft.Container(height=30),
            ft.ElevatedButton(
                "Ir a Perfil",
                icon=ft.icons.PERSON,
                on_click=lambda e: page.go("/perfil")
            ),
            ft.ElevatedButton(
                "Ir a Configuración",
                icon=ft.icons.SETTINGS,
                on_click=lambda e: page.go("/config")
            ),
            ft.ElevatedButton(
                "Ir a Login",
                icon=ft.icons.LOGIN,
                on_click=lambda e: page.go("/login")
            ),
            ft.Text(f"Ruta actual: {page.route}", size=12, color=ft.colors.GREEN_300),
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        vertical_alignment=ft.MainAxisAlignment.CENTER,
    )