import flet as ft


def build(page: ft.Page, on_login_success):

    error_msg = ft.Text("", color="#FF4C4C", size=12, visible=False)

    username = ft.TextField(
        label="Usuario",
        prefix_icon=ft.icons.PERSON_OUTLINE_ROUNDED,
        border_color="#3D3D3D",
        focused_border_color="#C8F135",
        label_style=ft.TextStyle(color="#888888"),
        text_style=ft.TextStyle(color="#FFFFFF", size=15),
        cursor_color="#C8F135",
        bgcolor="#1E1E1E",
        border_radius=12,
        content_padding=ft.padding.symmetric(horizontal=16, vertical=14),
    )

    password = ft.TextField(
        label="Contraseña",
        prefix_icon=ft.icons.LOCK_OUTLINE_ROUNDED,
        password=True,
        can_reveal_password=True,
        border_color="#3D3D3D",
        focused_border_color="#C8F135",
        label_style=ft.TextStyle(color="#888888"),
        text_style=ft.TextStyle(color="#FFFFFF", size=15),
        cursor_color="#C8F135",
        bgcolor="#1E1E1E",
        border_radius=12,
        content_padding=ft.padding.symmetric(horizontal=16, vertical=14),
    )

    def handle_login(e):
        if not username.value or not password.value:
            error_msg.value = "Por favor completa todos los campos."
            error_msg.visible = True
            page.update()
            return

        # TODO: reemplazar con lógica real de autenticación
        if username.value == "admin" and password.value == "1234":
            error_msg.visible = False
            page.update()
            on_login_success()
        else:
            error_msg.value = "Usuario o contraseña incorrectos."
            error_msg.visible = True
            page.update()

    password.on_submit = handle_login

    login_btn = ft.Container(
        content=ft.Text(
            "INICIAR SESIÓN",
            size=14,
            weight=ft.FontWeight.W_700,
            color="#0D0D0D",
        ),
        on_click=handle_login,
        bgcolor="#C8F135",
        border_radius=12,
        padding=ft.padding.symmetric(vertical=16),
        alignment=ft.alignment.center,
        ink=True,
    )

    card = ft.Container(
        content=ft.Column(
            controls=[
                ft.Container(
                    content=ft.Icon(ft.icons.FITNESS_CENTER_ROUNDED, size=44, color="#C8F135"),
                    alignment=ft.alignment.center,
                ),
                ft.Container(height=8),
                ft.Text(
                    "GYM APP",
                    size=26,
                    weight=ft.FontWeight.W_900,
                    color="#FFFFFF",
                    text_align=ft.TextAlign.CENTER
                ),
                ft.Text(
                    "Panel de Administración",
                    size=12,
                    color="#666666",
                    text_align=ft.TextAlign.CENTER
                ),
                ft.Container(height=28),
                username,
                ft.Container(height=12),
                password,
                ft.Container(height=4),
                error_msg,
                ft.Container(height=20),
                login_btn,
                ft.Container(height=14),
                ft.Text(
                    "¿Problemas para ingresar? Contacta al administrador.",
                    size=11,
                    color="#444444",
                    text_align=ft.TextAlign.CENTER,
                ),
            ],
            horizontal_alignment=ft.CrossAxisAlignment.STRETCH,
            spacing=0,
        ),
        width=380,
        padding=ft.padding.symmetric(horizontal=36, vertical=40),
        bgcolor="#141414",
        border_radius=20,
        border=ft.border.all(1, "#2A2A2A"),
        shadow=ft.BoxShadow(
            blur_radius=60,
            color=ft.colors.with_opacity(0.6, "#000000"),
            offset=ft.Offset(0, 20),
        ),
    )

    return ft.View(
        route="/login",
        controls=[
            ft.Container(expand=True),
            ft.Container(
                width=60, height=4,
                bgcolor="#C8F135",
                border_radius=2,
                margin=ft.margin.only(bottom=24),
            ),
            card,
            ft.Container(expand=True),
            ft.Text(
                "© 2025 Gym App · Todos los derechos reservados",
                size=10,
                color="#2A2A2A",
                text_align=ft.TextAlign.CENTER,
            ),
            ft.Container(height=16),
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        vertical_alignment=ft.MainAxisAlignment.START,
        bgcolor="#0D0D0D",
    )