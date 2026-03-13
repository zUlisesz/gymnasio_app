import flet as ft

def build(page: ft.Page):
    return ft.View(
        "/perfil",
        [
            ft.AppBar(title=ft.Text("Perfil"), center_title=True),
            ft.CircleAvatar(radius=50, bgcolor=ft.colors.BLUE_200),
            ft.Text("Ulises Ramírez", size=22),
            ft.Text("zacatelco@tlax.mx", color=ft.colors.GREY_400),
            ft.Container(height=40),
            ft.ElevatedButton(
                "Volver", icon=ft.icons.ARROW_BACK,
                on_click=lambda e: page.go("/home")
            ),
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )