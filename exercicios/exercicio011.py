if __name__ == '__main__':

    largura = float(input("Largura = "))
    altura = float(input("Altura = "))

    area = largura * altura;

    # assumindo que uma lata possui 1L

    latasInteiras = area // 2
    quantidadeRestante = (area % 2) * 1000

    print(f"Área total = {area}")
    print(f"Você vai precisar de {latasInteiras} latas inteiras e {quantidadeRestante} mililitro")