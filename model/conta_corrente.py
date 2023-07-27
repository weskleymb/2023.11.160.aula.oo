from model.conta import Conta

class ContaCorrente(Conta):
    
    __taxa = 1 / 100

    def __init__(self, agencia, numero, titular, saldo = 0.0, limite = 0.0):
        super().__init__(agencia, numero, titular, saldo)
        self.__limite = limite

    def sacar(self, valor):
        valor_taxa = valor * self.__taxa
        valor_a_sacar = valor + valor_taxa
        saldo_com_limite = self.saldo + self.__limite
        pode_sacar = valor_a_sacar <= saldo_com_limite
        if pode_sacar:
            self.saldo -= valor_a_sacar
            return True
        return False
