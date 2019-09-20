import Menu
from Raizes.MetodoDeNewton import MetodoDeNewton
from Raizes.MetodoDaBisseccao import MetodoDaBisseccao
from Raizes.MetodoDasSecantes import MetodoDasSecantes
from EquacoesLineares.Gauss import Gauss

if __name__ == "__main__":
    menu = Menu.Menu()

    raiz = False

    if menu.getSubject() == 1:
        if menu.getMethod() == 1:
            metodo = MetodoDaBisseccao()
            raiz = metodo.calculate()
        elif menu.getMethod() == 2:
            metodo = MetodoDeNewton()
            raiz = metodo.calculate()
        elif menu.getMethod() == 3:
            metodo = MetodoDasSecantes()
            raiz = metodo.calculate()
        if raiz:
            print("A raiz da equacao é: ", raiz)

    elif menu.getSubject() == 2:
        if menu.getMethod() == 1:
            gauss = Gauss()
            solucao = gauss.calculate()