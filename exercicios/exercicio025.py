if __name__ == '__main__':

    nome = input("Digite um nome = ")

    findIndex = nome.upper().find("SILVA")

    if findIndex >= 0:
        print("Tem Silva no Nome")
    else:
        print("Não tem Silva no nome")