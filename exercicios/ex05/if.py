saldo = 1000.00
saque = float(input("Informe o valor do saque: "))
if saque <= saldo:
    print("Saque autorizado")
if saque > saldo:
    print("Saldo insuficiente")
