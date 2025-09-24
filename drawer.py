from math import sqrt

import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm

Step = 500


def draw_curve(f, left, right, label):
    x_vals = np.linspace(left, right, Step)
    y_vals = f(x_vals)
    plt.plot(x_vals, y_vals, 'r-', lw=2, label=label)


def draw_hist(values, label, title):
    plt.hist(values, bins=100, density=True, alpha=0.6, color='skyblue', label=label)
    plt.title(title)


def draw_hist_and_ndf(X, mu, sigma, label, title):
    draw_hist(X, label, title)
    draw_curve(lambda x: norm.pdf(x, loc=mu, scale=sigma), np.min(X), np.max(X),
               "~ N({:.2f}, {:.2f})".format(mu, sigma))
    plt.legend()
    plt.show()


def draw_hist_and_df(X, f, f_description, label, title):
    draw_hist(X, label, title)
    draw_curve(f, np.min(X), np.max(X), f_description)
    plt.legend()
    plt.show()
