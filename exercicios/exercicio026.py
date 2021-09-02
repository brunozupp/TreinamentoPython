if __name__ == '__main__':

    frase = input("Digite algo: ")

    countA = frase.upper().count("A")

    findIndexA = frase.upper().find('A')

    findLastIndexA = frase.upper().rfind('A')

    print(f"Frase: {frase}")
    print(f"Vezes que a letra A aparece {countA} vezes")
    print(f"Última posição da letra A = {findLastIndexA}")