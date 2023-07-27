class Cliente:

    def __init__(self, nome: str, cpf: str):
        self.__nome = nome
        self.__cpf = cpf
    
    @property
    def nome(self) -> str:
        return self.__nome.capitalize()
    
    @property
    def cpf(self) -> str:
        return self.__cpf
    
    def __str__(self) -> str:
        return f"Nome: {self.nome}, CPF: {self.cpf}"
