if __name__ == '__main__':
    n1 = int(input('Número 1: '))
    n2 = int(input('Número 2: '))

    s = n1 + n2;
    m = n1 * n2;
    d = n1 / n2;
    di = n1 // n2;
    e = n1 ** n2

    #print('A soma é {}, o produto é {}, e a divisão é {:.3f}'.format(s,m,d))
    print('A soma é {}, \no produto é {}, e a divisão é {:.3f}'.format(s,m,d), end=" ") # para ficar na mesma linha usa o end
    print('Divisão inteira {} e potência {}'.format(di,e))