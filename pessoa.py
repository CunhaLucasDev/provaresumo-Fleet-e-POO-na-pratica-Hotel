class Pessoa:
    def __init__(self, nome, telefone, email):
        self.__nome = nome
        self.__telefone = telefone
        self.__email = email

    def get_nome(self):
        return self.__nome

    def get_telefone(self):
        return self.__telefone

    def get_email(self):
        return self.__email

    def exibir_informacoes(self):
        return f"Nome: {self.__nome}, Telefone: {self.__telefone}, Email: {self.__email}"
