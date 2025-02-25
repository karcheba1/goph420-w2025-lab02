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
    f : float or array_like
        The interpolated data. Same type and shape as x.
    """

    xd = np.asarray(xd, dtype=float)
    n = len(xd) - 1
    j = 0
    k = n

    def l_fraction(x, xd):
        """Calculate Lagrange polynomial"""
        l_frac = 1
        for j in range(len(xd)):
            if j == k:
                continue
            else:
                l_frac *= (x - xd[j]) / (xd[k] - xd[j])
        return l_frac

    def polynomial_value(x, xd, fd):
        """Determine polynomial value"""
        f = 0
        for i in range(len(xd)):
            f += fd[i]*l_fraction(x, xd)
        return f

    return polynomial_value(x, xd, fd) 



def interp_grad_2ndorder(x, xd, fd): 
    """find the gradient of the interpolating polynomial""" 
    xd = np.asarray(xd, dtype=float) 


    L0_prime = (2*x - xd[1] - xd[2]) / ((xd[0] - xd[1]) * (xd[0] - xd[2]))
    L1_prime = (2*x - xd[0] - xd[2]) / ((xd[1] - xd[0]) * (xd[1] - xd[2]))
    L2_prime = (2*x - xd[0] - xd[1]) / ((xd[2] - xd[0]) * (xd[2] - xd[1]))
    
    # Compute the derivative of the polynomial
    derivative = fd[0] * L0_prime + fd[1] * L1_prime + fd[2] * L2_prime
      
    return derivative 
