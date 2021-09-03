from datetime import date

if __name__ == '__main__':

    anoAtual = date.today().year

    anoNascimento = int(input("Ano de nascimento = "))

    idade = anoAtual - anoNascimento

    if idade > 18:
        print("Passou do tempo de se alistar")
    elif idade == 18:
        print("Hora de se alistar")
    else:
        print(f"Ainda não é hora de se alistar, falta {18 - idade} anos para se alistar")