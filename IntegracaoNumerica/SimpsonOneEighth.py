class SimpsonOneEigth:

    def __init__(self):

        self.intervalo = []

        print("F(x) =  1/(1+x) ")

        self.intervalo.append(
            float(input("Ínicio do intervalo: "))
        )

        self.intervalo.append(
            float(input("Final do intervalo: "))
        )

        self.numeroDeIteracoes = int(input("Número de iterações: "))

        self.h = (self.intervalo[1] - self.intervalo[0]) / self.numeroDeIteracoes

    def checkInteracoes(self):
        return self.numeroDeIteracoes % 2 == 0

    def f(self, x):
        return 1 / (1 + x)

    def calculate(self):

        if not self.checkInteracoes():
            print("Número de interações deve ser múltiplo de 2")
            return None

        val = 0

        for i in range(self.numeroDeIteracoes + 1):
            if i == 0:
                val += self.h / 3 * self.f(self.intervalo[0])
            elif i == self.numeroDeIteracoes:
                val += self.h / 3 * self.f(self.intervalo[1])
            elif i % 2 != 0:
                val += self.h / 3 * (4 * self.f(self.intervalo[0] + (self.h * i)))
            else:
                val += self.h / 3 * (2 * self.f(self.intervalo[0] + (self.h * i)))

        return val
