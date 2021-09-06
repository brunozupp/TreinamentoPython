from math import ceil

if __name__ == '__main__':

    palavra = input("Digite uma palavra = ")

    resultado = True

    tamanhoPalavra = len(palavra)
    indexMetadeDaPalavra = ceil(tamanhoPalavra / 2)

    for i in range(0, indexMetadeDaPalavra):
        indexInverso = (tamanhoPalavra - 1) - i

        if palavra[i] != palavra[indexInverso]:
            resultado = False
            break

    print("É palindromo" if resultado else "Não é palindromo")