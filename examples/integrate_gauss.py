import numpy as np
import matplotlib.pyplot as plt

from goph420_lab02.interpolation import (
    interp_grad_2ndorder,
    interp_lagrange,
)


#  data
T = [22.8, 22.8, 22.8, 20.6, 13.9, 11.7, 11.1, 11.1, 11.1]
z = [0, 2.3, 4.9, 9.1, 13.7, 18.3, 22.9, 26.0, 27.2]


def points(T):
    Tlist =  []
    for T,z in enumerate(T):
        Tpoints = np.linspace([z][T], z[T + 2], 10)
        Tlist.append(Tpoints)
    return Tlist

def main():
    #  plotting T(z)
    fig, ax = plt.subplots()
    ax.plot(T, z, "o")
    plt.ylabel("T(z)")
    plt.legend()
    plt.ylim(z[-1], z[0])
    ax.tick_params(top=True, labeltop=True, bottom=False, labelbottom=False)
    ax.set_title('z')

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

