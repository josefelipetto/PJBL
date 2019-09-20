class MetodoDeNewton:

    def __init__(self):
        self.pontoInicial = float(input("Defina um ponto inicial: "))
        self.erroEsperado = float(input("Defina um erro esperado: "))

    def calculate(self):
        erro = self.erroEsperado + 1
        i = 0

        ponto = self.pontoInicial

        if self.derivada(ponto) == 0:
            print("Derivada no ponto é 0. Abortando...")
            return False

        proximoPonto = ponto

        while erro > self.erroEsperado or i < 10000:
            valorNoPonto = self.f(ponto)
            derivadaNoPonto = self.derivada(ponto)
            proximoPonto = ponto - (valorNoPonto / derivadaNoPonto)
            erro = abs(proximoPonto - ponto) / abs(proximoPonto)
            i = i + 1
            ponto = proximoPonto

        if erro > self.erroEsperado:
            print("Raiz não encontrada")
            return False

        return proximoPonto

    def f(self, x):
        return x ** 3 - 2 * x - 17

    def derivada(self, x):
        return 3 * x ** 2 - 2
