saldo_conta_normal = 1000.00
saldo_conta_universitaria = 500.00
conta = float(input("Qual conta deseja sacar?\n [1] Conta Normal\n [2] Conta Universitária\n"))
if conta == 1 :
    print("Conta normal selecionada.")
    saque = float(input("Qual o valor do saque? "))
    if saque <= saldo_conta_normal:
        print("Saque realizado!")
    else:
        print("Saldo insuficiente!")
elif conta == 2 :
    print("Conta universitária selecionada.")
    saque = float(input("Qual o valor do saque? "))
    if saque <= saldo_conta_universitaria:
        print("Saque realizado!")
    else:
        print("Saldo insuficiente!")
