if __name__ == '__main__':

    numero = int(input("Digite um número = "))

    listaDenominadoresDivisiveis = []
    listaDenominadoresDivisiveis.append(1)

    for i in range(2,numero):
        if numero % i == 0:
            listaDenominadoresDivisiveis.append(i)

    listaDenominadoresDivisiveis.append(numero)

    if len(listaDenominadoresDivisiveis) > 2:
        print(f"O número {numero} não é PRIMO")
        print(listaDenominadoresDivisiveis)
    else:
        print(f"O número {numero} é PRIMO")
