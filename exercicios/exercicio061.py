if __name__ == '__main__':

    primeiroTermo = int(input("Digite o primeiro termo = "))
    razao = int(input("Digite a razão = "))

    count = 0

    while count < 10:
        termo = primeiroTermo + (razao * (count))
        print(termo)
        count += 1
