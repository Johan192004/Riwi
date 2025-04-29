class IMC:
    def __init__(self,peso,altura):
        self.peso = peso
        self.altura = altura
        self.imc = self.peso/(self.altura**2)

    def bajo_peso(self):
        return "Bajo peso"
    
    def normal(self):
        return "Normal"
    
    def sobre_peso(self):
        return "Sobrepeso"
    
    def obesidad(self):
        return "Obesidad"

    

    

weight = float(input("Ingresa el peso en Kg: "))

height = float(input("Ingresa la altura en M: "))

objeto = IMC(weight,height)

if objeto.imc < 18.5:
    print(objeto.bajo_peso())
elif objeto.imc >= 18.5 and objeto.imc < 25:
    print(objeto.normal())
elif objeto.imc >= 25 and objeto.imc <= 29.9:
    print(objeto.sobre_peso())
else:
    print(objeto.obesidad())