import random

numero_aleatorio = random.randint(1,10)

intento = int(input("Ingrese un numero entre 1 y 10: "))

while True:

    if intento == numero_aleatorio:
        print("Adivinaste")
        break
    elif intento < numero_aleatorio:
        print("El numero secreto es mayor al numero ingresado")
    else:
        print("El numero secreto es menor al numero ingresado")

    intento = int(input("Ingresa otro numero: "))