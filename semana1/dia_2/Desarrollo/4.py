edad = int(input("Ingresa tu edad: "))

edades = list(range(0,121,1))

if edad in edades:
    print("Edad valida")
else:
    print("Edad no valida")