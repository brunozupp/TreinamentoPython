if __name__ == '__main__':

    totalGasto = 0.0
    quantidadeProdutosCustoMaisDe1000 = 0

    nomeProdutoMaisBarato = ""
    precoProdutoMaisBarato = 0.0

    count = 0

    while True:

        count += 1

        nomeProduto = input(f"Digite o nome do produto {count} = ")
        precoProduto = float(input(f"Digite o preco do produto {count} = "))

        # A)
        totalGasto += precoProduto

        # B)
        if precoProduto > 1000.0:
            quantidadeProdutosCustoMaisDe1000 += 1

        if count == 1 or precoProduto < precoProdutoMaisBarato:
            nomeProdutoMaisBarato = nomeProduto
            precoProdutoMaisBarato = precoProduto

        continuar = ""

        while continuar != "s" and continuar != "n":
            continuar = str(input("Digite S para continuar ou N para sair = ")).lower()

        if continuar == "s":
            continue
        elif continuar == "n":
            break

    print(f"A) Total gasto = R$ {totalGasto}")
    print(f"B) Quantidade de produtos que custam mais de R$ 1000 = {quantidadeProdutosCustoMaisDe1000}")
    print(f"C) Nome do produto mais barato {nomeProdutoMaisBarato} custando R$ {precoProdutoMaisBarato}")