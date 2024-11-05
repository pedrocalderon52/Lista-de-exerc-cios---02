from veiculo import Pneu, Veiculo, Motor

pneu1 = Pneu(4, 40)
motor1 = Motor(3, 105)

hb20_do_isaac = Veiculo(pneu1.tamanho, pneu1.pressao, motor1.cilindros, motor1.potencia)

hb20_do_isaac.andar(9000)
hb20_do_isaac.status()
hb20_do_isaac.andar(800)
hb20_do_isaac.status()
hb20_do_isaac.andar(41000)
hb20_do_isaac.status()