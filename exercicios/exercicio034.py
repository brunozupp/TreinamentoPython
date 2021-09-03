if __name__ == '__main__':

    salario = float(input("Salário = "))

    salarioAumentado = (salario + (salario * 0.1)) if salario > 1250.0 else (salario + (salario * 0.15))

    print(f"Salário é de R$ {salarioAumentado}")