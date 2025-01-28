from goph420_lab02.interpolation import (
    interp_lagrange,
)
import matplotlib.pyplot as plt


def main():
    # generate some data from polynomials of different order

    # test the interp_lagrange() function

    # plot the results
    import numpy as np

    xd = np.linspace(-10, 10)
    x_plot = np.linspace(-10, 10, 100)

    y_linear = 3 * xd + 1
    y_quad = 3 * xd ** 2 + 2 * xd + 2
    y_cubic = 3 * xd ** 3 + 2 * xd ^ 2 + 2 * xd + 3

    L_linear = interp_lagrange(xd, y_linear)
    f_linear = y_linear(x_plot)

    L_quad = interp_lagrange(xd, y_quad)
    f_quad = y_quad(x_plot)

    L_cubic = interp_lagrange(xd, y_cubic)
    f_cubic = y_cubic(x_plot)

    plt.plot(x_plot, y_linear, label="Linear")
    plt.plot(x_plot, y_quad, label="Quadratic")
    plt.plot(x_plot, y_cubic, label="Cubic")
    plt.show()

    pass


if __name__ == "__main__":
    main()
