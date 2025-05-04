products = {}

def verify_float(decimal):
    while 1:
        try:
            decimal = float(decimal)
            return decimal
        
        except ValueError:
            decimal = input("Ingresaste un valor no valido, porfavor ingrese un numero valido: ")

def verify_int(number):
    while 1:
        if number.isnumeric():
            return int(number)
        
        else:
            number = input("Ingresaste un valor no valido, porfavor ingrese un numero valido: ")

def verify_positive(number,kind_of):

    while 1:
        if number >= 0:
            return number
        else:

            number = input("Ingresaste un numero negativo, porfavor ingresa un numero positivo: ")
            
            if kind_of == "int":
                number = verify_int(number)
            elif kind_of == "float":
                number = verify_float(number)


def verify_range(start,end,number,kind_of):

    while 1:
        if number >= start and number <= end:
            return number
        else:
            number = input(f"El numero no esta en el rango, porfavor ingrese un numero del {start} al {end}: ")
            
            if kind_of == "int":
                number = verify_int(number)
            elif kind_of == "float":
                number = verify_float(number)

def main():

    print("1.Añadir productos")
    print("2.Consultar producto")
    print("3.Actualizar precio de un producto")
    print("4.Eliminar producto")
    print("5.Calcular el valor total del inventario")
    print("6.Salir")

    option = input("Seleccione una opcion del 1 al 6: ")

    option = verify_int(option)
    option = verify_range(1,6,option,"int")


def option_1_add_products():

    print("")

    name = input("Ingrese el nombre del producto: ")

    if name in products.keys():
        print(f"El producto con nombre {name} ya existe.")

    else:
        price = input("Ingrese el precio del producto: ")
        price = verify_float(price)
        price = verify_positive(price,"float")

        quantity = input("Ingrese la cantidad del producto disponible: ")
        quantity = verify_int(quantity)
        quantity = verify_positive(quantity,"int")


        products[name] = (price,quantity)

        print(f"Se ha registrado el producto con nombre {name} exitosamente.")
    
    main()


def option_2_search_for_products():

    print("")

    name = input("Ingrese el nombre del producto que desea saber su informacion: ")

    if name not in products.keys():

        print(f"El producto con nombre {name} no existe.")

    else:

        product = products[name]

        print("============================")
        print(f"Nombre del producto: {name}")
        print(f"Precio del producto: {product[0]}")
        print(f"Cantidad del producto: {product[1]}")
        print("============================")


    main()


def option_3_update_product():

    
