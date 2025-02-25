import matplotlib.pyplot as plt
import numpy as np


def main():
    z = np.linspace(0, 10, 9)
    T = z**2

    plt.figure()
    plt.plot(T, z, "or")
    plt.ylim(bottom=z[-1], top=z[0])

    zplot = []
    Tplot = []
    for k, Tk in enumerate(T[:-1:2]):
        Tloc = T[2 * k : 2 * k + 3]
        zloc = z[2 * k : 2 * k + 3]

        zp = np.linspace(zloc[0], zloc[-1])
        Tslp = (Tloc[-1] - Tloc[0]) / (zloc[-1] - zloc[0])
        Tp = []
        for zk in zp:
            Tp.append(Tloc[0] + Tslp * (zk - zloc[0]))
        zplot.append(zp)
        Tplot.append(Tp)

        print(zloc)
        print(Tloc)
        zavg = np.sum(zloc) / 3
        Tavg = np.sum(Tloc) / 3
        plt.plot(Tavg, zavg, "xb")

    zplot = np.array(zplot).flatten()
    Tplot = np.array(Tplot).flatten()
    plt.plot(Tplot, zplot, "--b", label="interp")

    plt.show()


if __name__ == "__main__":
    main()
