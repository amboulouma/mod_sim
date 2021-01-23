import numpy as np
import matplotlib.pyplot as plt

from scipy.optimize import curve_fit
from ForestDDEM import ForestDDEM
from ForestCA import ForestCA

if __name__ == "__main__":
    np.random.seed(2)
    forest_ca = ForestCA(height=100, width=100,
                         fox_init=1000, deer_init=4000,
                         k=1, p1=0.2, p2=0.5, p3=5e-9,
                         num_runs=20, fps=2)
    deers_ca, foxes_ca = forest_ca.run(False)

    bounds = ((0, 0, 0, 0, 10000),
              (10 ** -7, 10 ** -4, 10 ** -6, 10 ** -4, 10 ** 6)
              )

    forest_ddem = ForestDDEM(deer_init=4000, fox_init=1000, t=20)

    fit = curve_fit(forest_ddem.run_time_foxes, [i for i in range(0, 21)], foxes_ca, bounds=bounds)

    alpha_fit, beta_fit, gamma_fit, delta_fit, M_fit = fit[0]

    x, y = forest_ddem.run_full(alpha_fit, beta_fit, gamma_fit, delta_fit, M_fit)

    forest_ca.plot()

    plt.figure(figsize=(12, 9))
    plt.plot(list(range(21)), y)
    plt.plot(list(range(21)), x)

    plt.legend(["foxes", "deers"])
