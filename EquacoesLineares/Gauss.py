class Gauss:

    def __init__(self):
        self.sistema = [
            [5, 2, 1],
            [3, 1, 4],
            [1, 1, 4],
        ]

        self.b = [7, 7, 13]

        self.n = len(self.sistema)

        self.checkPivots()

    def checkPivots(self):
        for i in range(0, self.n):
            if self.sistema[i][i] == 0:
                print("A[", i, "][", i, "] = 0. Abortando")

    def calculate(self):
        for k in range(0, self.n):
            for i in range(k+1, self.n):
                for j in range(k, self.n):
                    self.sistema[i][j] = self.sistema[i][j] - self.sistema[k][j] * self.sistema[i][k]/self.sistema[k][k]

        for k in range(0, self.n):
            for i in range(k+1, self.n):
                for j in range(k, self.n):
                    self.b[i] = self.b[i] - (self.b[k] * self.sistema[i][k] / self.sistema[k][k])