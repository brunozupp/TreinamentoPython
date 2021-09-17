from random import randint

if __name__ == '__main__':

    vitorias = 0

    while True:

        computador = randint(0,10)
        #print(f"Computador = {computador}")
        usuario = int(input("Digite um valor = "))

        soma = computador + usuario

        resposta = input("Par ou Ímpar? [P/I] = ")
        ehPar = soma % 2 == 0

        print(f"Você jogou {usuario} e o computador jogou {computador}. Total de {soma} {'DEU PAR' if ehPar else 'DEU ÍMPAR'}")

        if ehPar and resposta == "P":
            print("Você VENCEU")
            vitorias += 1
        elif not ehPar and resposta == "I":
            print("Você VENCEU")
            vitorias += 1
        else:
            print(f"VOCÊ PERDEU")
            break

        print()

    print()
    print(f"GAME OVER! Você venceu {vitorias} vezes.")