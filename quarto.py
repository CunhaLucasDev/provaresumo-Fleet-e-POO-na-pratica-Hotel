class Quarto:
    def __init__(self, numero, tipo, preco_diaria, disponivel=True):
        self.__numero = numero
        self.__tipo = tipo
        self.__preco_diaria = preco_diaria
        self.__disponivel = disponivel

    def get_numero(self):
        return self.__numero

    def get_tipo(self):
        return self.__tipo

    def get_preco_diaria(self):
        return self.__preco_diaria

    def is_disponivel(self):
        return self.__disponivel

    def reservar(self):
        if not self.__disponivel:
            raise Exception("Quarto já está ocupado.")
        self.__disponivel = False

    def liberar(self):
        self.__disponivel = True
