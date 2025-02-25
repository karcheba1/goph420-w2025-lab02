import numpy as np
import matplotlib.pyplot as plt

from goph420_lab02.interpolation import (
    interp_grad_2ndorder,
    interp_lagrange,
)


#  data
T = [22.8, 22.8, 22.8, 20.6, 13.9, 11.7, 11.1, 11.1, 11.1]
z = [0, 2.3, 4.9, 9.1, 13.7, 18.3, 22.9, 26.0, 27.2]


def points(T):
    Tlist =  []
    for T,z in enumerate(T):
        Tpoints = np.linspace([z][T], z[T + 2], 10)
        Tlist.append(Tpoints)
    return Tlist

def main():
    #  plotting T(z)
    plt.figure()
    plt.plot(T, z, "o")
    plt.xlabel("z")
    plt.ylabel("T(z)")
    plt.legend()
    plt.ylim(z[-1], z[0])
    plt.show()

    plt.figure()
    plt.xlabel("z")
    plt.ylabel("T(z)")
    plt.legend()
    plt.show()


if __name__ == "__main__":
    main()

