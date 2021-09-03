if __name__ == '__main__':

    numero = int(input("Escolha um número inteiro = "))

    print("")

    print("1 - Converter para binário\n2 - Converter para octal\n3 - Converter para hexadecimal\n")
    escolha = int(input("Digite o número da opção para converter = "))

    if escolha == 1:
        print("{}".format(str(bin(numero))[2:])) #0b
    elif escolha == 2:
        print("{}".format(str(oct(numero))[2:])) #0o
    else:
        print("{}".format(str(hex(numero))[2:])) #0x
