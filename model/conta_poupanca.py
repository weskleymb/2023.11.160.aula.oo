from model.conta import Conta

class ContaPoupanca(Conta):

    __rendimento = 1 / 100

    def render(self):
        self.saldo += self.saldo * self.__rendimento

    def sacar(self, valor):
        pode_sacar = valor <= self.saldo
        if pode_sacar:
            self.saldo -= valor
            return True
        return False