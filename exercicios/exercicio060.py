if __name__ == '__main__':

    num = int(input("Digite um número = "))

    if num == 0:
        print("Fatorial de 0 é 1")
        exit(0)

    fatorial = num;
    auxiliar = num;

    while auxiliar > 1:
        auxiliar -= 1;
        fatorial *= auxiliar

    print(f"O fatorial de {num} é = {fatorial}")
