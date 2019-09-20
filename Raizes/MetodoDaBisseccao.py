import math


class MetodoDaBisseccao:

    def __init__(self):
        self.a = float(input("De um valor para a:"))
        self.b = float(input("De um valor para b:"))
        self.erroEsperado = float(input("De um erro esperado(precisao): "))

    def calculate(self):

        if not self.checkBolzano(self.a, self.b):
            print("f(a) * f(b) > 0. Abortando...")
            return False

        erro = self.erroEsperado + 1
        i = 0
        a = self.a
        b = self.b
        pontoMedio = 0
        fPontoA = self.f(a)

        while erro > self.erroEsperado or i <= 100000:

            pontoMedio = a + (b-a)/2
            fPontoMedio = self.f(pontoMedio)
            erro = self.getErro(pontoMedio, a)

            if fPontoMedio == 0:
                break

            if fPontoA * fPontoMedio > 0:
                a = pontoMedio
                fPontoA = fPontoMedio
            else:
                b = pontoMedio

            i = i + 1

        if erro > self.erroEsperado:
            print("Raiz nao encontrada")
            return False

        return pontoMedio

    def f(self, x):
        return x**3 - x - 2

    def checkBolzano(self, a, b):
        return self.f(a) * self.f(b) < 0

    def getErro(self, nextElement, current):
        return abs(nextElement - current) / abs(nextElement)