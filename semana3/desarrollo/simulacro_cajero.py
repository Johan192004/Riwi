historial = []

cuenta = {
    "nombre":"David Rivera",
    "contraseña":"6789",
    "saldo": 455623,
}

def verificar_entero(numero):

    while 1:

        if numero.isdigit():
            return int(numero) #Castear cast
        
        else:

            print("Error, Ingresaste un valor no valido.")
            numero = input("Porfavor ingresa un numero entero: ")

def verificar_positivo(numero,tipo):

    while 1:
        if numero>= 0:
            return numero
        else:

            print("Error, Ingresaste un numero negativo.")
            numero = input("Porfavor ingresa un numero positivo: ")
            
            if tipo == "int":

                numero = verificar_entero(numero)

            else:

                numero = verificar_float(numero)


def verificar_float(numero):

    while 1:

        try:
            numero = float(numero)

            return numero
        except ValueError:

            print("Error, ingresaste un valor no valido.")
            numero = input("Porfavor ingresa un numero valido: ")

def verificar_rango(principio,final,numero,tipo):
    
    while 1:
        if numero >= principio and numero <= final:
            return numero
        
        else:

            print("Error, el numero que ingresaste esta fuera de el rango permitido.")
            numero = input(f"Porfavor ingresa un numero del {principio} al {final}: ")

            if tipo == "int":

                numero = verificar_entero(numero)
            else:

                numero = verificar_float(numero)

def interfaz_contraseña():
    contraseña = input("Ingresa el pin de 4 digitos: ")


    for i in range(3):
        if contraseña.isdigit():

            if len(contraseña) == 4:

                if contraseña == cuenta["contraseña"]:
                    
                    print("=======================")
                    print(f"Bienvenido, {cuenta['nombre']}")
                    print("=======================")

                    break
                    
                else:

                    if i == 2:
                        continue

                    print("Pin incorrecto")
                    contraseña = input("Ingrese un pin de 4 digitos: ")

            else:
                if i == 2:
                        continue
                print("Error, El pin debe ser de 4 digitos: ")
                contraseña = input("Ingresa el pin de 4 digitos: ")
        else:

            if i == 2:
                continue
            print("Error, el pin tiene caracteres no numericos.")
            contraseña = input("Ingresa un pin de 4 digitos: ")

    else:


        print("=======================")
        print("Numero de intentos superados.")
        print("Su cuenta estara bloqueada por las proximas 24 horas \npor motivos de seguridad.")
        print("=======================")

        return 0
    
    main()

def main():



    print("1.Ver saldo de la cuenta.")
    print("2.Retirar dinero")
    print("3.Depositar dinero.")
    print("4.Ver historial de movimientos.")
    print("5.Salir del programa")

    opcion = input("Seleccione una opcion del 1 al 5: ")

    opcion = verificar_entero(opcion)

    opcion = verificar_rango(1,5,opcion,"int")

    if opcion == 1:
        opcion_1()
    elif opcion == 2:
        opcion_2()
    elif opcion == 3:
        opcion_3()
    elif opcion == 4:
        opcion_4()
    else:
        print("Saliendo....")


def opcion_1():

    print("=======================")
    print(f"Actualmente tiene {cuenta['saldo']}$.")
    print("=======================")
    

    main()

def opcion_2():
    
    if cuenta["saldo"] == 0:
        print("No cuenta con saldo para retirar un monto.")

    else:

        dinero = input("Ingrese la cantidad de dinero que desea retirar: ")

        dinero = verificar_float(dinero)
        dinero = verificar_positivo(dinero,"float")

        if cuenta["saldo"] >= dinero:

            cuenta["saldo"] -= dinero 

            print("=======================")
            print(f"Retirarse {dinero}$ de tu cuenta.")
            print("=======================")

            historial.append(("Retiro de dinero",dinero))

        else:

            print("=======================")
            print("Error, el monto que solicitas retirar es mayor al que actualmente tienes.")
            print("=======================")

    main()

def opcion_3():

    dinero = input("Ingrese la cantidad de dinero que ingresaras a la cuenta: ")

    dinero = verificar_float(dinero)
    dinero = verificar_positivo(dinero,"float")

    cuenta["saldo"] += dinero

    print("=======================")
    print(f"Has agregado {dinero}$ a tu cuenta.")
    print("=======================")

    historial.append(("Deposito de dinero",dinero))

    main()

def opcion_4():

    if len(historial) == 0:

        print("=======================")
        print("No hay movimientos registrados.")
        print("=======================")

    else:
        
        print("Historial de movimientos: ")

        for x in historial:

            print("============")
            print(f"Tipo de movimiento: {x[0]}")
            print(f"Monto: {x[1]}")
            print("============")

    main()

interfaz_contraseña()