class Lagrange:

    def __init__(self):

        self.value = float(input("Qual valor será calculado pelo polinômio? "))

        self.values = {
            "x": [
                -1, 0, 3
            ],
            "y": [
                15, 8, -1
            ]
        }

        print("X: ", self.values["x"])
        print("Y: ", self.values["y"])

    def checkRepeated(self):
        repeated = set([x for x in self.values["x"] if self.values["x"].count(x) > 1])
        return len(repeated) > 0

    def calculate(self):

        if self.checkRepeated():
            print("Há valores repetidos no vetor X. Verifique. ")
            return

        lk = [1.] * len(self.values["x"])

        denominator = [1] * len(self.values["x"])

        result = 0

        for i in range(len(self.values["x"])):

            if i == 0:
                for j in range(1, len(self.values["x"])):
                    lk[i] *= (self.value - self.values["x"][j])
                    denominator[i] *= (self.values["x"][i] - self.values["x"][j])
                continue

            for j in range(len(self.values["x"])):
                if j != i:
                    lk[i] *= (self.value - self.values["x"][j])
                    denominator[i] *= (self.values["x"][i] - self.values["x"][j])

        for count in range(len(self.values["x"])):
            lk[count] = (lk[count] * self.values["y"][count] *
                         (max(denominator) / denominator[count])) / (max(denominator))

        for i in range(len(self.values["x"])):
            result += lk[i]

        # Usamos round 4 pois o python faz contas com binários e números que deveriam ser inteiros possuem
        # "ruídos" nas últimas casas decimais
        # todo: CHANGE THIS TO RETURN VALUES
        print("O f({}) onde {} é o valor a ser interpolado é".format(self.value, self.value), round(result, 4))
