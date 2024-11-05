import turtle as tl
from ponto import Ponto


ponto = Ponto(-300, 200, "green", 7)
ponto.andar_tracejado()
ponto.set_ponto(300, 150)
ponto.andar_tracejado()
ponto.set_ponto(0, 0)
ponto.andar_tracejado()





# vai ser adicionada uma opção de deixar a linha tracejada, fazer com pitágoras entre x e y
# distancia = raiz de ((x0 - x)² + (y0 - y)²)
# use trigonometria para descobrir o angulo
# a cada 2 cm, mais ou menos, ande com pen up, ande com pen down.
tl.done()