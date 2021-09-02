if __name__ == '__main__':

    nomeCompleto = input("Digite seu nome completo = ")

    nomeCompleto = nomeCompleto.strip()

    print(nomeCompleto.upper())

    print(nomeCompleto.lower())

    nomes = nomeCompleto.split()

    print(len("".join(nomes)))

    print(len(nomes[0]))