'''import flet as ft
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
# ft.app(target=main, view=ft.WEB_BROWSER)  # para pruebas rápidas'''




import flet as ft
from views.login_view import build as login_view
from views.empleado_view import build as empleado_view

# ── Sesión en memoria ──────────────────────────────────────────────────────────
# Temporal hasta que core/session.py esté listo.
# Por ahora el login solo tiene admin/1234 (hardcodeado en login_view.py de Ulises).
current_user = {
    "nombre":       "Administrador",
    "rol":          "admin",        # cambiar a "empleado" para probar ese rol
    "autenticado":  False,
}


def main(page: ft.Page):
    page.title = "Gym App"
    page.theme_mode = ft.ThemeMode.DARK
    page.padding = 0

    # ── Cerrar sesión ──────────────────────────────────────────────────────────
    def cerrar_sesion():
        current_user["autenticado"] = False
        page.go("/")

    # ── Builders ───────────────────────────────────────────────────────────────
    def login_builder(page):
        # on_login_success NO recibe argumentos — compatible con el original de Ulises
        def on_login_success():
            current_user["autenticado"] = True
            if current_user["rol"] == "admin":
                page.go("/admin")
            else:
                page.go("/empleado")

        return login_view(page, on_login_success)

    def empleado_builder(page):
        return empleado_view(
            page,
            nombre_empleado=current_user["nombre"],
            on_logout=lambda e: cerrar_sesion(),
        )

    def admin_builder(page):
        # admin_view.py se agrega después — por ahora redirige a empleado
        try:
            from views.admin_view import build as admin_view_fn
            return admin_view_fn(
                page,
                nombre_admin=current_user["nombre"],
                on_logout=lambda e: cerrar_sesion(),
            )
        except ImportError:
            # Si admin_view.py aún no existe, usar empleado_view temporalmente
            return empleado_view(
                page,
                nombre_empleado=current_user["nombre"],
                on_logout=lambda e: cerrar_sesion(),
            )

    # ── Mapa de rutas ──────────────────────────────────────────────────────────
    views_map = {
        "/":         login_builder,
        "/login":    login_builder,
        "/empleado": empleado_builder,
        "/admin":    admin_builder,
    }

    # ── Route guard ────────────────────────────────────────────────────────────
    def route_guard(ruta: str) -> str:
        RUTAS_PROTEGIDAS = {"/empleado", "/admin"}
        RUTAS_ADMIN      = {"/admin"}

        # Sin sesión → solo login
        if ruta in RUTAS_PROTEGIDAS and not current_user["autenticado"]:
            return "/login"

        # Empleado intentando entrar a admin → redirigir a empleado
        if ruta in RUTAS_ADMIN and current_user["rol"] != "admin":
            return "/empleado"

        return ruta

    # ── Manejo de rutas ────────────────────────────────────────────────────────
    def route_change(e):
        page.views.clear()

        ruta_solicitada = page.route or "/"
        ruta_final = route_guard(ruta_solicitada)

        if ruta_final != ruta_solicitada:
            page.go(ruta_final)
            return

        builder = views_map.get(ruta_final, login_builder)
        page.views.append(builder(page))
        page.update()

    def view_pop(e):
        page.views.pop()
        if page.views:
            page.go(page.views[-1].route)
        else:
            page.go("/")

    page.on_route_change = route_change
    page.on_view_pop = view_pop

    page.go("/")


ft.app(target=main, view=ft.AppView.WEB_BROWSER, port=8080)


