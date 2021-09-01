if __name__ == '__main__':

    preco = float(input("Digite o preço = "))

    desconto = preco - (preco * 0.05)

    print("O valor do produto com desconto = R$ {:.2f}".format(desconto))