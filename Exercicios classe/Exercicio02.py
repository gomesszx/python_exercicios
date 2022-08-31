class Triangulo:
    def __init__(self,lado_a,lado_b,lado_c):

        lado_a = int(lado_a)
        lado_b = int(lado_b)
        lado_c = int(lado_c)
        
        self.lado_a = lado_a
        self.lado_b = lado_b
        self.lado_c = lado_c
        


    def calcular_perimetro(self):
        soma_lados = self.lado_a + self.lado_b + self.lado_c
        return soma_lados

ladoA = input()
ladoB = input()
ladoC = input()

triangulo = Triangulo(ladoA, ladoB, ladoC)
print(triangulo.calcular_perimetro())