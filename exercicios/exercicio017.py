from math import hypot, pow, sqrt

if __name__ == '__main__':

    catAdj = float(input("Valor do cateto adjacente = "))
    catOposto = float(input("Valor do cateto oposto = "))

    hipotenusa = hypot(catAdj,catOposto)

    print(f"A hipotenusa é {hipotenusa}")
    print(f"A hipotenusa é {sqrt((pow(catAdj,2) + pow(catOposto,2)))}")