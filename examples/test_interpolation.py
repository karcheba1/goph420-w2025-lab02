from goph420_lab02.interpolation import (
    interp_lagrange,
)
import matplotlib.pyplot as plt


def main():
    # generate some data from polynomials of different order

    # test the interp_lagrange() function

    # plot the results
    import numpy as np

    xd = [-5, 5]
    xd_2 = [-5, 0, 5]
    xd_3 = [-5, -2, 2, 5]

    x = np.linspace(-10, 10, 100)

    y_linear_data = 3 * xd + 1
    y_linear_exp = 3 * x + 1

    y_quad_data = 3 * xd_2**2 + 2 * xd_2 + 2
    y_quad_exp = 3 * x**2 + 2 * x + 2

    y_cubic_data = 3 * xd_3**3 + 2 * xd_3**2 + 2 * xd_3 + 3
    y_cubic_exp = 3 * x**3 + 2 * x**2 + 2 * x + 3

    L_linear = interp_lagrange(x, xd, y_linear)
    f_linear = y_linear(x)

    L_quad = interp_lagrange(x, xd_2, y_quad)
    f_quad = y_quad(x)

    L_cubic = interp_lagrange(x, xd_3, y_cubic)
    f_cubic = y_cubic(x)

    plt.plot(x, y_linear_exp, "-b", label="Linear")
    plt.plot(x, y_quad_exp, "--b", label="Quadratic")
    plt.plot(x, y_cubic_exp, "-.b", label="Cubic")
    plt.show()

    pass


if __name__ == "__main__":
    main()
