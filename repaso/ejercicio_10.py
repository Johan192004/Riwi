edad = int(input("Ingresa tu edad: "))

if edad >= 0 and edad < 14:
    print("Eres niño")
elif edad >= 14 and edad<18:
    print("Eres adolecente")
elif edad >= 18 and edad < 60:
    print("Eres un adulto")
else:
    print("Eres un anciano")