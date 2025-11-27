from pessoa import Pessoa

class Cliente(Pessoa):
    def __init__(self, nome, telefone, email, id_unico):
        super().__init__(nome, telefone, email)
        self.__id_unico = id_unico

    def get_id(self):
        return self.__id_unico

    def exibir_informacoes(self):
        return (
            f"Cliente: {self.get_nome()} (ID: {self.__id_unico}), "
            f"Telefone: {self.get_telefone()}, Email: {self.get_email()}"
        )
