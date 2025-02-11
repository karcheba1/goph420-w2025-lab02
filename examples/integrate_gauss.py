# determine sample points and weights for integration over [-1, 1]
xi_star, ci_star = np.polynomial.legendre.leggauss(npts)
a, b = lims

# shifts then scales sample points from [-1, 1] to [a, b], eq (9)
xi = ((b + a) / 2) + (((b - a) / 2) * xi_star)

# only scales weights from [-1, 1] to [a, b], eq (10)
ci = ((b - a) / 2) * ci_star

# approx integral
integral = 0
for i in range(npts):
    integral += ci[i] * f(xi[i])
return integral