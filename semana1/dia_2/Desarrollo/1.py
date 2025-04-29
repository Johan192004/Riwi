lista = []

for i in range(3):
    lista.append(int(input("Ingrese un numero: ")))

smallest = lista[0]
biggest = lista[0]

for element in lista:
    if element > biggest:
        biggest = element
    elif element < smallest:
        smallest = element
    

print(f"El mas pequeño es {smallest} y el mas grande es {biggest}")