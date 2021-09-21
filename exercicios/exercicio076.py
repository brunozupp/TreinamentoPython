if __name__ == '__main__':

    produtos = "Banana", 10.5, "Maça", 20.7, "Uva", 300, "Pera", 40.08

    print("-" * 60)
    print(f"{'LISTAGEM DE PRODUTOS':^60}")
    print("-" * 60)

    for i in range(0, len(produtos), 2):
        print(f"{produtos[i]:.<50}R${produtos[i + 1]:>7.02f}")

    print("-" * 60)
