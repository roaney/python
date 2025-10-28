saldo_conta_normal = 1000.00
saldo_conta_universitaria = 500.00
c_normal = False
c_universitaria = False
conta = float(input("Qual conta deseja sacar?\n [1] Conta Normal\n [2] Conta Universitária\n"))

if conta == 1:
    c_normal = True
    print("Conta normal selecionada.")
elif conta == 2:
    c_universitaria = True
    print("Conta universitária selecionada.")

saque = float(input("Qual o valor do saque? "))

if c_normal:
    if saque <= saldo_conta_normal:
        print("Saque realizado!")
    else:
        print("Saldo insuficiente!")
elif c_universitaria:
    if saque <= saldo_conta_universitaria:
        print("Saque realizado!")
    else:
        print("Saldo insuficiente!")
