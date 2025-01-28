from goph420_lab02.interpolation import (
    interp_lagrange,
)
import matplotlib.pyplot as plt


def main():
    # generate some data from polynomials of different order

    # test the interp_lagrange() function

    # plot the results
    import numpy as np

    xd = [-5,5]
    xd_2 = [-5,0,5]
    xd_3 = [-5,-2,2,5]

    x = np.linspace(-10, 10, 100)

    y_linear = 3 * xd + 1
    y_quad = 3 * xd_2 ** 2 + 2 * xd_2 + 2
    y_cubic = 3 * xd_3 ** 3 + 2 * xd_3 ^ 2 + 2 * xd_3 + 3

    L_linear = interp_lagrange(x, xd, y_linear)
    f_linear = y_linear(x)

    L_quad = interp_lagrange(x, xd_2, y_quad)
    f_quad = y_quad(x)

    L_cubic = interp_lagrange(x ,xd_3, y_cubic)
    f_cubic = y_cubic(x)

    plt.plot(x, y_linear, label="Linear")
    plt.plot(x, y_quad, label="Quadratic")
    plt.plot(x, y_cubic, label="Cubic")
    plt.show()

    pass


if __name__ == "__main__":
    main()
