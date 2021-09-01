if __name__ == '__main__':
    valorTrue = True
    valorFalse = False
    valorInt = 4
    valorFloat = 5.7
    valorStr = "Olaaaaa"

    # Usar esse primeiro print que é melhor
    print(f"{type(valorTrue)} - {type(valorInt)} - {type(valorFloat)} - {type(valorStr)}")
    print('A soma de {} + {} = {}'.format(valorInt, valorFloat, (valorInt + valorFloat)))

    valorStrNumerico = '8'

    print(valorStr.isnumeric())
    print(valorStrNumerico.isnumeric())
