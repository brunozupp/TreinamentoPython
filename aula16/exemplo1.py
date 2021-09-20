if __name__ == '__main__':

    # formas de inicializar as tuplas
    lanche = ('hamburguer', 'suco', 'pizza', 'pudim')
    cores = 'azul', 'amarelo', 'verde', 'vermelho', 'cinza'

    print(lanche)
    print(cores)

    print("-" * 30)

    print(cores[2])

    print("-" * 30)

    print(cores[1:4])
    print(cores[1:])
    print(cores[:3]) # do indice 0 até o indice 2
    print(cores[-1]) # vai pegar o último elemento
    print(cores[-3:])

    print("-" * 30)

    # indice cor 0 é azul
    # Tuplas são IMUTAVEIS
    # print(cores[0])
    # cores[0] = 'roxo' # vai dar um erro
    # print(cores[0])

    for cor in cores:
        print(cor)

    print("-" * 30)

    for i in range(0,len(cores)):
        print(cores[i])

    print("-" * 30)

    for pos, cor in enumerate(cores):
        print(f"Eu vou usar a cor {cor} na posição {pos}")

    print("-" * 30)

    print(sorted(cores)) # o sorted não altera a minha tupla
    print(cores)

    print("-" * 30)

    a = [2,5,4]
    b = [5,6,8,1,2]
    c = a + b # cancatena. A ordem tem influência
    print(c)

    print("-" * 30)

    print(f"Quantas vezes está aparecendo o número 5 na Tupla c => {c.count(5)} vezes")

    print("-" * 30)

    print(f"O número 4 está na posição {c.index(4)} da tupla")

    print("-" * 30)

    # No python, as tuplas não são apenas de um tipo, posso ter mais de um tipo de dado
    pessoa = ("Bruno", 22, "M", 99.80)
    print(pessoa)

    # não posso remover um item da tupla pois ela é imutavel, mas posso deletar ela inteira
    #del(pessoa)
    #print(pessoa) # da erro pois removi da memória
