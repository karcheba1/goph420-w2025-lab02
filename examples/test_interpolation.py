<<<<<<< HEAD
from goph420_lab02.interpolation import (
=======
from src.goph420_lab02.interpolation import (
>>>>>>> ad7192a3dce4badce4f4505eb8e83c41c8ac9040
    interp_lagrange, 
    interp_grad_2ndorder,
)
import matplotlib.pyplot as plt
import numpy as np

T = [22.8, 22.8, 22.8, 20.6, 13.9, 11.7, 11.1, 11.1, 11.1]
z = [0, 2.3, 4.9, 9.1, 13.7, 18.3, 22.9, 26.0, 27.2]


def main():
    # generate some data from polynomials of different order

    # test the interp_lagrange() function

    # plot the results


    xd = np.array([-5,5])
    xd_2 = np.array([-5,0,5])
    xd_3 = np.array([-5,-2,2,5])

    x = np.linspace(-10, 10, 100)

    y_linear_data = 3 * xd + 1
    y_linear_exp = 3 * x + 1

    y_quad_data = 3 * xd_2**2 + 2 * xd_2 + 2
    y_quad_exp = 3 * x**2 + 2 * x + 2

    y_cubic_data = 3 * xd_3**3 + 2 * xd_3**2 + 2 * xd_3 + 3
    y_cubic_exp = 3 * x**3 + 2 * x**2 + 2 * x + 3

    L_linear = interp_lagrange(x, xd, y_linear_data)
<<<<<<< HEAD
    f_linear = y_linear[x]
=======

>>>>>>> ad7192a3dce4badce4f4505eb8e83c41c8ac9040

    L_quad = interp_lagrange(x, xd_2, y_quad_data)


    L_cubic = interp_lagrange(x ,xd_3, y_cubic_data)


    plt.plot(x, y_linear_exp, "-b", label="Linear")
    plt.plot(x, y_quad_exp, "--b", label="Quadratic")
    plt.plot(x, y_cubic_exp, "-.b", label="Cubic")

    plt.plot(x, f_linear_exp, label="Linear Function")
    plt.plot(x, L_linear_exp, label="Linear Interpolation")
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


def test_2nd_order_grad(x, wd, fd): 
    """Test the 2nd order gradient function""" 
    x = 3.0 
    xd = [0, 2.3, 4.9] 
    fd = [22.8, 22.8, 22.8] 
    grad = interp_grad_2ndorder(x, xd, fd) 
    assert grad == 0.0, "Gradient is not correct"