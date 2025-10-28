valor = float(input("Quanto você tem? "))

if valor >= 10000:
    print("Vamos para a Disney!")
else:
    if valor < 10000 and valor >= 5000:
        print("Visitar família.")
    else:
        print("Junte mais dinheiro.")

if valor >= 10000:
    print("Vamos para a Disney!")
elif valor < 10000 and valor >= 5000:
    print("Visitar família.")
else:
    print("Junte mais dinheiro.")
