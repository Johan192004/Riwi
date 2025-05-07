def saludo_personalizado(nombre):
    print(f"Hola, {nombre}")

def sumar_numeros(x,y):
    return x + y

def definir_par_impar(numero):

    if numero % 2 == 0:
        print("Par!")
    else:
        print("Impar")

def mayoria_edad(edad):

    if edad >= 0 and edad <= 17:
        print("Eres menor de edad")
    elif edad > 17:
        print("Eres mayor de edad")
    else:
        print("Edad no valida")


def celsius_a_fahrenheit(celsius):

    fahrenheit = (celsius * 9/5) + 32
    print(f"Celsius: {celsius}\n Fahrenheit: {fahrenheit}")


def area_triangulo(h,b):

    area = (h*b)/2

    print(f"El area del triangulo es: {area}")


def mayor_de_lista(lista):

    print(max(lista))


def contar_letras(palabra,letra):

    print(palabra.count(letra))


