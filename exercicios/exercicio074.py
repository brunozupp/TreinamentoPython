from random import randint

if __name__ == '__main__':

    tupla = ()

    for i in range(0,5):
        valor = randint(0,10)

        # (valor,) com a virgula no final ali é uma tupla, se tirar não é uma tupla
        tupla = tupla + (valor,)

    menor = tupla[0]
    maior = tupla[1]

    for i in range(1,len(tupla)):
        if menor > tupla[i]:
            menor = tupla[i]

        if maior < tupla[i]:
            maior = tupla[i]

    print(tupla)
    print(f"Menor = {menor}")
    print(f"Maior = {maior}")