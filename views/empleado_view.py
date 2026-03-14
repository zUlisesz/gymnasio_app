import flet as ft


# ── Paleta de colores ─────────────────────────────────────────────────────────
BG_DARK       = "#0D0D0D"
BG_CARD       = "#141414"
BG_INPUT      = "#1E1E1E"
BORDER        = "#2A2A2A"
BORDER_LIGHT  = "#3D3D3D"
ACCENT        = "#C8F135"
TEXT_PRIMARY  = "#FFFFFF"
TEXT_MUTED    = "#666666"
TEXT_FAINT    = "#2A2A2A"
SIDEBAR_BG    = "#111111"
HOVER_BG      = "#1A1A1A"


def build(page: ft.Page, nombre_empleado: str = "Administrador", on_logout=None):

    # ── Estado activo del sidebar ─────────────────────────────────────────────
    active_route = ft.Ref[str]()
    active_route.current = "miembros"

    content_area = ft.Ref[ft.Container]()

    # ── Helpers ───────────────────────────────────────────────────────────────
    def stat_card(icon, label, value, color=ACCENT):
        return ft.Container(
            content=ft.Column(
                controls=[
                    ft.Container(
                        content=ft.Icon(icon, color=color, size=28),
                        bgcolor=ft.colors.with_opacity(0.08, color),
                        border_radius=12,
                        padding=10,
                        alignment=ft.alignment.center,
                        width=52,
                        height=52,
                    ),
                    ft.Container(height=12),
                    ft.Text(str(value), size=26, weight=ft.FontWeight.W_800,
                            color=TEXT_PRIMARY),
                    ft.Text(label, size=12, color=TEXT_MUTED),
                ],
                spacing=0,
            ),
            bgcolor=BG_CARD,
            border_radius=16,
            border=ft.border.all(1, BORDER),
            padding=ft.padding.symmetric(horizontal=20, vertical=18),
            expand=True,
        )

    def action_card(icon, label, subtitle, color=ACCENT, on_click=None):
        return ft.Container(
            content=ft.Column(
                controls=[
                    ft.Icon(icon, color=color, size=32),
                    ft.Container(height=10),
                    ft.Text(label, size=14, weight=ft.FontWeight.W_700,
                            color=TEXT_PRIMARY),
                    ft.Text(subtitle, size=11, color=TEXT_MUTED),
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=0,
            ),
            bgcolor=BG_CARD,
            border_radius=16,
            border=ft.border.all(1, BORDER),
            padding=20,
            alignment=ft.alignment.center,
            ink=True,
            on_click=on_click,
            expand=True,
        )

    def section_title(text):
        return ft.Text(text, size=11, color=TEXT_MUTED,
                       weight=ft.FontWeight.W_600)

    # ── Vistas de contenido ───────────────────────────────────────────────────
    def view_miembros():
        return ft.Column(
            controls=[
                ft.Text("Miembros", size=22, weight=ft.FontWeight.W_800,
                        color=TEXT_PRIMARY),
                ft.Text("Gestión de clientes del gimnasio", size=13,
                        color=TEXT_MUTED),
                ft.Container(height=20),
                ft.Row(
                    controls=[
                        stat_card(ft.icons.PEOPLE_OUTLINE_ROUNDED,
                                  "Total miembros", "128"),
                        stat_card(ft.icons.PERSON_ADD_OUTLINED,
                                  "Nuevos este mes", "14", "#4FC3F7"),
                        stat_card(ft.icons.PERSON_OFF_OUTLINED,
                                  "Inactivos", "9", "#FF7043"),
                    ],
                    spacing=16,
                ),
                ft.Container(height=24),
                section_title("ACCIONES RÁPIDAS"),
                ft.Container(height=12),
                ft.Row(
                    controls=[
                        action_card(ft.icons.PERSON_ADD_ROUNDED,
                                    "Nuevo miembro", "Registrar cliente"),
                        action_card(ft.icons.SEARCH_ROUNDED,
                                    "Buscar", "Consultar miembro"),
                        action_card(ft.icons.LIST_ALT_ROUNDED,
                                    "Ver todos", "Lista completa"),
                    ],
                    spacing=16,
                ),
            ],
            spacing=0,
            expand=True,
        )

    def view_productos():
        return ft.Column(
            controls=[
                ft.Text("Productos", size=22, weight=ft.FontWeight.W_800,
                        color=TEXT_PRIMARY),
                ft.Text("Control de inventario y productos", size=13,
                        color=TEXT_MUTED),
                ft.Container(height=20),
                ft.Row(
                    controls=[
                        stat_card(ft.icons.INVENTORY_2_OUTLINED,
                                  "En stock", "342"),
                        stat_card(ft.icons.WARNING_AMBER_ROUNDED,
                                  "Bajo stock", "7", "#FFB300"),
                        stat_card(ft.icons.ATTACH_MONEY_ROUNDED,
                                  "Valor total", "$12,400", "#66BB6A"),
                    ],
                    spacing=16,
                ),
                ft.Container(height=24),
                section_title("ACCIONES RÁPIDAS"),
                ft.Container(height=12),
                ft.Row(
                    controls=[
                        action_card(ft.icons.ADD_BOX_ROUNDED,
                                    "Agregar producto", "Nuevo ítem"),
                        action_card(ft.icons.EDIT_OUTLINED,
                                    "Editar", "Modificar producto"),
                        action_card(ft.icons.BAR_CHART_ROUNDED,
                                    "Reportes", "Ver estadísticas",
                                    color="#4FC3F7"),
                    ],
                    spacing=16,
                ),
            ],
            spacing=0,
            expand=True,
        )

    def view_inscribir():
        return ft.Column(
            controls=[
                ft.Text("Inscribir", size=22, weight=ft.FontWeight.W_800,
                        color=TEXT_PRIMARY),
                ft.Text("Registrar nuevo miembro al gimnasio", size=13,
                        color=TEXT_MUTED),
                ft.Container(height=24),
                ft.Container(
                    content=ft.Column(
                        controls=[
                            section_title("DATOS DEL CLIENTE"),
                            ft.Container(height=16),
                            ft.Row(
                                controls=[
                                    ft.TextField(
                                        label="Nombre",
                                        prefix_icon=ft.icons.PERSON_OUTLINE,
                                        expand=True,
                                        border_color=BORDER_LIGHT,
                                        focused_border_color=ACCENT,
                                        label_style=ft.TextStyle(color=TEXT_MUTED),
                                        text_style=ft.TextStyle(color=TEXT_PRIMARY),
                                        cursor_color=ACCENT,
                                        bgcolor=BG_INPUT,
                                        border_radius=10,
                                    ),
                                    ft.TextField(
                                        label="Apellido",
                                        prefix_icon=ft.icons.PERSON_OUTLINE,
                                        expand=True,
                                        border_color=BORDER_LIGHT,
                                        focused_border_color=ACCENT,
                                        label_style=ft.TextStyle(color=TEXT_MUTED),
                                        text_style=ft.TextStyle(color=TEXT_PRIMARY),
                                        cursor_color=ACCENT,
                                        bgcolor=BG_INPUT,
                                        border_radius=10,
                                    ),
                                ],
                                spacing=16,
                            ),
                            ft.Container(height=12),
                            ft.TextField(
                                label="Teléfono",
                                prefix_icon=ft.icons.PHONE_OUTLINED,
                                border_color=BORDER_LIGHT,
                                focused_border_color=ACCENT,
                                label_style=ft.TextStyle(color=TEXT_MUTED),
                                text_style=ft.TextStyle(color=TEXT_PRIMARY),
                                cursor_color=ACCENT,
                                bgcolor=BG_INPUT,
                                border_radius=10,
                            ),
                            ft.Container(height=12),
                            ft.TextField(
                                label="Plan",
                                prefix_icon=ft.icons.CARD_MEMBERSHIP_OUTLINED,
                                border_color=BORDER_LIGHT,
                                focused_border_color=ACCENT,
                                label_style=ft.TextStyle(color=TEXT_MUTED),
                                text_style=ft.TextStyle(color=TEXT_PRIMARY),
                                cursor_color=ACCENT,
                                bgcolor=BG_INPUT,
                                border_radius=10,
                            ),
                            ft.Container(height=24),
                            ft.Container(
                                content=ft.Text(
                                    "INSCRIBIR MIEMBRO",
                                    size=13,
                                    weight=ft.FontWeight.W_700,
                                    color="#0D0D0D"
                                ),
                                bgcolor=ACCENT,
                                border_radius=10,
                                padding=ft.padding.symmetric(vertical=14),
                                alignment=ft.alignment.center,
                                ink=True,
                                width=240,
                            ),
                        ],
                        spacing=0,
                    ),
                    bgcolor=BG_CARD,
                    border_radius=16,
                    border=ft.border.all(1, BORDER),
                    padding=28,
                ),
            ],
            spacing=0,
            expand=True,
        )

    def view_renovar():
        return ft.Column(
            controls=[
                ft.Text("Renovar membresía", size=22, weight=ft.FontWeight.W_800,
                        color=TEXT_PRIMARY),
                ft.Text("Extender o cambiar el plan de un miembro", size=13,
                        color=TEXT_MUTED),
                ft.Container(height=24),
                ft.Container(
                    content=ft.Column(
                        controls=[
                            section_title("BUSCAR MIEMBRO"),
                            ft.Container(height=16),
                            ft.Row(
                                controls=[
                                    ft.TextField(
                                        label="Nombre o ID del miembro",
                                        prefix_icon=ft.icons.SEARCH_ROUNDED,
                                        expand=True,
                                        border_color=BORDER_LIGHT,
                                        focused_border_color=ACCENT,
                                        label_style=ft.TextStyle(color=TEXT_MUTED),
                                        text_style=ft.TextStyle(color=TEXT_PRIMARY),
                                        cursor_color=ACCENT,
                                        bgcolor=BG_INPUT,
                                        border_radius=10,
                                    ),
                                    ft.Container(
                                        content=ft.Text(
                                            "BUSCAR",
                                            size=13,
                                            weight=ft.FontWeight.W_700,
                                            color="#0D0D0D"
                                        ),
                                        bgcolor=ACCENT,
                                        border_radius=10,
                                        padding=ft.padding.symmetric(
                                            horizontal=24, vertical=14),
                                        alignment=ft.alignment.center,
                                        ink=True,
                                    ),
                                ],
                                spacing=12,
                            ),
                            ft.Container(height=24),
                            section_title("SELECCIONAR PLAN"),
                            ft.Container(height=16),
                            ft.Row(
                                controls=[
                                    _plan_card("Mensual", "$350", "30 días"),
                                    _plan_card("Trimestral", "$900", "90 días"),
                                    _plan_card("Anual", "$3,000", "365 días",
                                               selected=True),
                                ],
                                spacing=16,
                            ),
                            ft.Container(height=24),
                            ft.Container(
                                content=ft.Text(
                                    "RENOVAR MEMBRESÍA",
                                    size=13,
                                    weight=ft.FontWeight.W_700,
                                    color="#0D0D0D"
                                ),
                                bgcolor=ACCENT,
                                border_radius=10,
                                padding=ft.padding.symmetric(vertical=14),
                                alignment=ft.alignment.center,
                                ink=True,
                                width=240,
                            ),
                        ],
                        spacing=0,
                    ),
                    bgcolor=BG_CARD,
                    border_radius=16,
                    border=ft.border.all(1, BORDER),
                    padding=28,
                ),
            ],
            spacing=0,
            expand=True,
        )

    def _plan_card(nombre, precio, duracion, selected=False):
        color = ACCENT if selected else BORDER_LIGHT
        bg = ft.colors.with_opacity(0.06, ACCENT) if selected else BG_INPUT
        return ft.Container(
            content=ft.Column(
                controls=[
                    ft.Text(nombre, size=13, weight=ft.FontWeight.W_700,
                            color=ACCENT if selected else TEXT_PRIMARY),
                    ft.Text(precio, size=20, weight=ft.FontWeight.W_900,
                            color=TEXT_PRIMARY),
                    ft.Text(duracion, size=11, color=TEXT_MUTED),
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=4,
            ),
            bgcolor=bg,
            border_radius=12,
            border=ft.border.all(1.5 if selected else 1, color),
            padding=ft.padding.symmetric(horizontal=16, vertical=14),
            alignment=ft.alignment.center,
            expand=True,
        )

    # ── Mapa ruta → contenido ─────────────────────────────────────────────────
    views_map = {
        "miembros":  view_miembros,
        "productos": view_productos,
        "inscribir": view_inscribir,
        "renovar":   view_renovar,
    }

    # ── Sidebar items ─────────────────────────────────────────────────────────
    sidebar_refs = {}

    def make_sidebar_item(route, label, icon):
        is_active = route == active_route.current

        item_ref = ft.Ref[ft.Container]()
        sidebar_refs[route] = item_ref

        def on_tap(e, r=route):
            active_route.current = r
            # actualizar estilos sidebar
            for k, ref in sidebar_refs.items():
                is_sel = k == r
                ref.current.bgcolor = ft.colors.with_opacity(
                    0.08, ACCENT) if is_sel else "transparent"
                ref.current.border = ft.border.only(
                    left=ft.BorderSide(3, ACCENT)) if is_sel else ft.border.only(
                    left=ft.BorderSide(3, "transparent"))
                # icono y texto
                col = ref.current.content
                col.controls[0].color = ACCENT if is_sel else TEXT_MUTED
                col.controls[1].color = ACCENT if is_sel else TEXT_MUTED
                col.controls[1].weight = (
                    ft.FontWeight.W_700 if is_sel else ft.FontWeight.W_400)
            # actualizar contenido
            content_area.current.content = ft.Container(
                content=views_map[r](),
                padding=ft.padding.all(28),
                expand=True,
            )
            page.update()

        return ft.Container(
            ref=item_ref,
            content=ft.Row(
                controls=[
                    ft.Icon(icon,
                            color=ACCENT if is_active else TEXT_MUTED,
                            size=20),
                    ft.Text(label,
                            size=13,
                            color=ACCENT if is_active else TEXT_MUTED,
                            weight=ft.FontWeight.W_700 if is_active
                            else ft.FontWeight.W_400),
                ],
                spacing=14,
            ),
            bgcolor=ft.colors.with_opacity(0.08, ACCENT) if is_active
            else "transparent",
            border=ft.border.only(
                left=ft.BorderSide(3, ACCENT if is_active else "transparent")),
            border_radius=ft.border_radius.only(
                top_right=10, bottom_right=10),
            padding=ft.padding.symmetric(horizontal=20, vertical=13),
            ink=True,
            on_click=on_tap,
        )

    sidebar_items = [
        ("miembros",  "Miembros",  ft.icons.PEOPLE_OUTLINE_ROUNDED),
        ("productos", "Productos", ft.icons.INVENTORY_2_OUTLINED),
        ("inscribir", "Inscribir", ft.icons.PERSON_ADD_OUTLINED),
        ("renovar",   "Renovar",   ft.icons.AUTORENEW_ROUNDED),
    ]

    sidebar = ft.Container(
        content=ft.Column(
            controls=[
                # Logo mini
                ft.Container(
                    content=ft.Row(
                        controls=[
                            ft.Icon(ft.icons.FITNESS_CENTER_ROUNDED,
                                    color=ACCENT, size=22),
                            ft.Text("GYM", size=16, weight=ft.FontWeight.W_900,
                                    color=TEXT_PRIMARY),
                        ],
                        spacing=10,
                    ),
                    padding=ft.padding.symmetric(horizontal=20, vertical=24),
                ),
                ft.Divider(height=1, color=BORDER, thickness=1),
                ft.Container(height=16),
                *[make_sidebar_item(r, l, i) for r, l, i in sidebar_items],
                ft.Container(expand=True),
                ft.Divider(height=1, color=BORDER),
                ft.Container(
                    content=ft.Row(
                        controls=[
                            ft.Icon(ft.icons.LOGOUT_ROUNDED,
                                    color="#FF4C4C", size=18),
                            ft.Text("Cerrar sesión", size=12, color="#FF4C4C"),
                        ],
                        spacing=10,
                    ),
                    padding=ft.padding.symmetric(horizontal=20, vertical=16),
                    ink=True,
                    on_click=on_logout,
                    border_radius=ft.border_radius.only(
                        top_right=10, bottom_right=10),
                ),
            ],
            spacing=0,
            expand=True,
        ),
        width=210,
        bgcolor=SIDEBAR_BG,
        border=ft.border.only(right=ft.BorderSide(1, BORDER)),
    )

    # ── Navbar ────────────────────────────────────────────────────────────────
    navbar = ft.Container(
        content=ft.Row(
            controls=[
                ft.Text("Panel de Empleado", size=14, color=TEXT_MUTED),
                ft.Container(expand=True),
                ft.Container(
                    content=ft.Row(
                        controls=[
                            ft.Container(
                                content=ft.Icon(
                                    ft.icons.PERSON_OUTLINE_ROUNDED,
                                    color=ACCENT, size=18),
                                bgcolor=ft.colors.with_opacity(0.10, ACCENT),
                                border_radius=20,
                                padding=8,
                            ),
                            ft.Column(
                                controls=[
                                    ft.Text(nombre_empleado, size=13,
                                            weight=ft.FontWeight.W_700,
                                            color=TEXT_PRIMARY),
                                    ft.Text("Empleado", size=10,
                                            color=TEXT_MUTED),
                                ],
                                spacing=0,
                                horizontal_alignment=ft.CrossAxisAlignment.END,
                            ),
                        ],
                        spacing=10,
                    ),
                ),
            ],
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
        ),
        height=62,
        bgcolor=BG_CARD,
        border=ft.border.only(bottom=ft.BorderSide(1, BORDER)),
        padding=ft.padding.symmetric(horizontal=28),
    )

    # ── Área de contenido ─────────────────────────────────────────────────────
    main_content = ft.Container(
        ref=content_area,
        content=ft.Container(
            content=view_miembros(),
            padding=ft.padding.all(28),
            expand=True,
        ),
        expand=True,
        bgcolor=BG_DARK,
    )

    # ── Layout completo ───────────────────────────────────────────────────────
    body = ft.Row(
        controls=[sidebar, main_content],
        spacing=0,
        expand=True,
    )

    return ft.View(
        route="/empleado",
        controls=[
            ft.Column(
                controls=[navbar, body],
                spacing=0,
                expand=True,
            )
        ],
        padding=0,
        bgcolor=BG_DARK,
    )