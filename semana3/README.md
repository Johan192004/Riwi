## How to execute the program

In order to execute the program, first you must be in the mock_students directory. Then, you must run the main.py module.

## Inputs and outputs

The program works with numeric options, where the system displays the range of the option in relation with the
election of the user. When it comes to the output section, depending on the kind of operation the user is 
performing, the system will display colored messages mentioning the kind of output (red(DANGER), yellow(WARNING) and green(SUCCESS)). There are some options that display a list of students, in these ones, there is
only colored messages at the begining and the end of the message displayed provided that the operation was executed successfuly.

# Example of input

1.Agregar estudiantes
2.Buscar un estudiante
3.Actualizar la informacion de un estudiante
4.Eliminar estudiante
5.Calcular el promedio de notas
6.Listar a los estudiantes dado un umbral
7.Salir
Seleccione una opcion del 1 al 7: 

In the given example, you see that the system displays the posibles options for the user to choose, and then it prompts a number from the user. In this case the number must be between one and seven.

# Exaple of output

Se ha eliminado al estudiante con id #1 exitosamente

In the given example, this message is shown in a green colored, because it's been deleted a student from the students dictionary.

## Explanation of the code

# main.py

In this module is where the "main functions" are. Some of the are the backbone of the program to work. For instance, for each option, there is an option function. There is the main funcion too, that shows the list of
options. There is also the students dictionary.

# verify.py

In this module is where are all the functions that verify different kinds of thins, like the verification of a
string before casting it to an integer, and so on with the other data types that are used in this program.