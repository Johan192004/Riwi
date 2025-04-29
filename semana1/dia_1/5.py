valor_cuenta = int(input("Ingrese el valor total de la cuenta: "))

porcentaje_propina = int(input("Ingrese el porcentaje de propina, este debe ser del 10, 15 o 20 porcentaje: "))

while True:
    if porcentaje_propina == 10 or porcentaje_propina == 15 or porcentaje_propina == 20:
        break
    else:
        print("La propina debe ser del 10, 15 o 20 porciento")
    
    porcentaje_propina = int(input("Ingrese nuevamente la propina: "))

propina = (valor_cuenta*porcentaje_propina)/100


valor_total = valor_cuenta + propina

print(f"El valor de la propina es: {propina}, y el valor total es: {valor_total}")