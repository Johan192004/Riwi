licencia = bool(int(input("Tiene licencia? \n Si (ingrese 1)\n No (ingrese 0)")))
casco = bool(int(input("Lleva casco? \n Si (ingrese 1)\n No (ingrese 0)")))

if not licencia or not casco:
    print("No puede conducir")
else:
    print("Puede conducir")