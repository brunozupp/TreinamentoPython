if __name__ == '__main__':

    algumaCoisa = input("Digite qualquer coisa: ")

    isNumeric = algumaCoisa.isnumeric()
    isAlpha = algumaCoisa.isalpha()
    isLower = algumaCoisa.islower()
    isUpper = algumaCoisa.isupper()
    length = algumaCoisa.__len__()
    isBlankSpace = algumaCoisa.isspace()
    isAlphaNumeric = algumaCoisa.isalnum()
    isCapitalize = algumaCoisa.istitle() # Primeira letra maiuscula


    print(f"É Númerico = {isNumeric}")
    print(f"É Alfabetico = {isAlpha}")
    print(f"É LowerCase = {isLower}")
    print(f"É UpperCase = {isUpper}")
    print(f"Tamanho = {length}")
    print(f"Só tem espaço = {isBlankSpace}")
    print(f"É alfa númerico = {isAlphaNumeric}")
    print(f"É primeira letra maiuscula = {isCapitalize}")