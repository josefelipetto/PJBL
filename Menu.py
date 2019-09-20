class Menu:

    def __init__(self):
        print("================================ PjBL ================================\n")
        print("Aluno: José Henrique Medeiros Felipetto")
        print("Qual o assunto ?")
        self.themeOption = int(input('1 - Raízes ; 2 - Sistemas de equações lineares; 3 - Interpolação; 4 - Integração '
                                 'Numérica; 5 - Equações diferenciais ordinárias. \n'))
        self.choosenOption = int(self.subLevelMenu())
        print("=======================================================================\n")

    def subLevelMenu(self):
        print("Escolha qual método deseja utilizar: ")
        if self.themeOption == 1:
            return input("1 -> Método da bisseccção ; 2 -> Newton; 3 -> Método das secantes")
        elif self.themeOption == 2:
            return input("1 -> Eliminação de Gauss; 2 -> Decomposição LU; 3 -> Jacobi-Richardson; 4 -> "
                                       "Gauss-Seidel")
        elif self.themeOption == 3:
            return input("1 -> Lagrange; 2 -> Newton")
        elif self.themeOption == 4:
            return input("1 -> Trapézio; 2 -> 1/3 de SImpson; 3 -> 3/8 de Simpson")
        elif self.themeOption == 5:
            return input("1 -> Runge-Kutta 4a Ordem")
        else:
            print("Opção não permitida")

    def getSubject(self):
        return self.themeOption

    def getMethod(self):
        return self.choosenOption
