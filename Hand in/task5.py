import numpy as np

from ForestCA import ForestCA
from ForestDDEM import ForestDDEM

if __name__ == '__main__':
    np.random.seed(1)

    forest_ca = ForestCA(height=100, width=100,
                         deer_init=4000, fox_init=1000,
                         k=1, p1=0.2, p2=0.5, p3=5e-9, num_runs=20)

    forest_ca.run(visualization=False)

    forest_ca.plot()

    foxes = forest_ca.num_foxes
    deers = forest_ca.num_deers

    forest_ddem = ForestDDEM(4000, 1000, 20)


    # Fit to deers
    bounds = ((0, 0, 0, 0, 5000), (5 * 10 ** -7, 10 ** -4, 10 ** -6, 10 ** -4, 10 ** 6))

    forest_ddem.fit_to_deers(deers=deers, bounds=bounds)

    forest_ca.plot(show_plot=False)
    forest_ddem.plot(title="DDEM fitted to deers", new_window=False)

    
    # Fit to foxes
    bounds = ((0, 0, 0, 0, 5000), (10 ** -7, 10 ** -4, 10 ** -6, 10 ** -4, 10 ** 6))
    
    forest_ddem.fit_to_foxes(foxes=foxes, bounds=bounds)

    forest_ca.plot(show_plot=False)
    forest_ddem.plot(title="DDEM fitted to foxes", new_window=False)
    



    alpha_fit, beta_fit, gamma_fit, delta_fit, M_fit = (
         1.814528560849192e-07,
         4.976322139740308e-05,
         5e-07,
         3.6060415775325e-05,
         502500.0)


    forest_ddem.run_full(alpha=alpha_fit, beta=beta_fit, gamma=gamma_fit, delta=delta_fit, m=M_fit)

    forest_ca.plot(show_plot=False)
    forest_ddem.plot(title="DDEM manually tuned", new_window=False)
