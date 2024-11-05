from contabancaria import ContaBancaria, ContaCorrente, ContaPoupanca

poupanca = ContaPoupanca("04072012", "Lucas Oliveira de Carvalho Mendes")
corrente = ContaCorrente("04072012", "Lucas Oliveira de Carvalho Mendes")

poupanca.depositar(500)
poupanca.correcao_juros()
print(poupanca.get_taxajuros())
print("\n\n\n")
print(poupanca.get_saldo())
