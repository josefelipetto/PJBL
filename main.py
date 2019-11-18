import Menu
from Raizes.MetodoDeNewton import MetodoDeNewton
from Raizes.MetodoDaBisseccao import MetodoDaBisseccao
from Raizes.MetodoDasSecantes import MetodoDasSecantes
from EquacoesLineares.Gauss import Gauss
from Interpoladores.Lagrange import Lagrange
from Interpoladores.Newton import Newton

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
        elif menu.getMethod() == 2:
            print('LU')
        elif menu.getMethod() == 3:
            print('Jacobi')
    elif menu.getSubject() == 3:
        if menu.getMethod() == 1:
            metodo = Lagrange()
            metodo.calculate()
        elif menu.getMethod() == 2:
            metodo = Newton()
            metodo.calculate()
    elif menu.getSubject() == 4:
        if menu.getMethod() == 1:
            print('Trpezio')
        elif menu.getMethod() == 2:
            print('1/3')
        elif menu.getMethod() == 3:
            print('3/8')
    elif menu.getSubject() == 5:
        if menu.getMethod() == 1:
            print('Runge Gitta')