from forma import Forma
from forma import Circulo, Quadrado
import turtle as tl

tl.width(6)

circulo = Circulo("green", 50)
quadrado = Quadrado("gray", 30)

quadrado.desenhar()
circulo.desenhar()
tl.mainloop()