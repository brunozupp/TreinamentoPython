if __name__ == '__main__':

    tupla = ['zero','um','dois','três','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze',
             'quatorze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte']

    numero = -1;

    while numero < 0 or numero > 20:
        numero = int(input("Digite um número entre 0 e 20 = "))

    print(f"Você digitou o número {numero} que por extenso é {tupla[numero]}")