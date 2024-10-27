import flet as ft

def main(page: ft.Page):
    ad1 = ft.AlertDialog(
        title= ft.Text("Confirmação"),
        content= ft.Text(value="Deseja continar?"),
        content_padding= ft.padding.all(30),
        inset_padding= ft.padding.all(10),
        modal= False,
        shape= ft.RoundedRectangleBorder(radius= 5),
        on_dismiss= lambda _: print("Dialog dismissed!"),

        actions=[
            ft.TextButton(text="Cancelar", style=ft.ButtonStyle(color=ft.colors.RED)),
            ft.ElevatedButton(text="Salvar", style=ft.ButtonStyle(bgcolor=ft.colors.GREEN, color= ft.colors.WHITE)),
        ],
    actions_alignment= ft.MainAxisAlignment.END
    )

    def open_ad(e):
        #page.dialog = ad1  # Deprecated
        page.overlay.append(ad1)
        ad1.open = True
        page.update()

    btn1 = ft.ElevatedButton(text="Abrir", on_click= open_ad)
    page.add(btn1)

if __name__ == "__main__":
    ft.app(target=main)