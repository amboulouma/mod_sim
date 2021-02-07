import numpy as np

from ForestCA import ForestCA

if __name__ == '__main__':
    np.random.seed(1)

    h = [1, 2, 4, 5, 10, 20, 25, 50, 100]
    w = [100, 50, 25, 20, 10, 5, 4, 2, 1]

    for i, j in zip(h, w):
        forest_ca = ForestCA(height=i, width=j,
                             fox_init=10, deer_init=40,
                             k=5, p1=0.2, p2=0.5, p3=5e-9,
                             num_runs=20)

        forest_ca.run(visualization=False)

        forest_ca.plot()
