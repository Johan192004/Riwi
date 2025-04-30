
agenda = {}

while 1:
    print("Opcion 1: Agregar contactos")
    print("Opcion 2: Mostrar contactos")
    print("Opcion 3: Actualizar contactos")
    print("Opcion 4: Eliminar contactos")
    print("Opcion 5: Salir")


    opcion = input("Digite una opcion: " )

    while 1:
        try:
            opcion = int(opcion)
            break
        except ValueError:

            print("Valor incorrecto")

            opcion = input("Digite un número del 1 al 5: ")

    while 1:
        if opcion <= 5 and opcion >= 1:
            break
        else:
            print("Tu numero no esta en el rango esperado")
            opcion = input("Digite un número del 1 al 5: ")

            while 1:
                try:
                    opcion = int(opcion)
                    break
                except ValueError:

                    print("Valor incorrecto")

                    opcion = input("Digite un número del 1 al 5: ")


    if opcion == 1:
        nombre = input("Digite el nombre: ")

        if nombre in agenda.keys():
            print("El nombre ya se encuentra")
            continue
        else:
            pass


        tele = input("Digita el número telefonico: ")
        while 1:
            if tele.isnumeric():
                if len(tele) == 10:
                    break
                else:
                    print("Error: Valor incorrecto")
                    tele = input("Digite un número de 10 digitos: ")
            else:
                print("Error: Valor incorrecto")
                tele = input("Digite un número de 10 digitos: ")
        email = input("Digita el email: ")
        while 1:
            if "@" in email:
                if "." in email:
                
                    break
                else:
                    print("Correo no valido. Te falto el .")
                    email = input("Digita el email: ")
            else:
                print("Correo no valido. Te falto el @")
                email = input("Digita el email: ")


        print("Contacto Registrado Con Exito.")

        agenda[nombre] = 

        

        










