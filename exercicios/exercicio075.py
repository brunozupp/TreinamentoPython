if __name__ == '__main__':

    tupla = ()

    for i in range(0,4):
        valor = int(input("Digite um número inteiro = "))

        tupla += (valor,)

    # A)
    print(f"Apareceu o número 9 um total de {tupla.count(9)} vezes")

    # B)
    print(f"O número 3 foi digitado inicialmente na posição {tupla.index(3)}")

    # C)
    tuplaNumerosPares = ()

    for numero in tupla:
        if numero % 2 == 0:
            tuplaNumerosPares += (numero,)

    print(f"Números pares = {tuplaNumerosPares}")