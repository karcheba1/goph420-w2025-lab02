import numpy as np
import matplotlib.pyplot as plt

from goph420_lab02.interpolation import (
    interp_grad_2ndorder,
)


#  data
T = [22.8, 22.8, 22.8, 20.6, 13.9, 11.7, 11.1, 11.1, 11.1]
z = [0, 2.3, 4.9, 9.1, 13.7, 18.3, 22.9, 26.0, 27.2]

x = 1
dtdz = interp_grad_2ndorder(x, z, T)


def main():
    #  plotting T(z)
    plt.figure()
    plt.plot(T, z, "--g")
    plt.xlabel("z")
    plt.ylabel("T(z)")
    plt.legend()
    plt.show()

    plt.figure()
    plt.plot(dtdz, z, "--g")
    plt.xlabel("z")
    plt.ylabel("T(z)")
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()

