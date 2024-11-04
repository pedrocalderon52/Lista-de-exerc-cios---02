class Pneu():
    def __init__(self, tamanho, pressao) -> None:
        self.tamanho = tamanho
        self.pressao = pressao
        self.tamanho_sulco = 5.0

    def status_pneu(self):
        if self.tamanho_sulco <= 1.6:
            print(f"Pneu está careca, troque-o. O tamanho é {self.tamanho}. A pressão é {self.pressao}")
        else: 
            print(f"Pneu está ok, vence daqui a {(self.tamanho_sulco - 1.6) * 13889:.2f} kms.  O tamanho é {self.tamanho}. A pressão é {self.pressao}")


class Motor():
    def __init__(self, cilindros, potencia) -> None:
        self.cilindros = cilindros
        self.oleo = 8
        self.potencia = potencia


    def status_motor(self):
        if self.oleo <= 1.8:
            print(f"Precisa trocar o óleo. Nível: {self.oleo:.2f} litros. Ele tem {self.cilindros} cilindros. A potência é {self.potencia}")
        else:
            print(f"Óleo ok. Nível: {self.oleo:.2f} litros. Ele tem {self.cilindros} cilindros. A potência é {self.potencia}")

class Veiculo(Pneu, Motor):
    def __init__(self, tamanho, pressao, cilindros, potencia) -> None:
        super().__init__(tamanho, pressao)
        Motor.__init__(self, cilindros, potencia)
        self.oleo = 8


    
    def status(self):
        self.status_motor()
        self.status_pneu()


    def andar(self, quilometros):
        print("\n vr", ("u" * (int(quilometros/1000) + 2)), "mm!!!!!!\n", sep="")
        self.oleo -= 0.0005 * quilometros
        self.tamanho_sulco -= 0.000072 * quilometros
