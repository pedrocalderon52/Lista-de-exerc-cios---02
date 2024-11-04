import turtle as tl

class Forma():
    def __init__(self, cor) -> None:
        self.cor = cor
    def desenhar():
        pass

class Circulo(Forma):
    def __init__(self, cor, raio) -> None:
        super().__init__(cor)
        self.raio = raio


    def desenhar(self):
        tl.color(self.cor)
        tl.fillcolor(self.cor)
        tl.begin_fill()
        tl.circle(self.raio)
        tl.end_fill()

    
class Quadrado(Forma):
    def __init__(self, cor, lado) -> None:
        super().__init__(cor)
        self.lado = lado


    def desenhar(self):  
        tl.color(self.cor)
        tl.fillcolor(self.cor)  

        tl.begin_fill()
        for _ in range(4):
            tl.fd(self.lado)
            tl.right(90)
        tl.end_fill()