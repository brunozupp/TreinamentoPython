if __name__ == '__main__':

    soma = 0

    for i in range(0,6):
        num = int(input("Digite o número = "))

        if num % 2 == 0:
            soma += num

    print(soma)