import numpy as np

IMAGEM1 = [1, 1, 1, 1, 1, -1, -1, -1, -1, -1, 1, 1, -1, 1, 1, 1, 1, -1, -1, -1, -1, -1, 1, 1, 1, 1, 1, 1, 1, -1]
IMAGEM2 = [1, 1, -1, -1, 1, 1, 1, 1, -1, -1, 1, 1, 1, 1, 1, 1, 1, 1, -1, -1, -1, -1, 1, 1, -1, -1, -1, -1, 1, 1]
IMAGEM3 = [-1, -1, 1, 1, -1, -1, -1, 1, 1, 1, -1, -1, -1, -1, 1, 1, -1, -1, -1, -1, 1, 1, -1, -1, -1, 1, 1, 1, 1, -1]
IMAGEM4 = [-1, 1, 1, 1, 1, -1, 1, 1, -1, -1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, -1, -1, 1, 1, -1, 1, 1, 1, 1, -1]
IMAGEM5 = [1, 1, 1, 1, 1, 1, -1, -1, 1, 1, -1, -1, -1, -1, 1, 1, -1, -1, -1, -1, 1, 1, -1, -1, -1, -1, 1, 1, -1, -1]
IMAGEM6 = [1, 1, -1, -1, -1, -1, 1, 1, -1, -1, -1, -1, 1, 1, -1, -1, -1, -1, 1, 1, -1, -1, -1, -1, 1, 1, 1, 1, 1, 1]
IMAGEM7 = [-1, -1, 1, 1, -1, -1, -1, -1, 1, 1, -1, -1, -1, 1, 1, 1, 1, -1, 1, 1, -1, -1, 1, 1, 1, 1, 1, 1, 1, 1]
PADRAO_DESCONHECIDO = [1, 1, 1, 1, 1, -1, -1, -1, -1, -1, -1, -1, -1, 1, 1, 1, -1, -1, -1, -1, -1, -1, -1, -1, 1, 1, -1, 1, 1, -1]
padroesExercicio = [IMAGEM1, IMAGEM2, IMAGEM3, IMAGEM4, IMAGEM5, IMAGEM6, IMAGEM7]

MAX_ITERATIONS = 10

def inicializarMatriz():
    matriz = []

    for i in range(0,len(PADRAO_DESCONHECIDO)):

        linha = []

        for j in range(0,len(PADRAO_DESCONHECIDO)):
            linha.append(0)

        matriz.append(linha)

    return matriz


def gerarMatrizPesos():
    padroes = [IMAGEM1, IMAGEM2, IMAGEM3, IMAGEM4, IMAGEM5, IMAGEM7]
    matrizPeso = inicializarMatriz()

    for i in range(0, len(matrizPeso[0])):
        for j in range(0, len(matrizPeso[i])):

            if j >= i:
                break

            soma = 0

            for k in range(0, len(padroes)):
                soma += (padroes[k][i] * padroes[k][j])

            matrizPeso[j][i] = matrizPeso[i][j] = soma

    return matrizPeso


def treinar(pesos, padraoDesconhecido, counter):
    if counter == MAX_ITERATIONS:
        print("FALHOU")
        return

    counter += 1

    padraoY = [0 for i in range(len(padraoDesconhecido))]

    for i in range(0, len(pesos)):
        soma = 0

        for j in range(0, len(pesos[i])):
            soma += (padraoDesconhecido[j] * pesos[j][i])

        padraoY[i] = 1 if soma >= 0 else -1

    convergiu = False

    for i in range(0, len(padroesExercicio)):
        convergiu = np.array_equal(padraoY, padroesExercicio[i])

        if convergiu:
            break

    if not convergiu:
        treinar(pesos, padraoY, counter)
    else:
        print(f"\nCONVERGIU na {counter}ª vez")


if __name__ == '__main__':
    pesos = gerarMatrizPesos()
    counter = 0
    treinar(pesos, PADRAO_DESCONHECIDO, counter)
