if __name__ == '__main__':

    while True:
        tabuada = int(input("Digite um número = "))

        if tabuada < 0:
            break

        count = 1
        while count <= 10:
            print(f"{tabuada} x {count} = {tabuada * count}")
            count += 1