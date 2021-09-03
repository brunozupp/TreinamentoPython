if __name__ == '__main__':

    velocidade = float(input("Velocidade do carro = "))

    if velocidade > 80.0:

        diferencaVelocidade = velocidade - 80.0

        multa = diferencaVelocidade * 7.00

        print(f"Você foi multado em: R$ {multa}")
    else:
        print("Não foi multado")