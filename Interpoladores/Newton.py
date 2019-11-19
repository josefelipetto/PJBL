class Newton:

    def __init__(self):
        self.x = [-2., -1., 0., 1., 2.]
        self.fx = [-1., 2., 4., 3., 1.]
        self.val = float(input("Digite o valor para interpolar com o polinômio: "))

        print("Valores de x: ", self.x)
        print("Valores de y: ", self.fx)

    def calculate(self):

        tabela = [[0] * len(self.x)] * len(self.x)

        result = 0

        for i in range(len(self.x)):
            for j in range(len(self.x) - i):
                if i == 0:
                    tabela[i][j] = self.fx[j]
                else:
                    tabela[i][j] = (tabela[i - 1][j + 1] - tabela[i - 1][j]) / (self.x[j + i] - self.x[j])

        for i in range(len(self.x)):
            temp = 1
            for j in range(i):
                temp *= (self.val - self.x[j])
            result += temp * tabela[i][0]

        print("O f({}) onde {} é o valor a ser interpolado é".format(self.val, self.val), round(result, 4))