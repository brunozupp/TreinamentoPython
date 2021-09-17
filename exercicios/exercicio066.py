if __name__ == '__main__':

    count = 0
    sum = 0

    while True:
        numero = int(input("Digite um número ou 999 para sair = "))

        if numero == 999:
            break;

        count += 1
        sum += numero

    print(f"A soma dos {count} números foi de {sum}")