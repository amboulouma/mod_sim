import matplotlib.pyplot as plt
import numpy as np

from scipy.optimize import curve_fit


class ForestDDEM:
    def __init__(self, deer_init, fox_init, t):
        self.deer_init = deer_init
        self.fox_init = fox_init
        self.t = t

        self.alpha = None
        self.beta = None
        self.gamma = None
        self.delta = None
        self.m = None
        self.num_deers = []
        self.num_foxes = []

    def run_full(self, alpha=None, beta=None, gamma=None, delta=None, m=None):
        if alpha is None:
            alpha = self.alpha
        if beta is None:
            beta = self.beta
        if gamma is None:
            gamma = self.gamma
        if delta is None:
            delta = self.delta
        if m is None:
            m = self.m
        num_deers = [self.deer_init]
        num_foxes = [self.fox_init]
        for _ in range(1, self.t + 1):
            xt = num_deers[-1]
            yt = num_foxes[-1]
            try:
                xnext = xt + xt * alpha * (m - xt - yt) - xt * yt * beta
                ynext = yt + yt * (delta * xt - gamma)

                num_deers.append(xnext)
                num_foxes.append(ynext)

            except TypeError:
                print("Either provide parameters or train object first!")
                return [], []

        num_deers = [int(np.round(i)) for i in num_deers]
        num_foxes = [int(np.round(i)) for i in num_foxes]

        self.num_foxes = num_foxes
        self.num_deers = num_deers

        return num_deers, num_foxes

    def run_time_deers(self, time, alpha, beta, gamma, delta, m):
        return np.array(self.run_full(alpha, beta, gamma, delta, m)[0])[np.round(time).astype(int)]

    def run_time_foxes(self, time, alpha, beta, gamma, delta, m):
        return np.array(self.run_full(alpha, beta, gamma, delta, m)[1])[np.round(time).astype(int)]

    def fit_to_foxes(self, foxes, bounds):
        fit = curve_fit(self.run_time_foxes, [i for i in range(self.t + 1)], foxes, bounds=bounds)
        self.alpha, self.beta, self.gamma, self.delta, self.m = fit[0]
        print("\nFit to foxes:")
        print(f"alpha: {self.alpha}")
        print(f"beta: {self.beta}")
        print(f"gamma: {self.gamma}")
        print(f"delta: {self.delta}")
        print(f"M: {self.m}")

    def fit_to_deers(self, deers, bounds):
        fit = curve_fit(self.run_time_deers, [i for i in range(self.t + 1)], deers, bounds=bounds)
        self.alpha, self.beta, self.gamma, self.delta, self.m = fit[0]
        print("\nFit to deers:")
        print(f"alpha: {self.alpha}")
        print(f"beta: {self.beta}")
        print(f"gamma: {self.gamma}")
        print(f"delta: {self.delta}")
        print(f"M: {self.m}")

    def plot(self, title="DDEM Plot", new_window=True):
        if new_window:
            plt.figure(figsize=(12, 9))
        plt.plot(list(range(len(self.num_deers))), self.num_deers)
        plt.plot(list(range(len(self.num_foxes))), self.num_foxes)
        plt.title(title)
        if new_window:
            plt.legend(["Deers", "Foxes"])
        else:
            plt.legend(["Deers CA", "Foxes CA", "Deers DE", "Foxes DE"])
        plt.show()
