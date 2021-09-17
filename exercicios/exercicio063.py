if __name__ == '__main__':

    primeiroNumero = 0
    segundoNumero = 1

    sequencia = int(input("Digite um número = "))

    print(primeiroNumero)
    print(segundoNumero)

    count = 0

    while count < sequencia:
        auxiliar = primeiroNumero
        primeiroNumero = segundoNumero
        segundoNumero = auxiliar + primeiroNumero

        print(segundoNumero)
        count += 1

