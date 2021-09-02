if __name__ == '__main__':

    frase = "Curso em Vídeo Python"

    fat1 = frase[9:13]
    fat2 = frase[9:14]

    print(fat1)
    print(fat2)

    # vai da posição 9 a 21 pulando de 2 em 2
    fat3 = frase[9:21:2]
    print(fat3)

    fat4 = frase[:5] # igual escrever [0:5]
    print(fat4)

    fat5 = frase[15:] # da posição 15 até o final
    print(fat5)

    fat6 = frase[9::3] # vai começar do 9 e vai até o final pulando de 3 em 3
    print(fat6)

    contar = frase.count('o') # quantas letras 'o' aparecem
    print(contar)

    contarFat = frase.count('o',0,13) # contagem com fatiamento. Pega do 0 até o 13 (12 na realidade) e procura por letras 'o'
    print(contarFat)

    length = len(frase)
    print(length)

    find = frase.find('deo') # em que posição/index começou essa string que colocou para analisar no argumento
    print(find)

    existe = 'Curso' in frase
    print(existe)

    # A diferença é que capitalize só a primeira letra da string vai pra upper, já o title toda palavra entre espaços fica com a primeira letra upper
    funcCapitalize = frase.capitalize()
    funcTitle = frase.title()

    print(funcCapitalize)
    print(funcTitle)

    outrafrase = "   Aprendendo Python  "

    print(outrafrase.strip()) # Remove os espaços do começo e fim
    print(outrafrase.rstrip()) # Remove os espaços da direita (os finais)
    print(outrafrase.lstrip()) # Remove os espaços da esquerda (os iniciais)

    palavras = frase.split()
    print(palavras)

    juntarPalavras = '-'.join(frase)
    print(juntarPalavras)

