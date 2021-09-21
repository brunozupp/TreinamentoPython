if __name__ == '__main__':
    # LISTA SÃO MUTÁVEIS
    num = [3, 2, 1, 4, 5]
    print(num)

    print("-" * 30)

    num[2] = 6
    print(num)

    print("-" * 30)

    num.append(7)
    print(num)

    print("-" * 30)

    num.sort()
    print(num)

    print("-" * 30)

    num.sort(reverse=True)
    print(num)

    print("-" * 30)

    num.insert(0,74) # Na posição 0, insira o valor 74
    print(num)

    print("-" * 30)

    num.pop() # sem nenhum parametro ele vai eliminar o último elemento
    print(num)

    print("-" * 30)

    num.pop(1)
    print(num)

    print("-" * 30)

    if 74 in num:
        num.remove(74)

    print(num)

    print("-" * 30)

    if 109 in num:
        num.remove(709)
    else:
        print("NÃO ACHEI O NÚMERO 109")

    print(num)

    print("-" * 30)

    num.append(2)
    num.append(2)
    print(num)

    print("-" * 30)

    num.remove(2) # vai remover apenas o primeiro 2 que ele encontrar
    print(num)

    print("-" * 30)

    valores = []
    valores.append(5)
    valores.append(9)
    valores.append(4)

    for index,value in enumerate(valores):
        print(f"Na posição {index} encontrei o valor {value}")
    print("Cheguei no final")

    print("-" * 30)

    a = [2,3,4,7]
    b = a # ambas as variáveis estão apontando para o mesmo espaço de memória
    b[2] = 8 # então mudando aqui, a mudança vai refletir nas duas variáveis
    print(f"Lista A: {a}")
    print(f"Lista B: {b}")

    print("-" * 30)

    c = [2,3,4,7]
    d = c[:] # com essa sintaxe vai criar uma cópia do array, vai ser duas caixas na memória diferentes que c e d vão apontar
    d[2] = 8  # então mudando aqui, a mudança só vai refletir na lista apontada pela variável d
    print(f"Lista C: {c}")
    print(f"Lista D: {d}")
