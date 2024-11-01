import flet as ft

def main(page: ft.Page):
    def close_banner(e):
        bn1.open = False
        page.update()

    def open_banner(e):
        page.overlay.append(bn1)
        bn1.open = True
        page.update()

    bn1 = ft.Banner(
        actions=[
            ft.TextButton(text="Cancelar",on_click=close_banner, style=ft.ButtonStyle(color=ft.colors.RED)),
            ft.ElevatedButton(text="Tentar novamente",on_click=close_banner, style=ft.ButtonStyle(bgcolor=ft.colors.GREEN, color= ft.colors.WHITE)),
        ],
        content=ft.Text(value="Banner 1"),
        content_padding=ft.padding.all(20),
        leading=ft.Icon(name=ft.icons.WARNING_AMBER, color=ft.colors.RED),
        force_actions_below=True,
        bgcolor=ft.colors.AMBER_100
    )

    # page.banner = bn1
    
    btn1 = ft.ElevatedButton(text="Abrir", on_click= open_banner)    
    page.add(btn1)
    page.update()

if __name__ == "__main__":
    ft.app(target=main)