if __name__ == '__main__':

    num1 = int(input("Digite o número 1 = "))
    num2 = int(input("Digite o número 2 = "))
    num3 = int(input("Digite o número 3 = "))

    if num1 >= num2 and num1 >= num3:
        print(f"{num1} maior")
    elif num2 >= num1 and num2 >= num3:
        print(f"{num2} maior")
    else:
        print(f"{num3} maior")

    if num1 <= num2 and num1 <= num3:
        print(f"{num1} menor")
    elif num2 <= num1 and num2 <= num3:
        print(f"{num2} menor")
    else:
        print(f"{num3} menor")