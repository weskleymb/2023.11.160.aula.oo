from model.conta_corrente import ContaCorrente
from model.conta_poupanca import ContaPoupanca
from model.cliente import Cliente

joao = Cliente("joão", "123.456.789-00")
conta_joao = ContaCorrente(123, 456, joao, 0.0, 1000.0)
print(f"Titular: {conta_joao.titular.nome}, Saldo: {conta_joao.saldo}")

emily = Cliente("emily", "987.654.321-00")
conta_emily = ContaPoupanca(123, 789, emily, 3000.0)
print(f"Titular: {conta_emily.titular.nome}, Saldo: {conta_emily.saldo}")

conta_joao.transferir(conta_emily, 100.0)

conta_emily.render()
conta_emily.render()


print(f"Titular: {conta_joao.titular.nome}, Saldo: {conta_joao.saldo}")
print(f"Titular: {conta_emily.titular.nome}, Saldo: {conta_emily.saldo}")