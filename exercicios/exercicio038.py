if __name__ == '__main__':

    num1 = int(input("Digite o número 1 = "))
    num2 = int(input("Digite o número 2 = "))

    if num1 > num2:
        print(f"{num1} > {num2}")
    elif num2 > num1:
        print(f"{num2} > {num1}")
    else:
        print("Iguais")