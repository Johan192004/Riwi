primer_numero = int(input("Ingresa el primer numero: "))
segundo_numero = int(input("Ingresa el segundo numero: "))

if primer_numero == segundo_numero:
    print("Los numeros son iguales")
elif primer_numero < segundo_numero:
    print(f"El segundo numero {segundo_numero} es mayor al primer numero {primer_numero}")
else:
    print(f"El primer numero {primer_numero} es mayor al primer numero {segundo_numero}")