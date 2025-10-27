opcao = int(input("Informe uma opção:\n [1] Sacar\n [2] Extrato\n"))
if opcao == 1:
    valor = float(input("Informe o valor para saque: "))
elif opcao == 2:
    print("Exibindo o extrato...")
else:
    print("Opção inválida")
