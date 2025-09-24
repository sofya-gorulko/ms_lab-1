import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm, gamma
import matplotlib
matplotlib.use("TkAgg")

n = 50
Nsim = 100000

X = norm.rvs(size=(Nsim, n))

X_sorted = np.sort(X, axis=1)

U1 = n * norm.cdf(X_sorted[:, 1])
U2 = n * (1 - norm.cdf(X_sorted[:, -3]))

mean = np.mean(X_sorted, axis=1)
var = np.var(X_sorted, axis=1)
median = np.quantile(X_sorted, 0.5, axis=1)

plt.hist(U1, bins=100, density=True, alpha=0.6, color='skyblue', label='Эмпирика (Normal)')
x_vals = np.linspace(0, np.max(U1), 500)
plt.plot(x_vals, gamma.pdf(x_vals, a=2, scale=1), 'r-', lw=2, label='Gamma(2,1)')

plt.xlabel("y")
plt.ylabel("Плотность")
plt.title(f"nF(X(2)), n={n}, X~Normal(0,1)")
plt.legend()
plt.show()
