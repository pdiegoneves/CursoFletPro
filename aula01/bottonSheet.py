import flet as ft

def main(page: ft.Page):
    def show_bs(e):
        page.overlay.append(bs)
        bs.open = True
        page.update()

    def close_bs(e):
        bs.open = False
        page.update()


    bs = ft.BottomSheet(
        content=ft.Container(
            ft.Column(
                controls=[
                    ft.Text(value="Título", style=ft.TextThemeStyle.TITLE_MEDIUM),
                    ft.Text(value="Conteudo do bottomshrret", style=ft.TextThemeStyle.HEADLINE_MEDIUM),
                    ft.FilledButton(text="Fechar", on_click=close_bs)
                ]
            ),
            padding=ft.padding.all(20),
        ),
        dismissible=False,
        enable_drag=True,
        is_scroll_controlled=False,
        maintain_bottom_view_insets_padding=True,
        show_drag_handle=True
    )

    btn = ft.ElevatedButton(text="Abrir", on_click=show_bs)
    page.add(btn)
    # page.overlay.append(btn)
    page.update()


if __name__ == "__main__":
    ft.app(target=main)