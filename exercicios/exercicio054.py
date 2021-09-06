from datetime import date

if __name__ == '__main__':

    anoAtual = date.today().year

    maioresDeIdade = 0
    menoresDeIdade = 0

    for i in range(0, 7):
        anoNascimento = int(input("Em que ano a {}ª pessoa nasceu? = ".format(i + 1)))

        if anoAtual - anoNascimento >= 18:
            maioresDeIdade += 1
        else:
            menoresDeIdade += 1

    print(f"Ao todo tivemos {maioresDeIdade} pessoas maiores de idade")
    print(f"Ao todo tivemos {menoresDeIdade} pessoas menores de idade")