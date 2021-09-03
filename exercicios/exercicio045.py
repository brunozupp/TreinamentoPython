from random import randint

if __name__ == '__main__':

    rodada = 1

    while True:

        print("Rodada {}\n".format(rodada))

        print("1 - Pedra\n2 - Papel\n3 - Tesoura")
        escolhaPessoa = int(input("Escolha a opção = "))

        escolhaComputador = randint(1, 3)

        print("VOCÊ ESCOLHEU {} E O COMPUTADOR {}".format(escolhaPessoa, escolhaComputador))

        if escolhaPessoa == escolhaComputador:
            continue
        elif escolhaPessoa == 1 and escolhaComputador == 2:
            ganhador = "COMPUTADOR"
        elif escolhaPessoa == 1 and escolhaComputador == 3:
            ganhador = "PESSOA"
        elif escolhaPessoa == 2 and escolhaComputador == 3:
            ganhador = "COMPUTADOR"
        elif escolhaPessoa == 2 and escolhaComputador == 1:
            ganhador = "PESSOA"
        elif escolhaPessoa == 3 and escolhaComputador == 1:
            ganhador = "COMPUTADOR"
        elif escolhaPessoa == 3 and escolhaComputador == 2:
            ganhador = "PESSOA"

        if len(ganhador) > 0:
            break;

        rodada = rodada + 1

    print("O ganhador foi {}".format(ganhador))