def verify_int(integer):
    """The function verifies that the given numer (integer) is
    in fact an integer.
    """

    while 1:
        try:
            integer = int(integer)

        # If the exception is raised, the program will display a message on
        # the screen sayiing that the given number is not valid, and it'll prompt the user
        # to enter a valid number again. 
        except ValueError:
            print("Ingresaste un numero no valido.")
            integer = input("Ingresa un numero entero valido: ")

        #If no exception is raised, the function will return the valid number
        else:
            return integer

def int_range(start,stop,number):
        """This function verifies that the given number is in fact in
        the given range
        """

        #The program will keep on iterating until the user enters a number
        # in the given range
        while True:

            #If the number is in range, the program will exit the while
            if number >= start and number <= stop:
                return number

            # Otherwise, the program will display a message saying that the number is not
            # in the given range, and it will promt the user to enter a valid number within the
            # range
            else:
                print("Ingresaste un numero fuera de rango")
                number = input(f"Ingresa un numero entero en el rango valido (del {start} al {stop}): ")
                number = verify_int(number)

#Main section of code
while True:
    #Printing the option menu
    print("1.Determinar estado de aprobacion")
    print("2.Ingresar calificaciones y mostrar resultados")
    print("3.Salir")

    #In this section, it's verified that the number is valid and is
    #within range (1-5)
    option = input("Ingrese una opcion (del 1 al 5): ")
    option = verify_int(option)
    option = int_range(1,3,option)

    if option == 1:
        print("Has seleccionado la opcion 1 (Determinar el estado de aprobación)")
        grade = input("Ingresa una calificacion del 0 al 100: ")

        #In this section, it's verified that the number is valid and is
        #within range (0-100) 
        grade = verify_int(grade)
        grade = int_range(0,100,grade)

        #Here is where the output starts
        print("=================================================")
        if grade >= 60 and grade < 80:

            print("El estudiante aprobó")
        elif grade >= 80 and grade <= 100:
            print("El estudiante aprobo (sobresaliente)")
        else:

            print("El estudiante reprobo")

        print("=================================================")
        #Here is where the output finishes

    
    elif option == 2:

        print("Has seleccionado la opcion 2 (Ingresar calificaciones y mostrar resultados)")

        #In this section, it's being used the function "map" to iterate over each element
        #of the given grades, appling the fuction "int" to each element separated by ","
        list_grades = list(map(int,input("Ingrese las calificaciones en separadas por comas: ").split(",")))


        #Variable that stores the specific value given by the user
        specific_value = input("Ingrese un valor especifico (entero): ")
        specific_value = verify_int(specific_value)
        specific_value = int_range(0,100,specific_value)

        #Section of the grades greater than the given number
        #===================================================

        #Variable for establishing the anchor number with which the system will count how many numbers
        #are above this one.
        border = specific_value
        count = 0
        index = 0

        while True:
            element = list_grades[index]

            if element > border:
                count += 1
            
            if index == len(list_grades)-1:
                break

            index += 1

        #Here is where the output starts
        print("=================================================")

        print(f"La cantidad de calificaciones mayores a {specific_value} es {count}")


        #Section of the grades that equal the given number
        #===================================================


        #Variable for establishing the number the user'd like to know how many times it's repeated
        #in the given grades
        selected_grade = specific_value
        count = 0

        for x in list_grades:

            if specific_value == x:
                count += 1


        if count >= 2:
            print(f"La calificacion {selected_grade} se repite {count} veces.")
        else:
            print(f"La calificacion {selected_grade} se repite {count} vez.")


        #Section of the sum of the grades
        #===================================================

        #Variable that will save the total sum of the grades
        sum = 0

        #Adding the numbers in the variable sum...
        for x in list_grades:

            sum += x


        mean = sum/len(list_grades)

        #The system will display the mean of the given grades with one point decimal
        print(f"El promedio de las calificaciones es de {mean:.1f}")
        print("=================================================")
        #Here is where the output finishes


    else:
        #If the other options are not selected, the system will close the program
        print("Cerrando sistema...")
        break