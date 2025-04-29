books = {}

def interfaz():

    print("1.Agregar libro")
    print("2.Leer libro")
    print("3.Modificar un libro")
    print("4.Eliminar un libro")
    print("5.Salir")

    option = input("Seleccione una opcion: ")

    option = verify_int(option)

    while 1:

        if option >= 1 and option <= 5:
            break

        else:
            
            print("Error: Su numero no esta en el rango de opciones")
            option = input("Ingrese un número del 1 al 5: ")

            option = verify_int(option)

    if option == 1:
        option_1()
    elif option == 2:
        option_2()
    elif option == 3:
        option_3()
    elif option == 4:
        option_4()
    else:
        print("Saliendo del sistema...")
        return

def verify_int(number):

    while 1:

        try:

            number = int(number)

        except ValueError:

            number = not_expected_value()

        else:
            return number

def not_expected_value():

    print("Ingresaste un valor incorrecto")
    item = input("Ingrese un valor correcto: ")
    return item
        
def option_1():

    id = input("Ingrese el id del libro: ")

    id = verify_int(id)
    
    while 1:

        if id >= 0 and id <= 999:
            break
        else:

            print("Error, ingresaste un numero fuera de rango")
            id = input("Ingresa un numero del 0 al 999: ")
            id = verify_int(id)


    
    id = (3-len(str(id)))*"0" + str(id)


    if id in books.keys():

        print(f"Error, el registro con id {id} ya existe.")

    else:

        title = input("Ingrese el titulo del libro: ")
        author = input("Ingrese el nombre del autor: ")

        release_year = input("Ingrese el año de publicacion del libro: ")

        release_year = verify_int(release_year)

        while 1:
            if release_year >= 0 and release_year <= 2025:
                break
            else:
                print("Error, año de publicacion fuera de rango")
                release_year = input("Ingrese un año de publicacion valido")
                release_year = verify_int(release_year)

        books[id] = {"titulo":title,"autor":author,"año":release_year}
        print(f"Libro con id {id} agregado exitosamente.")


    interfaz()

def option_2():
    
    if len(books) == 0:
        print("No hay libros registrados")

    else:

        for key,value in books.items():

            print("")
            print(f"Id: {key}")
            print(f"Titulo: {value["titulo"]}")
            print(f"Autor: {value["autor"]}")
            print(f"Año: {value["año"]}")
            print("")
    
    interfaz()
  
def option_3():

    if len(books) == 0:

        print("No hay libros registrados para modificar")

    else:

        id = input("Ingrese el id del libro que desea modificar: ")

        id = verify_int(id)
        
        while 1:

            if id >= 0 and id <= 999:
                break
            else:

                print("Error, ingresaste un numero fuera de rango")
                id = input("Ingresa un numero del 0 al 999: ")
                id = verify_int(id)


        
        id = (3-len(str(id)))*"0" + str(id)

        if id not in books.keys():
            print(f"El registro con id {id} no existe")

        else:


            title = input("Ingrese el titulo del libro: ")
            author = input("Ingrese el nombre del autor: ")

            release_year = input("Ingrese el año de publicacion del libro: ")

            release_year = verify_int(release_year)

            while 1:
                if release_year >= 0 and release_year <= 2025:
                    break
                else:
                    print("Error, año de publicacion fuera de rango")
                    release_year = input("Ingrese un año de publicacion valido: ")
                    release_year = verify_int(release_year)

            books[id] = {"titulo":title,"autor":author,"año":release_year}
            print(f"Libro con id {id} modificado exitosamente.")

    interfaz()

def option_4():

    if len(books) == 0:
        print("No hay libros que eliminar")

    else:

        id = input("Ingrese el id del libro que desea eliminar: ")
        id = verify_int(id)


        while 1:

            if id >= 0 and id <= 999:
                break
            else:

                print("Error, ingresaste un numero fuera de rango")
                id = input("Ingresa un numero del 0 al 999: ")
                id = verify_int(id)


        id = (3-len(str(id)))*"0" + str(id)

        if id not in books.keys():

            print(f"El libro con id {id} no esta registrado")

        else:

            books.pop(id)

            print(f"Se ha eliminado el libro con id {id} correctamente")

    interfaz()

interfaz()