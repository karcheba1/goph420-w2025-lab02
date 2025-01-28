from src.goph420_lab02.interpolation import (
    interp_lagrange,
)
import matplotlib.pyplot as plt
import numpy as np


def main():
    # generate some data from polynomials of different order

    # test the interp_lagrange() function

    # plot the results

    xd = np.array([-5, 5])
    xd_2 = np.array([-5, 0, 5])
    xd_3 = np.array([-5, -2, 2, 5])

    x = np.linspace(-10, 10, 100)

    y_linear_data = 3 * xd + 1
    y_linear_exp = 3 * x + 1

    y_quad_data = 3 * xd_2**2 + 2 * xd_2 + 2
    y_quad_exp = 3 * x**2 + 2 * x + 2

    y_cubic_data = 3 * xd_3**3 + 2 * xd_3**2 + 2 * xd_3 + 3
    y_cubic_exp = 3 * x**3 + 2 * x**2 + 2 * x + 3

    L_linear = interp_lagrange(x, xd, y_linear_data)
    f_linear = y_linear(x)

    L_quad = interp_lagrange(x, xd_2, y_quad_data)
    f_quad = y_quad(x)

    L_cubic = interp_lagrange(x, xd_3, y_cubic_data)
    f_cubic = y_cubic(x)

    plt.plot(x, y_linear_exp, "-b", label="Linear")
    plt.plot(x, y_quad_exp, "--b", label="Quadratic")
    plt.plot(x, y_cubic_exp, "-.b", label="Cubic")

    plt.plot(x, f_linear, label="Linear Function")
    plt.plot(x, L_linear, label="Linear Interpolation")
    plt.scatter(xd, y_linear_data)

    plt.plot(x, f_quad, label="Quadratic Function")
    plt.plot(x, L_quad, label="Quadratic Interpolation")
    plt.scatter(xd_2, y_quad_data)

    plt.plot(x, f_cubic, label="Cubic Function")
    plt.plot(x, L_cubic, label="Cubic Interpolation")
    plt.plot(xd, y_cubic_data)

    plt.show()


if __name__ == "__main__":
    main()
