import numpy as np
import matplotlib.pyplot as plt

from goph420_lab02.interpolation import (
    interp_lagrange,
)


def main():
    # x plotting points
    xp = np.linspace(-1.0, 1.0)
    xt = np.linspace(-1.0, 1.0, 5)

    # first order, expected
    L_01 = -0.5 * (xp - 1.0)
    L_11 = 0.5 * (xp + 1.0)

    # first order, actual
    # f_01 = interp_lagrange(xt, [-1.0, 1.0], [1.0, 0.0])
    # f_11 = interp_lagrange(xt, [-1.0, 1.0], [0.0, 1.0])

    # second order, expected
    L_02 = 0.5 * xp * (xp - 1.0)
    L_12 = -(xp + 1.0) * (xp - 1.0)
    L_22 = 0.5 * xp * (xp + 1.0)

    # second order, actual
    # f_02 = interp_lagrange(xt, [-1.0, 0.0, 1.0], [1.0, 0.0, 0.0])
    # f_12 = interp_lagrange(xt, [-1.0, 0.0, 1.0], [0.0, 1.0, 0.0])
    # f_22 = interp_lagrange(xt, [-1.0, 0.0, 1.0], [0.0, 0.0, 1.0])

    # plot output
    plt.figure()
    plt.plot(xp, L_01, "-r", label="n=1, k=0")
    plt.plot(xp, L_11, "--r", label="n=1, k=1")
    plt.plot(xp, L_02, "--g", label="n=2, k=0")
    plt.plot(xp, L_12, "-g", label="n=2, k=1")
    plt.plot(xp, L_22, "-.g", label="n=2, k=2")
    # plt.plot(xt, f_01, "ok", label="interp_lagrange()")
    # plt.plot(xt, f_11, "ok")
    # plt.plot(xt, f_02, "ok")
    # plt.plot(xt, f_12, "ok")
    # plt.plot(xt, f_22, "ok")
    plt.xlabel("s")
    plt.ylabel("L_{kn}")
    plt.legend()
    plt.title("Standard Lagrange Interpolating Polynomials")
    plt.savefig("figures/standard_lagrange.png")


if __name__ == "__main__":
    main()
