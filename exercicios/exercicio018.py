from math import sin, cos, tan, radians

if __name__ == '__main__':

    angulo = radians(float(input("Digite o angulo = ")))

    seno = sin(angulo)
    cosseno = cos(angulo)
    tangente = tan(angulo)

    print(f"Seno: {seno}\nCosseno: {cosseno}\nTangente: {tangente}")