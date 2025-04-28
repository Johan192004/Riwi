lista = [x for x in range(0,100,2)]

numero = int(input("Ingrese un numero: "))

if numero in lista:
    print(lista.index(numero))
else:
    print("No esta")