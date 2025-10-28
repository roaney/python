palavra = input("Digite uma palavra: ")
VOGAIS = "AEIOU"
for letra in palavra:
    if letra.upper() in VOGAIS:
        print(letra, end = " ")
else:
    print("Executa no final do laço.")
