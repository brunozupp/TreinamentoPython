from random import randint

if __name__ == '__main__':

    numeroComputacao = randint(0,5)

    numeroPessoa = int(input("Digite um número = "))

    print(f"O computador pensou em = {numeroComputacao}")
    print("Venceu" if numeroPessoa == numeroComputacao else "Perdeu")