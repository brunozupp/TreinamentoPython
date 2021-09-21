if __name__ == '__main__':

    palavras = "maca", "uva", "pera", "banana", "manga", "abacaxi", "praticar", "estudar", "programador", "futuro"

    for palavra in palavras:

        vogais = ""
        caracteres = list(palavra)
        contador = 0

        while contador < len(caracteres):

            if caracteres[contador] == 'a':
                vogais += 'a '

            if caracteres[contador] == 'e':
                vogais += 'e '

            if caracteres[contador] == 'i':
                vogais += 'i '

            if caracteres[contador] == 'o':
                vogais += 'o '

            if caracteres[contador] == 'u':
                vogais += 'u '

            contador += 1

        print(f"Na palavra '{palavra}' temos as vogais = {vogais}")

        '''print(f"Na palavra '{palavra}' temos as vogais = "
              f"{'a ' * palavra.count('a')}"
              f"{'e ' * palavra.count('e')}"
              f"{'i ' * palavra.count('i')}"
              f"{'o ' * palavra.count('o')}"
              f"{'u ' * palavra.count('u')}")'''