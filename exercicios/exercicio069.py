if __name__ == '__main__':

    maisDe18Anos = 0
    quantidadeHomensCadastrados = 0
    quantidadeMulheresMenos20Anos = 0

    while True:

        idade = int(input("Idade: "))
        sexo = input("[M/F]: ")
        while sexo != "M" and sexo != "F":
            sexo = input("[M/F]: ")

        if idade >= 18:
            maisDe18Anos += 1;

        if sexo == "M":
            quantidadeHomensCadastrados += 1

        if sexo == "F" and idade < 20:
            quantidadeMulheresMenos20Anos += 1

        continuar = input("Quer continuar? [S/N]: ")

        while continuar != "S" and continuar != "N":
            continuar = input("Quer continuar? [S/N]: ")

        if continuar == "N":
            break

    print(f"Quantidade de pessoas maiores de 18 anos = {maisDe18Anos}")
    print(f"Quantiade de homens = {quantidadeHomensCadastrados}")
    print(f"Mulheres menores que 20 anos = {quantidadeMulheresMenos20Anos}")