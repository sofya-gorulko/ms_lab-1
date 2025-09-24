import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm, gamma
import matplotlib
matplotlib.use("TkAgg")

n = 50
Nsim = 100000

X = norm.rvs(size=(Nsim, n))

X_sorted = np.sort(X, axis=1)
X2 = X_sorted[:, 1]

U = norm.cdf(X2)

Y = n * U

plt.hist(Y, bins=100, density=True, alpha=0.6, color='skyblue', label='Эмпирика (Normal)')
x_vals = np.linspace(0, np.max(Y), 500)
plt.plot(x_vals, gamma.pdf(x_vals, a=2, scale=1), 'r-', lw=2, label='Gamma(2,1)')

plt.xlabel("y")
plt.ylabel("Плотность")
plt.title(f"nF(X(2)), n={n}, X~Normal(0,1)")
plt.legend()
plt.show()
