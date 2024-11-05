import turtle as tl
from ponto import Ponto


ponto = Ponto(-300, 200, "green", 7)
ponto.andar_tracejado()
ponto.set_ponto(311, 159)
ponto.andar_tracejado()
ponto.set_ponto(0, 0)
ponto.andar_tracejado()


tl.done()