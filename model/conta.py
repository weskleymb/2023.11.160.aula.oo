from abc import ABC, abstractmethod
from model.cliente import Cliente

class Conta(ABC):

    # definicao dos atributos
    # definicao o construtor
    def __init__(self, agencia, numero, titular: Cliente, saldo = 0.0):
        self.__agencia = agencia
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo

    # definicao dos metodos
    def depositar(self, valor):
        pode_depositar = valor > 0 # regra para poder depositar
        if pode_depositar:
            self.__saldo += valor
            return True
        return False

    @abstractmethod
    def sacar(self, valor):
        pass

    def transferir(self, conta_destino, valor):
        pode_transferir = self.sacar(valor) # regra para poder transferir
        if pode_transferir:
            return conta_destino.depositar(valor)
        return False

    # definicao dos getters
    @property
    def titular(self):
        return self.__titular
    
    @property
    def saldo(self):
        return self.__saldo
    
    @saldo.setter
    def saldo(self, saldo):
        self.__saldo = saldo
    
    @property
    def agencia(self):
        return self.__agencia
    
    @property
    def numero(self):
        return self.__numero
    