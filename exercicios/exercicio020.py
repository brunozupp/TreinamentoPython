from random import randint

if __name__ == '__main__':

    alunos = []

    for i in range(4):
        nome = input(f"Digite o nome do aluno {i + 1} = ")
        alunos.append(nome)

    ordemApresentacao = []

    while ordemApresentacao.__len__() < 4:

        numero = randint(0,3)

        while(ordemApresentacao.__contains__(numero)):
            numero = randint(0,3)

        ordemApresentacao.append(numero)

    print("Ordem de apresentação:")
    for i in range(4):
        print(f"Aluno {i + 1} - {alunos[ordemApresentacao[i]]}")


