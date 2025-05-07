import re
import random

def contraseña_segura(contraseña):

    if len(contraseña) >= 8:

        tiene_mayuscula = any(letra.isupper() for letra in contraseña)

        if tiene_mayuscula:

            tiene_minuscula = any(char.islower() for char in contraseña)

            if tiene_minuscula:

                tiene_numero = any(letra.isdigit() for letra in contraseña)

                if tiene_numero:

                    tiene_caracter = bool(re.search(r"[^a-zA-Z0-9\s]",contraseña))

                    if tiene_caracter:

                        print("Tu contraseña es segura")
                    
                    else:
                        print("La contraseña debe contener caracteres especiales")


                else:
                    print("La contraseña debe contener numeros")

            else:

                print("La contraseña debe contener minusculas")

        else:
            print("La contraseña debe contener mayusculas")

    else:

        print("La contraseña debe de tener mas de 8 caracteres")

def dado():

    print(random.randint(1,6))

def suma_unicos(lista):

    seteado = set(lista)

    suma = sum(seteado)

    return suma


def generador_de_contraseñas(longitud):

    contraseña = ""

    for x in range(longitud):

        numero_aletorio = 0
        while 1:
            
            numero_aletorio = random.randint(32,126)

            if numero_aletorio == 32:
                continue
            else:
                break

        contraseña += chr(numero_aletorio) 
    
    print(contraseña)


def doble(x):
    return x * 2

def cuadrado(x):
    return x ** 2