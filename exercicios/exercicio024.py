if __name__ == '__main__':

    cidade = input("Digite o nome da cidade = ")

    findIndex = cidade.upper().find("SANTO")

    if findIndex == 0:
        print("Começa com a palavra SANTO")
    else:
        print("Não começa com a palavra SANTO")