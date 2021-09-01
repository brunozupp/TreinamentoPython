if __name__ == '__main__':

    nome = input("Qual é seu nome: ")
    print('Prazer em te conhecer {:20}!'.format(nome))
    print('Prazer em te conhecer {:>20}!'.format(nome)) # alinhado a direita
    print('Prazer em te conhecer {:<20}!'.format(nome)) # alinhado a esquerda
    print('Prazer em te conhecer {:^20}!'.format(nome)) # centralizado em 20 espaços
    print('Prazer em te conhecer {:=^20}!'.format(nome)) # centralizado preenchendo os espaços em branco com =