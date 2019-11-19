class Trapezio:

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

    def f(self, x):
        return 1 / (1 + x)

    def calculate(self):

        val = 0

        for i in range(self.numeroDeIteracoes):
            val += self.h / 2 * (self.f(self.intervalo[0] + (self.h * i)) + self.f(self.intervalo[0] + (self.h * (i + 1))))

        return val
