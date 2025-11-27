# gerenciador.py
from reserva import Reserva

class GerenciadorDeReservas:
    def __init__(self):
        self.__reservas = []
        self.__clientes = []
        self.__quartos = []

    def adicionar_cliente(self, cliente):
        self.__clientes.append(cliente)

    def adicionar_quarto(self, quarto):
        self.__quartos.append(quarto)

    def criar_reserva(self, cliente, quarto, check_in, check_out):
        if quarto.is_disponivel():
            reserva = Reserva(cliente, quarto, check_in, check_out)
            self.__reservas.append(reserva)
            return reserva
        return None

    def listar_reservas(self):
        return self.__reservas

    def listar_quartos(self):
        return self.__quartos

    def listar_clientes(self):
        return self.__clientes
