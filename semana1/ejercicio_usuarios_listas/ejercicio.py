true_list = []

def remplazar_usuario(lista,index,name,surname,age,mail):

    lista[index] = [name,surname,age,mail]

def show_elements(lista):

    contador = 0
    for x in lista:
        print("")
        print(f"Registro #{contador}")
        print(f"Nombre: {x[0]}")
        print(f"Apellido: {x[1]}")
        print(f"Edad: {x[2]}")
        print(f"Correo: {x[3]}")
        print("")

        contador += 1

def valor_no_valido():
    print("Error, ingresaste un valor no valido")
    elemento = input("Ingrese un valor valido: ")
    return elemento

def verificar_correo():
    mail = input("Ingrese el correo del usuario: ")

    while 1:
        if "@" in mail and "." in mail:
            return mail
        else:
            print("Correo no valido")
            mail = input("Ingrese un correo valido: ")


def verificar_entero(elemento):
    while 1:
        try:
            elemento = int(elemento)
        except ValueError:
            elemento = valor_no_valido()
        else:
            if isinstance(elemento,float):
                elemento = valor_no_valido()
            else:
                return elemento
def verificar_float(elemento):
    while 1:
        try:
            elemento = float(elemento)
        except ValueError:
            elemento = valor_no_valido()
        else:
            pass


def agregar_usuario(lista,name,surname,age,mail):

    is_in = False

    for x in lista:

        if mail == x[3]:
            is_in = True
            break

    if is_in:

        print(f"Error, Usuario ya registrado con correo {mail}")

    else:

        print("Se ha registrado al usuario:")
        print(f"Nombre: {name}")
        print(f"Apellido: {surname}")
        print(f"Edad: {age}")
        print(f"Correo: {mail}")

        lista.append([name,surname,age,mail])
    

def eliminar_elemento(lista,elemento):
    lista.remove(elemento)

def opcion_1(lista):
    print("Seleccionaste la opcion 1 (Agregar usuario)")

    nombre = input("Ingrese el nombre del usuario: ")

    apellido = input("Ingrese el apellido del usuario: ")


    edad = input("Ingrese la edad del usuario: ")


    edad = verificar_entero(edad)

    while 1:

        if edad >= 0:
            break
        else:
            edad = verificar_entero(edad)

    correo = verificar_correo()

    agregar_usuario(lista, nombre, apellido, edad, correo)

    interfaz()


def opcion_2(lista):
    print("Seleccionaste la opcion 2 (Mostrar usuarios)")

    if len(lista) == 0:
        print("No hay usuarios registrados.")

    else:
        show_elements(lista)

    interfaz()

def opcion_3(lista):
    print("Seleccionaste la opcion 3 (Actualizar usuario)")


    if len(lista) == 0:
        print("No hay usuarios registrados")
    else:
        show_elements(lista)

        index = input("Ingrese el # de registro que desea actualizar")

        index = verificar_entero(index)

        if index < 0 and index >= len(lista):
            print("# de registro no valido")
        else:


            nombre = input("Ingrese el nombre del usuario: ")

            apellido = input("Ingrese el apellido del usuario: ")


            edad = input("Ingrese la edad del usuario")


            edad = verificar_entero(edad)

            while 1:

                if edad >= 0:
                    break
                else:
                    edad = verificar_entero(edad)

            correo = verificar_correo(correo)

            is_in = False

            for x in lista:

                if correo == x[3]:
                    is_in = True
                    break

            if is_in:

                print(f"Error, Usuario ya registrado con correo {correo}")

            else:
                remplazar_usuario(lista,index,nombre,apellido,edad,correo)

    interfaz()

def opcion_4(lista):
    print("Seleccionaste la opcion 4 (Eliminar usuarios)")

    if len(lista) == 0:
        print("No hay registros disponibles")
    else:

        show_elements(lista)

        index = input("Ingrese el # de registro que desea eliminar")


        index = verificar_entero(index)


        if index < 0 and index >= len(lista):
            print("# de registro no valido")
        else:

            del lista[index]

            print("Se ha eliminado el usuario correctamente")

    interfaz()

def interfaz():
    print("")
    print("1.Agregar usuario")
    print("2.Mostrar usuarios")
    print("3.Actualizar usuario")
    print("4.Eliminar usuario")
    print("5.Salir")



    entrada = input("Seleccione una opcion: ")

    opcion = verificar_entero(entrada)

    while 1:

        if opcion >= 1 and opcion <= 5:
            break
        else:
            opcion = verificar_entero(opcion)

    if opcion == 1:
        opcion_1(true_list)
    elif opcion == 2:
        opcion_2(true_list)
    elif opcion == 3:
        opcion_3(true_list)
    elif opcion == 4:
        opcion_4(true_list)
    else:
        print("Cerrando...")



interfaz()
