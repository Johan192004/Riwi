products = {}

def verify_float(decimal):
    """Function that verifies that a given number (str) can be casted to float.

    Args:
        decimal (str): The string that is going to be casted to float.

    Returns:
        decimal (float): The decimal number after being casted from string to float.
    """

    while 1:
        try:
            decimal = float(decimal)
            return decimal
        
        except ValueError:
            decimal = input("Ingresaste un valor no valido, porfavor ingrese un numero valido: ")

def verify_int(number):
    """Function that verifies that a given number (str) can be casted to int.

    Args:
        number (str): The number as a string.

    Returns:
        number (int): The number after being casted to int.
    """

    while 1:
        if number.isnumeric():
            return int(number)
        
        else:
            number = input("Ingresaste un valor no valido, porfavor ingrese un numero valido: ")

def verify_positive(number,kind_of):
    """Function that verifies that a given number is positive (>= 0).

    Args:
        number (int or float): The number that is going to be verified.
        kind_of (str): The kind of number (int or float).

    Returns:
        number (int or float): The verified number.
    """


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
    """Function that verifies that a number (int or float) is within a given range.

    Args:
        start (int or float): The lowest limit of the number.
        end (int or float): The highest limit of the number.
        number (int or float): The number.
        kind_of (str): The kind of number (int or float).

    Returns:
        number (int or float): The verified number
    """

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
    """Main function
    """

    print("1.Añadir productos")
    print("2.Consultar producto")
    print("3.Actualizar precio de un producto")
    print("4.Eliminar producto")
    print("5.Calcular el valor total del inventario")
    print("6.Salir")

    option = input("Seleccione una opcion del 1 al 6: ")

    option = verify_int(option)
    option = verify_range(1,6,option,"int")

    if option == 1:
        option_1()
    elif option == 2:
        option_2()
    elif option == 3:
        option_3()
    elif option == 4:
        option_4()
    elif option == 5:
        option_5()
    else:
        print("Saliendo...")


def option_1():
    """Function that verifies that, in fact, there is at least one product in the products' dictionary.
    Then, the function verifies that the product's name given by the user exists. Finally, the function executes
    the add product function. 
    """

    name = input("Ingrese el nombre del producto: ")

    if name in products.keys():

        #Output
        print("============================")
        print(f"El producto con nombre {name} ya existe.")
        print("============================")

    else:
        price = input("Ingrese el precio del producto: ")
        price = verify_float(price)
        price = verify_positive(price,"float")

        quantity = input("Ingrese la cantidad del producto disponible: ")
        quantity = verify_int(quantity)
        quantity = verify_positive(quantity,"int")

        add_product(name,price,quantity)
    
    main()


def option_2():
    """Function that verifies that, in fact, there is at least one product in the products' dictionary.
    Then, the function verifies that the product's name given by the user exists. Finally, the function executes
    the search for product function. 
    """

    if len(products) == 0:

        #Output
        print("============================")
        print("No hay productos registrados.")
        print("============================")

    else:

        print("")

        name = input("Ingrese el nombre del producto que desea saber su informacion: ")

        if name not in products.keys():

            #Output
            print("============================")
            print(f"El producto con nombre {name} no existe.")
            print("============================")

        else:

            search_for_product(name)

    main()


def option_3():
    """Function that verifies that, in fact, there is at least one product in the products' dictionary.
    Then, the function verifies that the product's name given by the user exists. Finally, the function executes
    the update price function, 
    """


    if len(products) == 0:

        #Output
        print("============================")
        print("No hay productos registrados.")
        print("============================")

    else:


        name = input("Ingrese el nombre del producto al que le desea modificar el precio: ")

        if name not in products.keys():

            #Output
            print("============================")
            print(f"El producto con nombre {name} no se encuentra registrado.")
            print("============================")

        else:

            price = input("Ingrese el nuevo precio del producto: ")
            price = verify_float(price)
            price = verify_positive(price,"float")

            update_price(name,price)
        
    
    main()

def option_4():
    """Function that verifies that, in fact, there is at least one product in the products' dictionary.
    Then, The function verifies that the product's name given by the user exists. Finally, The function executes
    the delete product function.
    """


    if len(products) == 0:

        #Output
        print("============================")
        print("No hay productos registrados.")
        print("============================")

    else:


        name = input("Ingrese el nombre del producto que desea eliminar: ")

        if name not in products.keys():

            #Output
            print("============================")
            print(f"El producto con nombre {name} no se encuentra registrado.")
            print("============================")

        else:

            delete_product(name)

    main() 

def option_5():
    """Function #5 that verifies that, in fact, there is at least one product and then executes 
    the calculte total inventoy function.
    """

    if len(products) == 0:


        #Output
        print("============================")
        print("No hay productos registrados.")
        print("============================")
    
    else:
        calculate_total_inventory()

    main()
    
def add_product(name,price,quantity):
        """Function that adds a product to the products' dictionary, where each key is the name 
        and it's assigned to each key a tuple where price and quantity of the products are stored.

        Args:
            name (str): The name of the person.
            price (float): The price of the product.
            quantity (int): The quantity of the product.
        """
        
        
        products[name] = (price,quantity)

        #Output
        print("============================")
        print(f"Se ha registrado el producto con nombre {name} exitosamente.")
        print("============================")

def search_for_product(name):
    """Function that searches for a product and display on the screen the atributes of each product.

    Args:
        name (str): The name of the product.
    """
    product = products[name]

    #Output
    print("============================")
    print(f"Nombre del producto: {name}")
    print(f"Precio del producto: {product[0]}")
    print(f"Cantidad del producto: {product[1]}")
    print("============================")

def update_price(name,price):
    """Function that updates the price of a product.

    Args:
        name (str): The name of the product.
        price (float): The price of the product.
    """

    products[name] = (price,products[name][1])

    #Output
    print("============================")
    print(f"Se ha cambiado el precio del producto {name} a {price}.")
    print("============================")

def delete_product(name):
    """Function that deletes a product.

        Args:
            name (str): The name of the product.
    """

    del products[name]

    #Output
    print("============================")
    print(f"Se ha eliminado el producto con nombre {name} exitosamente.")
    print("============================")

def calculate_total_inventory():
    """Function that calculates the total inventory.
    """

    total_money = 0

    #Lambda function that adds the two given numbers
    adding_money = lambda x,y: x + y

    for i in products.values():

        total_money = adding_money(total_money,i[0]*i[1])

    #Output
    print("============================")
    print(f"La cantidad total de inventario es {total_money}.")
    print("============================")

#Execution of the main function
main()