class Reserva:
    def __init__(self, cliente, quarto, check_in, check_out):
        self.__cliente = cliente
        self.__quarto = quarto
        self.__check_in = check_in
        self.__check_out = check_out
        self.__status = "Ativa"
        quarto.reservar()

    def cancelar(self):
        self.__status = "Cancelada"
        self.__quarto.liberar()

    def exibir_informacoes(self):
        return (
            f"{self.__cliente.get_nome()} reservou {self.__quarto.get_tipo()} "
            f"(Quarto {self.__quarto.get_numero()}) de {self.__check_in} até {self.__check_out} "
            f"| Status: {self.__status}"
        )

    def get_cliente(self):
        return self.__cliente
