from datetime import date

if __name__ == '__main__':

    anoAtual = date.today().year

    anoNascimento = int(input("Nascimento = "))

    idade = anoAtual - anoNascimento

    if idade <= 9:
        print("MIRIM")
    elif idade <= 14:
        print("INFANTIL")
    elif idade <= 19:
        print("JUNIOR")
    elif idade <= 20:
        print("SÊNIOR")
    else:
        print("MASTER")