from math import ceil

if __name__ == '__main__':

    frase = input("Digite uma frase = ")

    palavras = frase.lower().split(" ")

    fraseJuntada = "".join(palavras)

    resultado = True

    tamanhoPalavra = len(fraseJuntada)
    indexMetadeDaPalavra = ceil(tamanhoPalavra / 2)

    for i in range(0, indexMetadeDaPalavra):
        indexInverso = (tamanhoPalavra - 1) - i

        if fraseJuntada[i] != fraseJuntada[indexInverso]:
            resultado = False
            break

    print("É palindromo" if resultado else "Não é palindromo")