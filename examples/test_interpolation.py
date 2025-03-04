from goph420_lab02.interpolation import (
    interp_lagrange,
    interp_grad_2ndorder,
)
import matplotlib.pyplot as plt
import numpy as np


def main():
    # generate some data from polynomials of different order
    xd = np.array([-5.0, 5.0])
    xd_2 = np.array([-5, 0, 5], dtype=float)
    xd_3 = np.array([-5, -2, 2, 5], dtype=float)

    x = np.linspace(-5, 5, 100)

    y_linear_data = 3 * xd + 1
    y_linear_exp = 3 * x + 1

    y_quad_data = 3 * xd_2**2 + 2 * xd_2 + 2
    y_quad_exp = 3 * x**2 + 2 * x + 2

    y_cubic_data = 3 * xd_3**3 + 2 * xd_3**2 + 2 * xd_3 + 3
    y_cubic_exp = 3 * x**3 + 2 * x**2 + 2 * x + 3

    # test the interp_lagrange() function
    f_linear = interp_lagrange(x, xd, y_linear_data)
    f_quad = interp_lagrange(x, xd_2, y_quad_data)
    f_cubic = interp_lagrange(x, xd_3, y_cubic_data)

    print(f"Linear data equal: {np.allclose(f_linear, y_linear_exp)}")
    print(f"Quadratic data equal: {np.allclose(f_quad, y_quad_exp)}")
    print(f"Cubic data equal: {np.allclose(f_cubic, y_cubic_exp)}")

    # plot the results
    plt.subplot(3, 1, 1)
    plt.plot(xd, y_linear_data, "or", label="linear data")
    plt.plot(x, f_linear, "--b", label="interpolated")
    plt.plot(x[::5], y_linear_exp[::5], "xk", label="expected")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.legend()

    plt.subplot(3, 1, 2)
    plt.plot(xd_2, y_quad_data, "or", label="quadratic data")
    plt.plot(x, f_quad, "--b", label="interpolated")
    plt.plot(x[::5], y_quad_exp[::5], "xk", label="expected")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.legend()

    plt.subplot(3, 1, 3)
    plt.plot(xd_3, y_cubic_data, "or", label="cubic data")
    plt.plot(x, f_cubic, "--b", label="interpolated")
    plt.plot(x[::5], y_cubic_exp[::5], "xk", label="expected")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.legend()

    plt.show()


def test_2nd_order_grad():
    """Test the 2nd order gradient function"""
    x = 3.0
    xd = [0, 2.3, 4.9]
    fd = [22.8, 22.8, 22.8]
    grad = interp_grad_2ndorder(x, xd, fd)
    print(grad)
    assert np.abs(grad - 0) < 1e-8, "Gradient is not correct"


if __name__ == "__main__":
    main()
    # test_2nd_order_grad()

