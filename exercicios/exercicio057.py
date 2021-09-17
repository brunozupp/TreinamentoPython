if __name__ == '__main__':

    sexo = ""

    while sexo != "M" and sexo != "F":
        sexo = str(input("Digite [M/F] para identificar o sexo = ")).upper()

    print(f"O valor digitado é {sexo}")