import flet as ft
from gerenciador import GerenciadorDeReservas
from cliente import Cliente
from quarto import Quarto
from reserva import Reserva
from pessoa import Pessoa


def main(page: ft.Page):
    page.title = "Sistema de Reservas - Refúgio dos Sonhos"
    page.window_width = 900
    page.window_height = 700

    gerenciador = GerenciadorDeReservas()

    # Dados iniciais
    cliente_padrao = Cliente("Lucas", "99999999", "lucas@email.com", 1)
    quarto_padrao = Quarto(101, "Single", 200)
    gerenciador.adicionar_cliente(cliente_padrao)
    gerenciador.adicionar_quarto(quarto_padrao)

    # Componentes da interface
    cliente_dropdown = ft.Dropdown(
        label="Cliente",
        options=[ft.dropdown.Option(str(cliente_padrao.get_id()))],
        width=200
    )

    quarto_dropdown = ft.Dropdown(
        label="Quarto",
        options=[ft.dropdown.Option(str(quarto_padrao.get_numero()))],
        width=200
    )

    checkin_input = ft.TextField(label="Check-in (YYYY-MM-DD)", width=200)
    checkout_input = ft.TextField(label="Check-out (YYYY-MM-DD)", width=200)

    reservas_list = ft.Column()

    def reservar_click(e):
        cliente_id = int(cliente_dropdown.value)
        quarto_num = int(quarto_dropdown.value)
        checkin = checkin_input.value
        checkout = checkout_input.value

        cliente = next((c for c in gerenciador.listar_clientes() if c.get_id() == cliente_id), None)
        quarto = next((q for q in gerenciador.listar_quartos() if q.get_numero() == quarto_num), None)

        reserva = gerenciador.criar_reserva(cliente, quarto, checkin, checkout)
        if reserva:
            reservas_list.controls.append(ft.Text(reserva.exibir_informacoes()))
            page.update()
        else:
            page.snack_bar = ft.SnackBar(ft.Text("Quarto indisponível!"))
            page.snack_bar.open = True
            page.update()

    reservar_btn = ft.ElevatedButton("Reservar", on_click=reservar_click)

    page.add(
        ft.Text("Criar Reserva", size=20, weight="bold"),
        cliente_dropdown,
        quarto_dropdown,
        checkin_input,
        checkout_input,
        reservar_btn,
        ft.Divider(),
        ft.Text("Reservas Atuais", size=18),
        reservas_list
    )
ft.app(target=main)