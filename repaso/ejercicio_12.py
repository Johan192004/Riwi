frutas = ["mango","aguacate","arrow"]
print([x for x in frutas])

selection = input("Ingrese el nombre de la fruta que quiera eliminar: ")

if selection in frutas:
    frutas.remove(selection)
    print(frutas)
else:
    print("No existe esa fruta")