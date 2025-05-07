import re
import random

def pares_de_lista(lista):

    pares = set()

    for x in lista:

        if x % 2 == 0:
            pares.add(x)

    return list(pares)

def palindromo(texto):


    if texto[:] == texto[::-1]:
        
        print(f"\"{texto}\" es palindromo")
    else:

        print(f"\"{texto}\" no es palindromo")

def factorial(numero):

    if numero == 0:
        return 1
    elif numero == 1:
        return 1
    else:
        return numero*factorial(numero-1)
    

def sin_repetidos(lista):


    return(list(set(lista)))


def fizz_buzz(principio,final):

    numero = principio

    while numero <= final:

        if numero % 3 == 0:

            if numero % 5 == 0:

                print("FizzBuzz")
            
            else:
                print("Fizz")
        elif numero % 5 == 0:
            print("Buzz")
        else:
            print(numero)
        
        numero += 1


def contar_vocales(texto):

    conteo = texto.count("a")
    conteo += texto.count("A")
    conteo += texto.count("e")
    conteo += texto.count("E")
    conteo += texto.count("i")
    conteo += texto.count("I")
    conteo += texto.count("o")
    conteo += texto.count("O")
    conteo += texto.count("u")
    conteo += texto.count("U")

    return conteo


def invertir_texto(texto):

    invertido = texto[::-1]

    return invertido

