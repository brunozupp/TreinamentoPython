if __name__ == '__main__':

    salario = float(input("Digite o salário = "))

    novoSalario = salario + (salario * 0.15)

    print("O novo salário é R$ {:.2f}".format(novoSalario))