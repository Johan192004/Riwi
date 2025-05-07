from funciones_basico import contar_letras,mayor_de_lista,area_triangulo, celsius_a_fahrenheit,mayoria_edad, saludo_personalizado, sumar_numeros, definir_par_impar

from funciones_intermedio import invertir_texto, pares_de_lista, palindromo, factorial, sin_repetidos, fizz_buzz, contar_vocales
from funciones_avanzadas import suma_unicos,dado,contraseña_segura,generador_de_contraseñas, doble, cuadrado

# #Punto 1
# saludo_personalizado("Johan")

# #Punto 2

# primer_numero = int(input("Ingrese el primer numero: "))
# segundo_numero = int(input("Ingrese el segundo numero: "))
# suma = sumar_numeros(primer_numero,segundo_numero)

# print(suma)

# #Punto 3

# numero = int(input("Ingrese un numero: "))
# definir_par_impar(numero)


# #Punto 4

# edad = int(input("Ingrese una edad: "))
# mayoria_edad(edad)

# #Punto 5

# celsius = float(input("Ingrese la temperatura en grados celsius: "))
# celsius_a_fahrenheit(celsius)


# #Punto 6

# altura = float("Ingrese la altura del triangulo: ")
# base = float("Ingrese la base del triangulo: ")

# area_triangulo(altura,base)


# #Punto 7

# numeros = [1,2,3,65,21,32,555,1,2,9,0]
# mayor_de_lista(numeros)

# #Punto 8

# palabra = input("Ingrese una palabra: ")
# letra = input("Ingrese la palabra que desea contar: ")
# contar_letras(palabra,letra)

#Punto 9

# numeros = [1,2,3,4,5,6,7,8,0,22,21,43,2]
# print(pares_de_lista(numeros))

#Punto 10

# palindromo("Hola")
# palindromo("dabale arroz a la zorra el abad")
# palindromo("arenera")

#Punto 11

# numero = int(input("Ingrese un numero al que le gustaria obtener el factorial: "))
# print(f"El factorial de {numero} es {factorial(numero)}")

#Punto 12

# lista = [1,2,3,4,45,6,7,8,2,2,2,3,3,3,4,4,2,1,4,4,5,6,7,8]
# print(sin_repetidos(lista))

#Punto 13

# principio = int(input("Ingrese desde donde se hara el fizz buzz: "))
# final = int(input("Ingrese hasta donde se hara el fizz buzz: "))
# fizz_buzz(principio,final)


#Punto 14

# palabra = input("Ingrese la palabra a la cual le gustaria contar las vocales: ")
# print(f"Hay {contar_vocales(palabra)} en la palabra {palabra}")


#Punto 15

# palabra = input("Ingrese la palabra a la cual le gustaria voltear: ")
# print(invertir_texto(palabra))


#Punto 16

# contraseña = input("Ingresa una contraseña: ")
# contraseña_segura(contraseña)


#Punto 17

# dado()

#Punto 18

# numeros = [1,5,3,1,2,3,4,5,6,7,8,4,2,3,2,3,2]
# print(suma_unicos(numeros))

#Punto 19

# longitud = int(input("Ingrese la longitud de la contraseña: "))
# generador_de_contraseñas(longitud)

#Punto 20

print(doble(cuadrado(3)))

