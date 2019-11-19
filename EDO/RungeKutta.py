class RungeKutta:

    def __init__(self):
        self.intervalo = []
        self.y = []

        self.intervalo.append(
            float(input("Ínicio do intervalo: "))
        )

        self.intervalo.append(
            float(input("Final do intervalo: "))
        )

        self.intervalo.append(
            float(input("f(x) inicial: "))
        )

        self.h = float(input("Digite o h: "))

        self.maxn = int(round(((self.intervalo[1] - self.intervalo[0]) / self.h), 10))

        self.x = ([round(a * self.h, 10) for a in range(self.maxn + 1)])

    def f(self, x, y):
        return -2 + x + y

    def calculate(self):
        for n in range(self.maxn):
            k1 = self.f(self.x[n], self.y[n])
            k2 = self.f(self.x[n] + self.h / 2, self.y[n] + (self.h / 2 * k1))
            k3 = self.f(self.x[n] + self.h / 2, self.y[n] + (self.h / 2 * k2))
            k4 = self.f(self.x[n] + self.h, self.y[n] + self.h * k3)
            y.append(self.y[n] + self.h / 6 * (k1 + 2 * (k2 + k3) + k4))

        for i in range(self.maxn + 1):
            print("Xn {} | Yn {} \n".format(self.x[i], self.y[i]))