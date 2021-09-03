from math import fabs

if __name__ == '__main__':

    ladoA = float(input("Digite o tamanho do lado A = "))
    ladoB = float(input("Digite o tamanho do lado B = "))
    ladoC = float(input("Digite o tamanho do lado C = "))

    # Só irá existir um triângulo se, somente se, os seus lados obedeceram à seguinte regra: um de seus lados deve ser
    # maior que o valor absoluto(módulo) da diferença dos outros dois lados e menor que a soma
    # dos outros dois lados.Veja o resumo da regra abaixo:
    #
    # | b - c | < a < b + c
    # | a - c | < b < a + c
    # | a - b | < c < a + b

    resultado = True

    if not (fabs(ladoB - ladoC) < ladoA < (ladoB + ladoC)):
        resultado = False
    elif not (fabs(ladoA - ladoC) < ladoB < (ladoA + ladoC)):
        resultado = False
    elif not (fabs(ladoA - ladoB) < ladoC < (ladoA + ladoB)):
        resultado = False

    print("É um triangulo" if resultado else "Não é um triangulo")