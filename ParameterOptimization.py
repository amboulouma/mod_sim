import numpy as np

from ForestDDEM import ForestDDEM
from ForestCA import ForestCA

if __name__ == "__main__":
    np.random.seed(2)
    forest_ca = ForestCA(height=100, width=100,
                         fox_init=1000, deer_init=4000,
                         k=1, p1=0.2, p2=0.5, p3=5e-9,
                         num_runs=20, fps=2)
    deers_ca, foxes_ca = forest_ca.run(False)

    bounds = ((0, 0, 0, 0, 5000),
              (10 ** -7, 10 ** -4, 10 ** -6, 10 ** -4, 10 ** 6)
              )

    forest_ddem = ForestDDEM(deer_init=4000, fox_init=1000, t=20)

    forest_ddem.fit_to_foxes(foxes_ca, bounds)

    forest_ddem.run_full()

    forest_ca.plot()
    forest_ddem.plot()
