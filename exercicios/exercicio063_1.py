if __name__ == '__main__':

    lista = [0,1]

    sequencia = int(input("Digite um número = "))

    count = 0

    while count < sequencia:
        tamanho = len(lista)
        lista.append(lista[tamanho - 1] + lista[tamanho - 2])
        count += 1

    print(lista)
