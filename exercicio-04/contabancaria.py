from abc import ABC, abstractmethod

class ContaBancaria(ABC):
    def __init__(self,numero_conta,titular):
        self.numero_conta = numero_conta
        self.titular = titular
        self.saldo = 0


    @abstractmethod
    def depositar(self, valor):
        pass


    @abstractmethod
    def sacar (self, valor):
        pass


    @abstractmethod
    def get_saldo(self):
        pass


# subclasses concretas
class ContaCorrente(ContaBancaria):
    def __init__(self, numero_conta, titular, cheque_especial = 300):
        super().__init__(numero_conta,titular)
        self.cheque_especial = cheque_especial


    def depositar(self, valor):
        if self.cheque_especial < 300:
            if self.cheque_especial + valor > 300:
                self.saldo = (self.cheque_especial + valor) - 300
                self.cheque_especial = 300
            else:
                self.cheque_especial += valor
        else:
            self.saldo += valor


    def sacar(self, valor):
        if self.saldo - valor < 0:
            if self.cheque_especial - abs(self.saldo - valor) < 0:
                print('Limite excedido')
            else:
                self.cheque_especial -= abs(self.saldo - valor)
                self.saldo = 0
        else:
            self.saldo -= valor


    def get_saldo(self):
        return self.saldo


class ContaPoupanca(ContaBancaria):
    def __init__(self, numero_conta, titular):
        super().__init__(numero_conta, titular)
        self.taxa_juros = 1.105


    def depositar(self, valor:float):
        self.saldo += valor


    def get_taxajuros(self):
        return self.taxa_juros


    def sacar(self, valor):
        if self.saldo < valor:
            print('Saldo insuficiente')
        else:
            self.saldo -= valor


    def get_saldo(self):
        return self.saldo


    def correcao_juros(self):
        self.saldo *= self.taxa_juros