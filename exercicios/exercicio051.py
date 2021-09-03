if __name__ == '__main__':

    primeiroTermo = int(input("Digite o primeiro termo = "))
    razao = int(input("Digite a razão = "))

    for i in range(0, 10):
        print(primeiroTermo + (razao * (i)))
