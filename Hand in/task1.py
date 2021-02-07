from ForestDDEM import ForestDDEM

if __name__ == '__main__':

    forest_ddem = ForestDDEM(deer_init=4000, fox_init=1000, t=120)

    forest_ddem.run_full(alpha=1e-5, beta=2e-5, gamma=5e-9, delta=5e-6, m=20000)

    forest_ddem.plot()
