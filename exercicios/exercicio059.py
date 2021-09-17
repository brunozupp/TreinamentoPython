if __name__ == '__main__':

    num1 = float(input("Digite o número 1 = "))
    num2 = float(input("Digite o número 2 = "))

    opcao = 0

    while True:

        print("1 - Somar\n2 - Multiplicar\n3 - Maior\n4 - Novos números\n5 - Sair do programa")
        opcao = int(input("Digite a opção = "))

        if opcao == 1:
            print(f"A conta {num1} + {num2} = {num1 + num2}")

        elif opcao == 2:
            print(f"A conta {num1} * {num2} = {num1 * num2}")

        elif opcao == 3:
            print(f"O número maior é {num1 if num1 > num2 else num2}")

        elif opcao == 4:
            num1 = float(input("Digite o número 1 = "))
            num2 = float(input("Digite o número 2 = "))

        elif opcao == 5:
            print("Saindo")
            exit(0)

        else:
            print("Opção errada. Digite novamente\n")