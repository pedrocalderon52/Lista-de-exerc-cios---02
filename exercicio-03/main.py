import turtle as tl
from ponto import Ponto

ponto = Ponto(300, 200, "green", 7)
tl.color(ponto.cor)
tl.width(ponto.grossura)
tl.goto(ponto.x, ponto.y)

tl.done()