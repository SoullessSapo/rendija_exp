import numpy as np
import matplotlib.pyplot as plt
from qiskit.visualization import plot_histogram

def m_bool(m,vector,clicks):
    m = np.squeeze(np.asarray(m))
    clicks = int(clicks)
    vector = np.array(vector)
    m = m ** clicks
    res = m * vector
    return res
def rendija_1(m,clicks):
    m = m
    q = 0
    r = x.shape
    sapo = []

    for i in range(r[0]):
        clicks = int(clicks)
        if clicks == 1:
            for j in range(r[1]):
                q = x[i][j]
                if q != 0:
                    sapo.append(q)

        elif clicks == 2:
            m = m*m*m
            for j in range(r[1]):
                q = x[i][j]
                if q != 0:
                    sapo.append(q)

        else:
            return 'se sale del rango'

        return 'la probabilidad de la matriz en', clicks, 'es de', sapo
def rendija_2(cant_rendijas,clicks):
    cant_rendijas = int(cant_rendijas)
    click_2 = int(1+2*cant_rendijas)
    click_1 =int(cant_rendijas)
    prob_1 = 1/click_1
    prob_2 = 1/click_2
    x = int(click_2/2)
    clicks = int(clicks)
    m = np.zeros(click_2, click_2)
    if clicks == 1:
        m = np.zeros([click_1,0])
        for i in range(1, click_1):
            m[0][0] = 0
            m[i][0] = prob_1
    if clicks == 2:
        m = np.zeros([click_2,1])
        for i in range(1, click_1):
            m[0][0] = 0
            m[i][0] = prob_1
            for j in range(clicks + 1, x):
                m[i][1] = 0
                m[j][1] = prob_2
                for r in range(x, click_2):
                    m[r][2] = prob_2
    return m
def main():
    x = int(input("eliga si quiere \n"
              "1. hallar booleano \n"
              "2. sacar probabilidad matriz despues de n clicks\n"
              "3. hacer experimento de rendijas con n rendijas"))
    if x ==1:
        m = []
        filas = int(input( 'digite numero de filas de la matriz'))
        columnas = int(input('introduce numero de columnas matriz'))
        for i in range(filas):
            m.append([])
            for j in range(columnas):
                valor = complex(input("fila {}, columna {}:".format(i+1,j+1)))
                m[i].append(valor)
        q = input("ingrese vector")
        e = input("ingrese la cantidad de clicks")
        res = m_bool(m,q,e)
    elif x ==2:
        m = []
        filas = int(input('digite numero de filas de la matriz'))
        columnas = int(input('introduce numero de columnas matriz'))
        for i in range(filas):
            m.append([])
            for j in range(columnas):
                valor = complex(input("fila {}, columna {}:".format(i + 1, j + 1)))
                m[i].append(valor)
        e = input("ingrese la cantidad de clicks")
        res = rendija_1(m,e)
    elif x ==3:
        r = input("ingrese cantidad de rendijas que desea")
        q = input("ingrese cantidad de clicks")
        res = rendija_2(r,q)
    print(res)
main()




