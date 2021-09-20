if __name__ == '__main__':

    '''
        Cédulas que podem ter: 
        R$ 50
        R$ 20
        R$ 10
        R$ 1
    '''

    valorSacado = int(input("Qual o valor a ser sacado? = "))

    # Variável auxiliar
    valorParaSerSubtraido = valorSacado

    notasDe50 = 0
    notasDe20 = 0
    notasDe10 = 0
    notasDe1 = 0

    if valorParaSerSubtraido >= 50:
        while valorParaSerSubtraido >= 50:
            notasDe50 += 1
            valorParaSerSubtraido -= 50

    if valorParaSerSubtraido >= 20 and valorParaSerSubtraido < 50:
        while valorParaSerSubtraido >= 20:
            notasDe20 += 1
            valorParaSerSubtraido -= 20

    if valorParaSerSubtraido >= 10 and valorParaSerSubtraido < 20:
        while valorParaSerSubtraido >= 10:
            notasDe10 += 1
            valorParaSerSubtraido -= 10

    if valorParaSerSubtraido >= 1 and valorParaSerSubtraido < 10:
        while valorParaSerSubtraido >= 1:
            notasDe1 += 1
            valorParaSerSubtraido -= 1

    print(f"Notas de R$50 = {notasDe50}")
    print(f"Notas de R$20 = {notasDe20}")
    print(f"Notas de R$10 = {notasDe10}")
    print(f"Notas de R$1 = {notasDe1}")
