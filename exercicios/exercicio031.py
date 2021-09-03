if __name__ == '__main__':

    distancia = float(input("Distância da viagem em Km = "))

    if distancia <= 200.0:
        preco = 0.50 * distancia
        print(f"O valor a ser pago = R$ {preco}")
    else:
        preco = 0.45 * distancia
        print(f"O valor a ser pago = R$ {preco}")