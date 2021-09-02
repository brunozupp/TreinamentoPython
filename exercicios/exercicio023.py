def mostrar1digitos(digitos):
    print(f"unidade: {digitos[0]}")


def mostrar2digitos(digitos):
    print(f"unidade: {digitos[1]}")
    print(f"dezena: {digitos[0]}")


def mostrar3digitos(digitos):
    print(f"unidade: {digitos[2]}")
    print(f"dezena: {digitos[1]}")
    print(f"centena: {digitos[0]}")


def mostrar4digitos(digitos):
    print(f"unidade: {digitos[3]}")
    print(f"dezena: {digitos[2]}")
    print(f"centena: {digitos[1]}")
    print(f"milhar: {digitos[0]}")


if __name__ == '__main__':

    numero = int(input("Digite um número de 0 a 9999 = "))

    while numero < 0 or numero > 9999:
        numero = int(input("Digite um número de 0 a 9999 = "))

    numero = str(numero)

    digitos = list(numero)

    if len(digitos) == 4:
        mostrar4digitos(digitos)

    elif len(digitos) == 3:
        mostrar3digitos(digitos)

    elif len(digitos) == 2:
        mostrar2digitos(digitos)

    else:
        mostrar1digitos(digitos)
