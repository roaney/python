print("\n--- Usando CONTINUE para pular pares ---")
for numero in range(1, 11):
    if numero % 2 == 0:
        print(f"O número {numero} é par. Pulando...")
        continue
    print(f"✅ Processando número ímpar: {numero}")
