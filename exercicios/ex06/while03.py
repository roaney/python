print("\n--- Loop com BREAK para validação ---")
while True:  # Cria um loop que seria infinito se não tivesse o 'break'
    senha = input("Digite a senha (ou 'sair' para encerrar): ")
    if senha == "1234":
        print("Senha correta. Acesso concedido!")
        break # Sai do loop 'while True'
    elif senha.lower() == "sair":
        print("Encerrando o programa.")
        break # Sai do loop 'while True'
    else:
        print("Senha incorreta. Tente novamente.")
