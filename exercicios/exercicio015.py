if __name__ == '__main__':

    kmPercorrido = float(input("KM percorrido: "))
    diasAlugado = int(input("Dias alugado: "))

    aluguel = (60 * diasAlugado) + (0.15 * kmPercorrido)

    print("O total a pagar é de R$ {:.2f}".format(aluguel))