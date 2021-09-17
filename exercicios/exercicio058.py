from random import randint

if __name__ == '__main__':

    computador = randint(0,10)
    palpites = 0

    numeroPessoa = -1

    while numeroPessoa != computador:

        palpites += 1

        numeroPessoa = int(input("Digite um número de 0 á 10 = "))

    print(f"Acertou, o número do computador era {computador}")
    print(f"Foram necessários {palpites} para acertar")