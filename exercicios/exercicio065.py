if __name__ == '__main__':

    sum = 0
    count = 0

    maior = 0
    menor = 0

    continuar = 1

    while continuar != 0:
        numero = int(input("Digite um número = "))

        if count == 0:
            maior = numero
            menor = numero
        else:
            if numero > maior:
                maior = numero

            if numero < menor:
                menor = numero

        sum += numero
        count += 1

        continuar = int(input("Digite 0 para sair ou qualquer outro número para continuar = "))

    print(f"A média é {sum / count}")
    print(f"A quantidade de números digitados é = {count}")
    print(f"O maior número é {maior}")
    print(f"O menor número é {menor}")
