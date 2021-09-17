if __name__ == '__main__':

    sum = 0
    count = 0

    numero = int(input("Digite um número ou 999 para sair = "))

    while numero != 999:
        sum += numero
        count += 1

        numero = int(input("Digite um número ou 999 para sair = "))

    print(f"A soma é {sum}")
    print(f"A quantidade de números digitados é = {count}")