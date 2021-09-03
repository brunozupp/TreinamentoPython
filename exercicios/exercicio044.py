if __name__ == '__main__':

    precoProduto = 1000.0

    print("Opções de pagamento")
    print("1 - A vista dinheiro/cheque")
    print("2 - A vista no cartão")
    print("3 - Em até 2x no cartão")
    print("4 - 3x ou mais no cartão")

    escolha = int(input("Digite uma opção = "))

    if escolha == 1:
        pagamento = precoProduto - (precoProduto * 0.1)
    elif escolha == 2:
        pagamento = precoProduto - (precoProduto * 0.05)
    elif escolha == 3:
        pagamento = precoProduto
    else:
        pagamento = precoProduto + (precoProduto * 0.2)

    print("Vai pagar {:.2f}".format(pagamento))