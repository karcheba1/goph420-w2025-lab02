import numpy as np


def interp_lagrange(x, xd, fd):
    """Interpolate using Lagrange Interpolating Polynomials.

    Parameters
    ----------
    x : float or array_like
        The target point(s) for interpolation.
    xd : array_like
        The independent variable data.
    fd : array_like
        The dependent variable data.

    Returns
    -------
    float or numpy.ndarray
        The interpolated data. Same type and shape as x.
    """
    xd = np.array(xd, dtype=float)
    fd = np.array(fd, dtype=float)
    data_shape = xd.shape
    if fd.shape != data_shape:
        raise ValueError(
            f"xd has shape {data_shape}, fd has shape {fd.shape}, must be equal"
        )
    x = np.array(x, dtype=float)
    x_shape = x.shape

    xd = xd.flatten()
    fd = fd.flatten()
    x = x.flatten()

    def l_fraction(x, xd, k):
        """Calculate Lagrange weight function.

        Parameters
        ----------
        x : float
            The target point.
        xd : numpy.ndarray
            The independent variable data.
        k : int
            The index of the weight function.

        Returns
        -------
        float
            The value of the weight function.
        """
        l_frac = 1.0
        xk = xd[k]
        for j, xj in enumerate(xd):
            if j == k:
                continue
            else:
                l_frac *= (x - xj) / (xk - xj)
        return l_frac

    def polynomial_value(x, xd, fd):
        """Determine polynomial value.

        Parameters
        ----------
        x : float
            The target point.
        xd : numpy.ndarray
            The independent variable data.
        fd : numpy.ndarray
            The dependent variable data.

        Returns
        -------
        float
            The interpolated value of the function.
        """
        f = 0.0
        for j, fj in enumerate(fd):
            f += fj * l_fraction(x, xd, j)
        return f

    f = np.zeros_like(x)
    for j, xj in enumerate(x):
        f[j] = polynomial_value(xj, xd, fd)
    f = np.reshape(f, x_shape)
    if not len(x_shape):
        f = float(f)

    return f


def interp_grad_2ndorder(x, xd, fd):
    """find the gradient of the interpolating polynomial"""

    # test this

    xd = np.asarray(xd, dtype=float)

    L0_prime = (2 * x - xd[1] - xd[2]) / ((xd[0] - xd[1]) * (xd[0] - xd[2]))
    L1_prime = (2 * x - xd[0] - xd[2]) / ((xd[1] - xd[0]) * (xd[1] - xd[2]))
    L2_prime = (2 * x - xd[0] - xd[1]) / ((xd[2] - xd[0]) * (xd[2] - xd[1]))

    # Compute the derivative of the polynomial
    derivative = fd[0] * L0_prime + fd[1] * L1_prime + fd[2] * L2_prime

    return derivative
