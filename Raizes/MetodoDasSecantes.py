class MetodoDasSecantes:

    def __init__(self):
        self.a = float(input("Digite o valor de x0: "))
        self.b = float(input("Digite o valor de x1: "))
        self.erroEsperado = float(input("Digite o erro esperado(precisão): "))

    def calculate(self):
        if not self.checkCondition(self.b, self.a):
            print("Condicao não satisfeita")
            return False

        erro = self.erroEsperado + 1
        i = 0

        xkMenos1 = self.a
        xk = self.b
        proximoPonto = xk

        while erro > self.erroEsperado or i < 10000:
            proximoPonto = (xkMenos1*self.f(xk) - xk*self.f(xkMenos1)) / (self.f(xk) - self.f(xkMenos1))
            i = i + 1

            erro = self.getErro(proximoPonto, xk)
            if erro < self.erroEsperado:
                break

            tempXk = xk
            xk = proximoPonto
            xkMenos1 = tempXk

        if erro > self.erroEsperado:
            print("Raiz não encontrada")
            return False

        return proximoPonto

    def checkCondition(self, nextElement, currentElement):
        return self.f(nextElement) - self.f(currentElement) != 0

    def f(self, x):
        return x**3 - x - 2

    def getErro(self, nextElement, current):
        return abs(nextElement - current) / abs(nextElement)