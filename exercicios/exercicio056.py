if __name__ == '__main__':

    nomeHomemMaisVelho = ""
    idadeHomemMaisVelho = 0
    quantidadeMulheresMenoresQue20Anos = 0
    somaIdade = 0

    for i in range(0,4):
        print(f"----- {i + 1}ª PESSOA -----")
        nome = input("Nome: ")
        idade = int(input("Digite sua idade: "))
        sexo = input("Sexo: [M/F]: ")

        if sexo == "F" and idade < 20:
            quantidadeMulheresMenoresQue20Anos += 1

        if sexo == "M" and idadeHomemMaisVelho < idade:
            idadeHomemMaisVelho = idade
            nomeHomemMaisVelho = nome

        somaIdade += idade

    mediaIdade = somaIdade / 4

    print(f"A média de idade do grupo é de {mediaIdade} anos")
    print(f"O homem mais velho tem {idadeHomemMaisVelho} e se chama {nomeHomemMaisVelho}")
    print(f"Ao todo são {quantidadeMulheresMenoresQue20Anos} mulheres com menos de 20 anos")

