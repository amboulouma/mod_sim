import numpy as np

from ForestCA import ForestCA

if __name__ == "__main__":
    np.random.seed(1)

    forest_ca = ForestCA(height=100, width=100,
                         fox_init=1000, deer_init=4000,
                         k=1, p1=0.2, p2=0.5, p3=0.1,
                         num_runs=50, fps=4)

    forest_ca.run(visualization=True)

    forest_ca.plot()
