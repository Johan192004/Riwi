año = int(input("Ingresa un año: "))

if año % 4 == 0:

    if año % 100 == 0:

        if año % 400 == 0:
            print("Es bisiesto")

        else:
            print("No es bisiesto")
    else:

        print("Es bisiesto")


else:
    print("No es bisiesto")

