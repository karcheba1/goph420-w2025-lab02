import numpy as np
import matplotlib.pyplot as plt

from goph420_lab02.interpolation import (
    interp_grad_2ndorder,
    interp_lagrange,
)


#  data
T = [22.8, 22.8, 22.8, 20.6, 13.9, 11.7, 11.1, 11.1, 11.1]
z = [0, 2.3, 4.9, 9.1, 13.7, 18.3, 22.9, 26.0, 27.2]


def nd_ord():
    zplot = []
    Tplot = []
    for k, Tk in enumerate(T[:-1:2]):
        Tloc = T

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
    #  using 2 points
    n = 2 
    x, y = np.polynomial.legendre.leggauss(n)
    nodes = x
    weights = y 
    # scaling the x points from a [-1, 1] interval to the actual interval for the integral.
    scaled_nodes = 0.5*(nodes + 1)*(Z[-1] - Z[0]) + Z[0]
    #calculating the integral value using the gauss-legendre quadrature formula.
    integral_value = np.sum(weights * (interp_grad_2ndorder(scaled_nodes)**2)) * (0.5 * (Z[-1] - Z[0]))












if __name__ == "__main__":
    main()

