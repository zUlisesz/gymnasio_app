import flet as ft
from views.login_view import build as login_view  
from  views.empleado_view import build as empleado_view

def empleado_view_builder(page):
    return empleado_view(page, nombre_empleado="Administrador", on_logout=lambda: page.go("/"))

def login_view_builder(page):
    return login_view(page, lambda: page.go("/empleado"))

def main(page: ft.Page):
    page.title = "App MVC-ish Flet"
    page.theme_mode = ft.ThemeMode.DARK
    page.padding = 20

    # Diccionario de rutas → función que construye la vista
    views = {
        "/":  login_view_builder,
        "/empleado": empleado_view_builder
    }

    def route_change(e):
        # Limpiamos la pila de vistas (estilo SPA limpio)
        page.views.clear()

        # Obtenemos la función constructora o usamos home por defecto
        view_builder = views.get(page.route, login_view_builder)
        page.views.append(view_builder(page))

        page.update()

    def view_pop(e):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    # Conectamos eventos
    page.on_route_change = route_change
    page.on_view_pop = view_pop

    # Ruta inicial
    page.go(page.route or "/home")


ft.app(target=main)
# ft.app(target=main, view=ft.WEB_BROWSER)  # para pruebas rápidas