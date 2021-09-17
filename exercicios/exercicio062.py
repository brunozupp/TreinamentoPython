if __name__ == '__main__':

    primeiroTermo = int(input("Digite o primeiro termo = "))
    razao = int(input("Digite a razão = "))

    count = 0

    while count < 10:
        termo = primeiroTermo + (razao * (count))
        print(termo)
        count += 1

    quantidadeDeTermos = 1

    while quantidadeDeTermos > 0:
        quantidadeDeTermos = int(input("Quantos termos vc quer mostrar mais? = "))

        novoCount = count + quantidadeDeTermos

        while count < novoCount:
            termo = primeiroTermo + (razao * count)
            print(termo)
            count += 1