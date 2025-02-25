import numpy as np
import matplotlib.pyplot as plt

from goph420_lab02.interpolation import (
    interp_grad_2ndorder,
    interp_lagrange,
)


#  data
T = [22.8, 22.8, 22.8, 20.6, 13.9, 11.7, 11.1, 11.1, 11.1]
z = [0, 2.3, 4.9, 9.1, 13.7, 18.3, 22.9, 26.0, 27.2]


def points():
    for i in range(T):
        n = 0
        Tpoints = np.linspace(T[n], T[n + 2], 10)
        Tlist = Tpoints.append()
        return Tlist

def points2():    
    for i in range(z):
        n = 0
        zpoints = np.linspace(z[n], z[n + 2], 10)
        zlist = zpoints.append()
    return zlist

def main():
    #  plotting T(z)
    plt.figure()
    plt.plot(T, z, "o")
    plt.xlabel("z")
    plt.ylabel("T(z)")
    plt.legend()
    plt.show()

    plt.figure()
    plt.xlabel("z")
    plt.ylabel("T(z)")
    plt.legend()
    plt.show()

def integral_gauss():
    #  integrate T(z) using Gaussian quadrature
    #  using 3 points
    n = 3 
    x, y = np.polynomial.legendre.leggauss(n)
    nodes = x
    weights = y 











if __name__ == "__main__":
    main()

