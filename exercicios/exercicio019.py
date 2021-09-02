from random import randint

if __name__ == '__main__':

    alunos = []

    for i in range(4):
        nome = input(f"Digite o nome do aluno {i + 1} = ")
        alunos.append(nome)

    escolhido = randint(0,3)
    print(f"O aluno escolhido para apagar a lousa é = {alunos[escolhido]}")

