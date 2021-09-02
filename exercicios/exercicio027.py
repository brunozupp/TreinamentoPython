if __name__ == '__main__':

    nome = input("Nome completo = ")

    nomes = nome.strip().split()

    primeiroNome = nomes[0]
    ultimoNome = nomes[len(nomes) - 1]

    print(f"Primeiro nome = {primeiroNome}")
    print(f"Último nome = {ultimoNome}")