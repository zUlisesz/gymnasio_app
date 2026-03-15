import flet as ft

BG_BASE       = "#080C10"
BG_SURFACE    = "#0F1519"
BG_CARD       = "#141C22"
BG_INPUT      = "#1A2330"
BORDER        = "#1E2D3D"
BORDER_LIGHT  = "#2A3F55"
ACCENT        = "#E8F4FD"
ACCENT_DIM    = "#7BA7C4"
ACCENT_BLUE   = "#3B82F6"
ACCENT_EMERALD= "#10B981"
ACCENT_AMBER  = "#F59E0B"
ACCENT_RED    = "#EF4444"
TEXT_PRIMARY  = "#E8F4FD"
TEXT_MUTED    = "#4A6478"
SIDEBAR_BG    = "#0A0F14"


def build(page: ft.Page, nombre_admin: str = "Administrador", on_logout=None):

    active_route = ft.Ref[str]()
    active_route.current = "dashboard"
    content_area = ft.Ref[ft.Container]()
    sidebar_refs = {}

    def divider_line():
        return ft.Divider(height=1, color=BORDER, thickness=1)

    def sec_label(text):
        return ft.Text(text.upper(), size=9, color=TEXT_MUTED, weight=ft.FontWeight.W_700)

    def tag(texto, color):
        return ft.Container(
            content=ft.Text(texto, size=10, color=color, weight=ft.FontWeight.W_600),
            bgcolor=ft.colors.with_opacity(0.10, color),
            border_radius=4,
            padding=ft.padding.symmetric(horizontal=8, vertical=3),
        )

    def metric_card(titulo, valor, subtitulo, icono, color=ACCENT_BLUE):
        return ft.Container(
            content=ft.Column(
                controls=[
                    ft.Row(controls=[
                        ft.Container(
                            content=ft.Icon(icono, color=color, size=16),
                            bgcolor=ft.colors.with_opacity(0.10, color),
                            border_radius=8,
                            padding=8,
                        ),
                        ft.Container(expand=True),
                    ]),
                    ft.Container(height=16),
                    ft.Text(str(valor), size=28, weight=ft.FontWeight.W_800, color=TEXT_PRIMARY),
                    ft.Container(height=4),
                    ft.Text(titulo, size=12, color=TEXT_MUTED),
                    ft.Text(subtitulo, size=10, color=TEXT_MUTED),
                ],
                spacing=0,
            ),
            bgcolor=BG_CARD,
            border_radius=12,
            border=ft.border.all(1, BORDER),
            padding=ft.padding.symmetric(horizontal=20, vertical=18),
            expand=True,
        )

    def action_btn(texto, icono, color=ACCENT_BLUE, on_click=None):
        return ft.Container(
            content=ft.Row(
                controls=[
                    ft.Icon(icono, color=color, size=16),
                    ft.Text(texto, size=12, color=color, weight=ft.FontWeight.W_600),
                ],
                spacing=8,
                tight=True,
            ),
            bgcolor=ft.colors.with_opacity(0.08, color),
            border=ft.border.all(1, ft.colors.with_opacity(0.20, color)),
            border_radius=8,
            padding=ft.padding.symmetric(horizontal=14, vertical=10),
            ink=True,
            on_click=on_click,
        )

    # ── DASHBOARD ─────────────────────────────────────────────────────────────
    def view_dashboard():
        proximos = [
            ("Ana Torres",     "Mensual",     "3 días"),
            ("Luis Ramírez",   "Trimestral",  "5 días"),
            ("María González", "Mensual",     "2 días"),
            ("Pedro Hdz.",     "Anual",       "7 días"),
        ]
        acciones = [
            ("Agregar empleado",      "Nuevo staff",      ft.icons.PERSON_ADD_OUTLINED,    ACCENT_BLUE,    "staff"),
            ("Ver reporte de hoy",    "Ventas del día",   ft.icons.BAR_CHART_ROUNDED,      ACCENT_EMERALD, "reportes"),
            ("Editar precios",        "Inventario",       ft.icons.EDIT_OUTLINED,           ACCENT_AMBER,   "inventario"),
            ("Ver todos los miembros","Clientes activos", ft.icons.PEOPLE_OUTLINE_ROUNDED,  ACCENT_DIM,     "miembros"),
        ]

        filas_proximos = []
        for nombre, plan, dias in proximos:
            color_dias = ACCENT_AMBER if dias[0] in "34567" else ACCENT_RED
            filas_proximos.append(
                ft.Container(
                    content=ft.Row(
                        controls=[
                            ft.Container(
                                content=ft.Text(nombre[0].upper(), size=12, color=ACCENT_BLUE, weight=ft.FontWeight.W_700),
                                bgcolor=ft.colors.with_opacity(0.10, ACCENT_BLUE),
                                border_radius=20, width=32, height=32,
                                alignment=ft.alignment.center,
                            ),
                            ft.Column(
                                controls=[
                                    ft.Text(nombre, size=12, color=TEXT_PRIMARY, weight=ft.FontWeight.W_500),
                                    ft.Text(plan, size=10, color=TEXT_MUTED),
                                ],
                                spacing=2,
                                expand=True,
                            ),
                            tag(dias, color_dias),
                        ],
                        spacing=10,
                        vertical_alignment=ft.CrossAxisAlignment.CENTER,
                    ),
                    padding=ft.padding.symmetric(vertical=8),
                    border=ft.border.only(bottom=ft.BorderSide(1, BORDER)),
                )
            )

        filas_acciones = []
        for titulo, sub, icono, color, ruta in acciones:
            filas_acciones.append(
                ft.Container(
                    content=ft.Row(
                        controls=[
                            ft.Icon(icono, color=color, size=18),
                            ft.Column(
                                controls=[
                                    ft.Text(titulo, size=12, color=TEXT_PRIMARY, weight=ft.FontWeight.W_600),
                                    ft.Text(sub, size=10, color=TEXT_MUTED),
                                ],
                                spacing=2,
                                expand=True,
                            ),
                            ft.Icon(ft.icons.CHEVRON_RIGHT_ROUNDED, color=TEXT_MUTED, size=16),
                        ],
                        spacing=12,
                        vertical_alignment=ft.CrossAxisAlignment.CENTER,
                    ),
                    bgcolor=BG_INPUT,
                    border_radius=10,
                    border=ft.border.all(1, BORDER),
                    padding=ft.padding.symmetric(horizontal=16, vertical=14),
                    ink=True,
                    on_click=lambda e, r=ruta: cambiar_seccion(r),
                )
            )

        return ft.Column(
            controls=[
                ft.Row(
                    controls=[
                        ft.Column(
                            controls=[
                                ft.Text("Panel general", size=22, weight=ft.FontWeight.W_700, color=TEXT_PRIMARY),
                                ft.Text("Resumen ejecutivo del gimnasio", size=13, color=TEXT_MUTED),
                            ],
                            spacing=2,
                        ),
                        ft.Container(expand=True),
                        ft.Container(
                            content=ft.Text("En vivo", size=10, color=ACCENT_EMERALD, weight=ft.FontWeight.W_600),
                            bgcolor=ft.colors.with_opacity(0.10, ACCENT_EMERALD),
                            border=ft.border.all(1, ft.colors.with_opacity(0.20, ACCENT_EMERALD)),
                            border_radius=20,
                            padding=ft.padding.symmetric(horizontal=12, vertical=5),
                        ),
                    ],
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                ),
                ft.Container(height=24),
                sec_label("Métricas clave"),
                ft.Container(height=12),
                ft.Row(
                    controls=[
                        metric_card("Miembros activos",  "248",     "+12 este mes",          ft.icons.PEOPLE_OUTLINE_ROUNDED,  ACCENT_BLUE),
                        metric_card("Ingresos del mes",  "$18,400", "Membresías + ventas",   ft.icons.ATTACH_MONEY_ROUNDED,    ACCENT_EMERALD),
                        metric_card("Ventas hoy",        "34",      "Productos vendidos",    ft.icons.POINT_OF_SALE_OUTLINED,  ACCENT_AMBER),
                        metric_card("Staff activo",      "6",       "2 admins · 4 empleados",ft.icons.BADGE_OUTLINED,          ACCENT_DIM),
                    ],
                    spacing=12,
                ),
                ft.Container(height=28),
                ft.Row(
                    controls=[
                        ft.Container(
                            content=ft.Column(
                                controls=[
                                    ft.Row(controls=[
                                        sec_label("Membresías por vencer"),
                                        ft.Container(expand=True),
                                        tag("7 días", ACCENT_AMBER),
                                    ]),
                                    ft.Container(height=16),
                                    *filas_proximos,
                                ],
                                spacing=0,
                            ),
                            bgcolor=BG_CARD,
                            border_radius=12,
                            border=ft.border.all(1, BORDER),
                            padding=20,
                            expand=2,
                        ),
                        ft.Container(width=12),
                        ft.Container(
                            content=ft.Column(
                                controls=[
                                    sec_label("Acciones rápidas"),
                                    ft.Container(height=16),
                                    *filas_acciones,
                                ],
                                spacing=8,
                            ),
                            bgcolor=BG_CARD,
                            border_radius=12,
                            border=ft.border.all(1, BORDER),
                            padding=20,
                            expand=1,
                        ),
                    ],
                ),
            ],
            spacing=0,
            scroll=ft.ScrollMode.AUTO,
            expand=True,
        )

    # ── STAFF ─────────────────────────────────────────────────────────────────
    def view_staff():
        def staff_row(nombre, usuario, rol, activo):
            color_rol    = ACCENT_BLUE    if rol    == "admin"  else ACCENT_DIM
            color_estado = ACCENT_EMERALD if activo             else ACCENT_RED
            return ft.Container(
                content=ft.Row(
                    controls=[
                        ft.Container(
                            content=ft.Text(nombre[0].upper(), size=13, color=color_rol, weight=ft.FontWeight.W_700),
                            bgcolor=ft.colors.with_opacity(0.10, color_rol),
                            border_radius=20, width=36, height=36,
                            alignment=ft.alignment.center,
                        ),
                        ft.Column(
                            controls=[
                                ft.Text(nombre,       size=13, color=TEXT_PRIMARY, weight=ft.FontWeight.W_500),
                                ft.Text(f"@{usuario}", size=11, color=TEXT_MUTED),
                            ],
                            spacing=2,
                            expand=True,
                        ),
                        tag(rol, color_rol),
                        ft.Container(width=12),
                        tag("activo" if activo else "inactivo", color_estado),
                        ft.Container(width=12),
                        ft.IconButton(icon=ft.icons.EDIT_OUTLINED,  icon_color=TEXT_MUTED,  icon_size=16, tooltip="Editar"),
                        ft.IconButton(icon=ft.icons.BLOCK_ROUNDED,  icon_color=ACCENT_RED,  icon_size=16, tooltip="Desactivar"),
                    ],
                    spacing=0,
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                ),
                bgcolor=BG_CARD,
                border_radius=10,
                border=ft.border.all(1, BORDER),
                padding=ft.padding.symmetric(horizontal=16, vertical=12),
            )

        def campo(label, icono, password=False):
            return ft.TextField(
                label=label,
                prefix_icon=icono,
                password=password,
                can_reveal_password=password,
                expand=True,
                border_color=BORDER_LIGHT,
                focused_border_color=ACCENT_BLUE,
                label_style=ft.TextStyle(color=TEXT_MUTED),
                text_style=ft.TextStyle(color=TEXT_PRIMARY),
                cursor_color=ACCENT_BLUE,
                bgcolor=BG_INPUT,
                border_radius=8,
            )

        return ft.Column(
            controls=[
                ft.Row(
                    controls=[
                        ft.Column(
                            controls=[
                                ft.Text("Gestión de staff", size=22, weight=ft.FontWeight.W_700, color=TEXT_PRIMARY),
                                ft.Text("Administra empleados y accesos", size=13, color=TEXT_MUTED),
                            ],
                            spacing=2,
                            expand=True,
                        ),
                    ],
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                ),
                ft.Container(height=24),
                ft.Container(
                    content=ft.Column(
                        controls=[
                            sec_label("Agregar nuevo empleado"),
                            ft.Container(height=16),
                            ft.Row(
                                controls=[
                                    campo("Nombre completo",  ft.icons.PERSON_OUTLINE),
                                    campo("Usuario",          ft.icons.ALTERNATE_EMAIL_ROUNDED),
                                    campo("Contraseña",       ft.icons.LOCK_OUTLINE, password=True),
                                    ft.Dropdown(
                                        label="Rol",
                                        width=140,
                                        border_color=BORDER_LIGHT,
                                        focused_border_color=ACCENT_BLUE,
                                        label_style=ft.TextStyle(color=TEXT_MUTED),
                                        text_style=ft.TextStyle(color=TEXT_PRIMARY),
                                        bgcolor=BG_INPUT,
                                        border_radius=8,
                                        options=[
                                            ft.dropdown.Option("empleado", "Empleado"),
                                            ft.dropdown.Option("admin",    "Admin"),
                                        ],
                                        value="empleado",
                                    ),
                                ],
                                spacing=12,
                            ),
                            ft.Container(height=16),
                            ft.Row(
                                controls=[
                                    ft.Container(expand=True),
                                    ft.Container(
                                        content=ft.Text("GUARDAR EMPLEADO", size=12, weight=ft.FontWeight.W_700, color=BG_BASE),
                                        bgcolor=ACCENT_BLUE,
                                        border_radius=8,
                                        padding=ft.padding.symmetric(horizontal=20, vertical=12),
                                        ink=True,
                                    ),
                                ],
                            ),
                        ],
                        spacing=0,
                    ),
                    bgcolor=BG_CARD,
                    border_radius=12,
                    border=ft.border.all(1, BORDER),
                    padding=20,
                ),
                ft.Container(height=20),
                sec_label("Empleados registrados"),
                ft.Container(height=12),
                ft.Column(
                    controls=[
                        staff_row("Administrador",  "admin",   "admin",    True),
                        staff_row("Carlos Méndez",  "carlos",  "empleado", True),
                        staff_row("Laura Sánchez",  "laura",   "empleado", True),
                        staff_row("Roberto Díaz",   "roberto", "empleado", False),
                    ],
                    spacing=8,
                ),
            ],
            spacing=0,
            scroll=ft.ScrollMode.AUTO,
            expand=True,
        )

    # ── INVENTARIO ────────────────────────────────────────────────────────────
    def view_inventario():
        def producto_row(nombre, precio, descuento, stock):
            precio_final = precio * (1 - descuento / 100)
            color_stock  = ACCENT_EMERALD if stock > 5 else (ACCENT_AMBER if stock > 0 else ACCENT_RED)
            return ft.Container(
                content=ft.Row(
                    controls=[
                        ft.Column(
                            controls=[
                                ft.Text(nombre, size=13, color=TEXT_PRIMARY, weight=ft.FontWeight.W_500),
                                ft.Text(f"Stock: {stock} unidades", size=10, color=color_stock),
                            ],
                            spacing=2,
                            expand=True,
                        ),
                        ft.TextField(
                            value=str(precio), prefix_text="$", width=110,
                            border_color=BORDER_LIGHT, focused_border_color=ACCENT_BLUE,
                            text_style=ft.TextStyle(color=TEXT_PRIMARY, size=13),
                            bgcolor=BG_INPUT, border_radius=8,
                            content_padding=ft.padding.symmetric(horizontal=12, vertical=8),
                        ),
                        ft.TextField(
                            value=str(int(descuento)), suffix_text="%", width=90,
                            border_color=BORDER_LIGHT, focused_border_color=ACCENT_AMBER,
                            text_style=ft.TextStyle(color=TEXT_PRIMARY, size=13),
                            bgcolor=BG_INPUT, border_radius=8,
                            content_padding=ft.padding.symmetric(horizontal=12, vertical=8),
                        ),
                        ft.Container(
                            content=ft.Text(f"${precio_final:.0f}", size=13, color=ACCENT_EMERALD, weight=ft.FontWeight.W_700),
                            width=80,
                            alignment=ft.alignment.center,
                        ),
                        ft.Container(
                            content=ft.Text("Guardar", size=11, color=ACCENT_BLUE, weight=ft.FontWeight.W_600),
                            bgcolor=ft.colors.with_opacity(0.08, ACCENT_BLUE),
                            border=ft.border.all(1, ft.colors.with_opacity(0.20, ACCENT_BLUE)),
                            border_radius=6,
                            padding=ft.padding.symmetric(horizontal=12, vertical=8),
                            ink=True,
                        ),
                    ],
                    spacing=12,
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                ),
                bgcolor=BG_CARD,
                border_radius=10,
                border=ft.border.all(1, BORDER),
                padding=ft.padding.symmetric(horizontal=16, vertical=12),
            )

        return ft.Column(
            controls=[
                ft.Row(
                    controls=[
                        ft.Column(
                            controls=[
                                ft.Text("Inventario y precios", size=22, weight=ft.FontWeight.W_700, color=TEXT_PRIMARY),
                                ft.Text("Modifica precios y descuentos", size=13, color=TEXT_MUTED),
                            ],
                            spacing=2,
                            expand=True,
                        ),
                        action_btn("Nuevo producto", ft.icons.ADD_BOX_OUTLINED, ACCENT_EMERALD),
                    ],
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                ),
                ft.Container(height=24),
                ft.Container(
                    content=ft.Row(
                        controls=[
                            ft.Text("Producto",   size=10, color=TEXT_MUTED, weight=ft.FontWeight.W_700, expand=True),
                            ft.Text("Precio",     size=10, color=TEXT_MUTED, weight=ft.FontWeight.W_700, width=110),
                            ft.Text("Descuento",  size=10, color=TEXT_MUTED, weight=ft.FontWeight.W_700, width=90),
                            ft.Text("Final",      size=10, color=TEXT_MUTED, weight=ft.FontWeight.W_700, width=80, text_align=ft.TextAlign.CENTER),
                            ft.Container(width=80),
                        ],
                        spacing=12,
                    ),
                    padding=ft.padding.symmetric(horizontal=16, vertical=8),
                ),
                ft.Column(
                    controls=[
                        producto_row("Proteína Whey 1kg",  450, 0,  10),
                        producto_row("Guantes de Box",     280, 10,  5),
                        producto_row("Cuerda para saltar",  85, 0,  20),
                        producto_row("Cinturón Lumbar",    320, 5,   3),
                        producto_row("Shaker 700ml",        95, 0,  15),
                        producto_row("Creatina 300g",      380, 0,   2),
                    ],
                    spacing=8,
                ),
            ],
            spacing=0,
            scroll=ft.ScrollMode.AUTO,
            expand=True,
        )

    # ── REPORTES ──────────────────────────────────────────────────────────────
    def view_reportes():
        def venta_row(producto, cantidad, precio, descuento, cliente, empleado, hora):
            total = precio * cantidad * (1 - descuento / 100)
            return ft.Container(
                content=ft.Row(
                    controls=[
                        ft.Column(
                            controls=[
                                ft.Text(producto,              size=12, color=TEXT_PRIMARY, weight=ft.FontWeight.W_500),
                                ft.Text(cliente or "Sin cliente", size=10, color=TEXT_MUTED),
                            ],
                            spacing=2,
                            expand=True,
                        ),
                        ft.Text(f"×{cantidad}",                  size=12, color=TEXT_MUTED,    width=30),
                        ft.Text(f"${precio}",                    size=12, color=TEXT_PRIMARY,  width=60),
                        ft.Text(f"-{int(descuento)}%" if descuento else "—", size=11,
                                color=ACCENT_AMBER if descuento else TEXT_MUTED, width=45),
                        ft.Text(f"${total:.0f}",                 size=13, color=ACCENT_EMERALD, weight=ft.FontWeight.W_700, width=70),
                        ft.Text(empleado,                        size=10, color=TEXT_MUTED,    width=80),
                        ft.Text(hora,                            size=10, color=TEXT_MUTED,    width=50),
                    ],
                    spacing=8,
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                ),
                bgcolor=BG_CARD,
                border_radius=8,
                border=ft.border.all(1, BORDER),
                padding=ft.padding.symmetric(horizontal=16, vertical=10),
            )

        return ft.Column(
            controls=[
                ft.Row(
                    controls=[
                        ft.Column(
                            controls=[
                                ft.Text("Reporte del día", size=22, weight=ft.FontWeight.W_700, color=TEXT_PRIMARY),
                                ft.Text("Ventas registradas hoy", size=13, color=TEXT_MUTED),
                            ],
                            spacing=2,
                            expand=True,
                        ),
                        action_btn("Actualizar", ft.icons.REFRESH_ROUNDED, ACCENT_DIM),
                    ],
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                ),
                ft.Container(height=20),
                ft.Row(
                    controls=[
                        metric_card("Total vendido",        "$2,840", "12 transacciones",     ft.icons.POINT_OF_SALE_OUTLINED,   ACCENT_EMERALD),
                        metric_card("Membresías cobradas",  "$1,400", "4 renovaciones",       ft.icons.CARD_MEMBERSHIP_OUTLINED, ACCENT_BLUE),
                        metric_card("Productos vendidos",   "$1,440", "8 ventas inventario",  ft.icons.INVENTORY_2_OUTLINED,     ACCENT_AMBER),
                    ],
                    spacing=12,
                ),
                ft.Container(height=24),
                ft.Container(
                    content=ft.Row(
                        controls=[
                            ft.Text("Producto / Cliente", size=10, color=TEXT_MUTED, weight=ft.FontWeight.W_700, expand=True),
                            ft.Text("Cant.",   size=10, color=TEXT_MUTED, weight=ft.FontWeight.W_700, width=30),
                            ft.Text("Precio",  size=10, color=TEXT_MUTED, weight=ft.FontWeight.W_700, width=60),
                            ft.Text("Desc.",   size=10, color=TEXT_MUTED, weight=ft.FontWeight.W_700, width=45),
                            ft.Text("Total",   size=10, color=TEXT_MUTED, weight=ft.FontWeight.W_700, width=70),
                            ft.Text("Empleado",size=10, color=TEXT_MUTED, weight=ft.FontWeight.W_700, width=80),
                            ft.Text("Hora",    size=10, color=TEXT_MUTED, weight=ft.FontWeight.W_700, width=50),
                        ],
                        spacing=8,
                    ),
                    padding=ft.padding.symmetric(horizontal=16, vertical=8),
                ),
                ft.Column(
                    controls=[
                        venta_row("Proteína Whey 1kg", 2, 450, 0,   "Ana Torres",   "Carlos", "09:14"),
                        venta_row("Guantes de Box",    1, 280, 10,  "Luis Ramírez", "Laura",  "10:32"),
                        venta_row("Creatina 300g",     1, 380, 0,   None,           "Carlos", "11:05"),
                        venta_row("Shaker 700ml",      3,  95, 0,   "Pedro Hdz.",   "Laura",  "12:18"),
                    ],
                    spacing=6,
                ),
            ],
            spacing=0,
            scroll=ft.ScrollMode.AUTO,
            expand=True,
        )

    # ── MIEMBROS ──────────────────────────────────────────────────────────────
    def view_miembros():
        def miembro_row(nombre, plan, estado, dias, telefono):
            color_estado = (
                ACCENT_EMERALD if estado == "Al corriente" else
                ACCENT_AMBER   if estado == "Por vencer"  else
                ACCENT_RED
            )
            return ft.Container(
                content=ft.Row(
                    controls=[
                        ft.Container(
                            content=ft.Text(nombre[0].upper(), size=12, color=ACCENT_BLUE, weight=ft.FontWeight.W_700),
                            bgcolor=ft.colors.with_opacity(0.10, ACCENT_BLUE),
                            border_radius=20, width=34, height=34,
                            alignment=ft.alignment.center,
                        ),
                        ft.Column(
                            controls=[
                                ft.Text(nombre,    size=13, color=TEXT_PRIMARY, weight=ft.FontWeight.W_500),
                                ft.Text(telefono,  size=10, color=TEXT_MUTED),
                            ],
                            spacing=2,
                            expand=True,
                        ),
                        tag(plan,    ACCENT_DIM),
                        ft.Container(width=8),
                        tag(estado,  color_estado),
                        ft.Container(width=8),
                        ft.Text(dias, size=10, color=TEXT_MUTED, width=60),
                        ft.IconButton(icon=ft.icons.AUTORENEW_ROUNDED,  icon_color=ACCENT_EMERALD, icon_size=16, tooltip="Renovar"),
                        ft.IconButton(icon=ft.icons.PERSON_OFF_OUTLINED, icon_color=ACCENT_RED,    icon_size=16, tooltip="Dar de baja"),
                    ],
                    spacing=0,
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                ),
                bgcolor=BG_CARD,
                border_radius=10,
                border=ft.border.all(1, BORDER),
                padding=ft.padding.symmetric(horizontal=16, vertical=10),
            )

        return ft.Column(
            controls=[
                ft.Row(
                    controls=[
                        ft.Column(
                            controls=[
                                ft.Text("Todos los miembros", size=22, weight=ft.FontWeight.W_700, color=TEXT_PRIMARY),
                                ft.Text("Vista completa de clientes activos", size=13, color=TEXT_MUTED),
                            ],
                            spacing=2,
                            expand=True,
                        ),
                        ft.TextField(
                            hint_text="Buscar miembro...",
                            prefix_icon=ft.icons.SEARCH_ROUNDED,
                            width=240,
                            border_color=BORDER_LIGHT,
                            focused_border_color=ACCENT_BLUE,
                            hint_style=ft.TextStyle(color=TEXT_MUTED),
                            text_style=ft.TextStyle(color=TEXT_PRIMARY),
                            cursor_color=ACCENT_BLUE,
                            bgcolor=BG_INPUT,
                            border_radius=8,
                            content_padding=ft.padding.symmetric(horizontal=12, vertical=10),
                        ),
                    ],
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                ),
                ft.Container(height=20),
                ft.Column(
                    controls=[
                        miembro_row("Ana Torres",       "Mensual",     "Al corriente", "15 días", "222-111-1111"),
                        miembro_row("Luis Ramírez",     "Trimestral",  "Por vencer",   "3 días",  "222-222-2222"),
                        miembro_row("María González",   "Mensual",     "Vencido",      "-5 días", "222-333-3333"),
                        miembro_row("Pedro Hernández",  "Anual",       "Al corriente", "20 días", "222-444-4444"),
                        miembro_row("Sofía Martínez",   "Mensual",     "Vencido",      "-20 días","222-555-5555"),
                    ],
                    spacing=8,
                ),
            ],
            spacing=0,
            scroll=ft.ScrollMode.AUTO,
            expand=True,
        )

    # ── Mapa de vistas ────────────────────────────────────────────────────────
    views_map = {
        "dashboard":  view_dashboard,
        "staff":      view_staff,
        "inventario": view_inventario,
        "reportes":   view_reportes,
        "miembros":   view_miembros,
    }

    def cambiar_seccion(ruta):
        active_route.current = ruta
        for k, ref in sidebar_refs.items():
            sel = k == ruta
            ref.current.bgcolor = ft.colors.with_opacity(0.06, ACCENT_BLUE) if sel else "transparent"
            ref.current.border  = ft.border.only(left=ft.BorderSide(2, ACCENT_BLUE if sel else "transparent"))
            row = ref.current.content
            row.controls[0].color  = ACCENT if sel else TEXT_MUTED
            row.controls[1].color  = ACCENT if sel else TEXT_MUTED
            row.controls[1].weight = ft.FontWeight.W_600 if sel else ft.FontWeight.W_400
        content_area.current.content = ft.Container(
            content=views_map[ruta](),
            padding=ft.padding.all(28),
            expand=True,
        )
        page.update()

    # ── Sidebar ───────────────────────────────────────────────────────────────
    def make_sidebar_item(ruta, label_texto, icono):
        sel = ruta == active_route.current
        ref = ft.Ref[ft.Container]()
        sidebar_refs[ruta] = ref
        return ft.Container(
            ref=ref,
            content=ft.Row(
                controls=[
                    ft.Icon(icono, color=ACCENT if sel else TEXT_MUTED, size=17),
                    ft.Text(label_texto, size=12,
                            color=ACCENT if sel else TEXT_MUTED,
                            weight=ft.FontWeight.W_600 if sel else ft.FontWeight.W_400),
                ],
                spacing=12,
            ),
            bgcolor=ft.colors.with_opacity(0.06, ACCENT_BLUE) if sel else "transparent",
            border=ft.border.only(left=ft.BorderSide(2, ACCENT_BLUE if sel else "transparent")),
            border_radius=ft.border_radius.only(top_right=8, bottom_right=8),
            padding=ft.padding.symmetric(horizontal=18, vertical=12),
            ink=True,
            on_click=lambda e, r=ruta: cambiar_seccion(r),
        )

    sidebar_items_def = [
        ("dashboard",  "Dashboard",  ft.icons.GRID_VIEW_ROUNDED),
        ("miembros",   "Miembros",   ft.icons.PEOPLE_OUTLINE_ROUNDED),
        ("staff",      "Staff",      ft.icons.BADGE_OUTLINED),
        ("inventario", "Inventario", ft.icons.INVENTORY_2_OUTLINED),
        ("reportes",   "Reportes",   ft.icons.BAR_CHART_ROUNDED),
    ]

    sidebar = ft.Container(
        content=ft.Column(
            controls=[
                ft.Container(
                    content=ft.Column(
                        controls=[
                            ft.Row(
                                controls=[
                                    ft.Icon(ft.icons.FITNESS_CENTER_ROUNDED, color=ACCENT_BLUE, size=18),
                                    ft.Text("GYM", size=15, weight=ft.FontWeight.W_800, color=TEXT_PRIMARY),
                                ],
                                spacing=8,
                            ),
                            ft.Text("ADMIN", size=8, color=TEXT_MUTED, weight=ft.FontWeight.W_700),
                        ],
                        spacing=2,
                    ),
                    padding=ft.padding.symmetric(horizontal=18, vertical=22),
                ),
                ft.Container(height=1, bgcolor=BORDER),
                ft.Container(height=12),
                *[make_sidebar_item(r, l, i) for r, l, i in sidebar_items_def],
                ft.Container(expand=True),
                ft.Container(height=1, bgcolor=BORDER),
                ft.Container(
                    content=ft.Column(
                        controls=[
                            ft.Row(
                                controls=[
                                    ft.Container(
                                        content=ft.Text(nombre_admin[0].upper(), size=11, color=ACCENT_BLUE, weight=ft.FontWeight.W_700),
                                        bgcolor=ft.colors.with_opacity(0.12, ACCENT_BLUE),
                                        border_radius=20, width=32, height=32,
                                        alignment=ft.alignment.center,
                                    ),
                                    ft.Column(
                                        controls=[
                                            ft.Text(nombre_admin,    size=11, color=TEXT_PRIMARY, weight=ft.FontWeight.W_600),
                                            ft.Text("Administrador", size=9,  color=TEXT_MUTED),
                                        ],
                                        spacing=1,
                                        expand=True,
                                    ),
                                ],
                                spacing=10,
                            ),
                            ft.Container(
                                content=ft.Row(
                                    controls=[
                                        ft.Icon(ft.icons.LOGOUT_ROUNDED, color=ACCENT_RED, size=14),
                                        ft.Text("Cerrar sesión", size=11, color=ACCENT_RED),
                                    ],
                                    spacing=8,
                                ),
                                ink=True,
                                on_click=on_logout,
                                padding=ft.padding.symmetric(vertical=8),
                                border_radius=6,
                            ),
                        ],
                        spacing=10,
                    ),
                    padding=ft.padding.symmetric(horizontal=18, vertical=16),
                ),
            ],
            spacing=0,
            expand=True,
        ),
        width=200,
        bgcolor=SIDEBAR_BG,
        border=ft.border.only(right=ft.BorderSide(1, BORDER)),
    )

    topbar = ft.Container(
        content=ft.Row(
            controls=[
                ft.Text("Panel de administración", size=12, color=TEXT_MUTED),
                ft.Container(expand=True),
                ft.Row(
                    controls=[
                        ft.Container(width=6, height=6, bgcolor=ACCENT_EMERALD, border_radius=3),
                        ft.Text("Sistema activo", size=10, color=TEXT_MUTED),
                    ],
                    spacing=6,
                ),
            ],
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
        ),
        height=48,
        bgcolor=BG_SURFACE,
        border=ft.border.only(bottom=ft.BorderSide(1, BORDER)),
        padding=ft.padding.symmetric(horizontal=24),
    )

    main_area = ft.Container(
        ref=content_area,
        content=ft.Container(
            content=view_dashboard(),
            padding=ft.padding.all(28),
            expand=True,
        ),
        expand=True,
        bgcolor=BG_BASE,
    )

    body = ft.Row(controls=[sidebar, main_area], spacing=0, expand=True)

    return ft.View(
        route="/admin",
        controls=[
            ft.Column(controls=[topbar, body], spacing=0, expand=True)
        ],
        padding=0,
        bgcolor=BG_BASE,
    )
