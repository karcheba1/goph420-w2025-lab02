from src.goph420_lab02.interpolation import (
    interp_lagrange,
)
import matplotlib.pyplot as plt
import numpy as np


def main():
    # generate some data from polynomials of different order

    # test the interp_lagrange() function

    # plot the results


    xd = np.array([-5,5])
    xd_2 = np.array([-5,0,5])
    xd_3 = np.array([-5,-2,2,5])

    x = np.linspace(-10, 10, 100)

    y_linear = 3 * xd + 1
    y_quad = 3 * xd_2 ** 2 + 2 * xd_2 + 2
    y_cubic = 3 * xd_3 ** 3 + 2 * xd_3 ** 2 + 2 * xd_3 + 3

    L_linear = interp_lagrange(x, xd, y_linear)
    f_linear = y_linear(x)

    L_quad = interp_lagrange(x, xd_2, y_quad)
    f_quad = y_quad(x)

    L_cubic = interp_lagrange(x ,xd_3, y_cubic)
    f_cubic = y_cubic(x)

    plt.plot( x, f_linear, label="Linear Function")
    plt.plot(x, L_linear, label="Linear Interpolation")
    plt.scatter(xd, y_linear)

    plt.plot(x, f_quad, label="Quadratic Function")
    plt.plot(x, L_quad, label="Quadratic Interpolation")
    plt.scatter(xd_2, y_quad)

    plt.plot(x, f_cubic, label="Cubic Function")
    plt.plot(x, L_cubic, label="Cubic Interpolation")
    plt.plot(xd, y_cubic)
    plt.show()

    pass


if __name__ == "__main__":
    main()
