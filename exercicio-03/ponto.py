import turtle as tl
import math as m
class Ponto:
    def __init__(self, x, y, cor, grossura):
        self.prox_x = x
        self.prox_y = y
        self.cor = cor
        self.grossura = grossura
        self.x = 0
        self.y = 0
        tl.color(self.cor)
        tl.width(grossura)


    def set_cor(self, cor):
        tl.color(cor)
        self.cor = cor


    def set_grossura(self, grossura):
        self.grossura = grossura
        tl.width(grossura)


    def set_ponto(self, x, y):
        self.prox_x = x
        self.prox_y = y


    def andar_reto(self):
        tl.goto(self.prox_x, self.prox_y)
        self.x = self.prox_x
        self.y = self.prox_y


    def andar_tracejado(self):
        adjacente =  self.prox_x - self.x
        oposto = self.prox_y - self.y

        distancia = m.sqrt(adjacente ** 2 + oposto ** 2)
        
        angulo = m.degrees(m.atan(abs(oposto)/abs(adjacente)))
        if adjacente < 0: 
            if oposto < 0:
                tl.left(180 + angulo)
            else:
                tl.left(180-angulo)
        else:
            if oposto < 0:
                tl.left(0 - angulo)
            else:
                tl.left(0 + angulo)
        tl.fd(10)
        for _ in range(int(distancia // 20 - ((abs(10 - distancia % 20)) / 20))):
            tl.pendown()
            tl.fd(10)
            tl.penup()
            tl.fd(10)
        tl.pendown()
        tl.goto(self.prox_x, self.prox_y)
        self.x = self.prox_x
        self.y = self.prox_y
        tl.setheading(0)

        

    

        