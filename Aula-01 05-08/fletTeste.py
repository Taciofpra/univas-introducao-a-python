import flet as ft

def main(Pagina: ft.Page):


    def click(e: ft.Event[ft.Button]):
        textoCaixa.value = (input.value)
        Pagina.add(textoCaixa)
        

    botao = ft.Button("Teste", on_click=click)
    input = ft.TextField(hint_text="Digie seu nome")
    textoCaixa = ft.Text

    Pagina.add(
        input,
        botao
    )

ft.run(main)
    