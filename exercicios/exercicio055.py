if __name__ == '__main__':

    maiorPeso = 0.0
    menorPeso = 0.0

    for i in range(0,5):
        peso = float(input("Peso da {}ª pessoa: ".format(i + 1)))

        if i == 0:
            maiorPeso = peso
            menorPeso = peso
            continue

        if peso > maiorPeso:
            maiorPeso = peso

        if peso < menorPeso:
            menorPeso = peso

    print(f"O maior peso lido foi de {maiorPeso} kg")
    print(f"O menor peso lido foi de {menorPeso} kg")