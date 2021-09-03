if __name__ == '__main__':

    valorCasa = float(input("Qual o valor da casa = "))
    salarioComprador = float(input("Salário do comprador = "))
    quantosAnos = int(input("Quantos anos deseja pagar = "))

    prestacaoPorMes = valorCasa / (12 * quantosAnos)

    if prestacaoPorMes > (salarioComprador * 0.3):
        print("Prestação por mês maior que 30% do salário do cliente. NEGADO")
    else:
        print("APROVADO")