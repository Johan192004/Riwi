hora = int(input("Ingrese la hora: "))

if hora < 12 or hora > 18:
    print("No es hora de trabajar")
else:
    print("Es hora de trabajar")