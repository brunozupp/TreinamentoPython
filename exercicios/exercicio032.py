if __name__ == '__main__':

    while True:
        ano = int(input("Digite um ano = "))

        if ano % 4 == 0:
            if ano % 100 != 0:
                print(f"{ano} é um ano bissexto (1)")
            else:
                if ano % 400 == 0:
                    print(f"{ano} é um ano bissexto (2)")
                else:
                    print("Não é bissexto")
        else:
            print("Não é bissexto")