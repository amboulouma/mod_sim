import matplotlib.pyplot as plt
import numpy as np


class ForestDDEM:
    def __init__(self, deer_init, fox_init, t):
        self.deer_init = deer_init
        self.fox_init = fox_init
        self.t = t
        self.num_deers = []
        self.num_foxes = []

    def run_full(self, alpha, beta, gamma, delta, m):
        num_deers = [self.deer_init]
        num_foxes = [self.fox_init]
        for _ in range(1, self.t + 1):
            xt = num_deers[-1]
            yt = num_foxes[-1]

            xnext = xt + xt * alpha * (m - xt - yt) - xt * yt * beta
            ynext = yt + yt * (delta * xt - gamma)

            num_deers.append(xnext)
            num_foxes.append(ynext)

        num_deers = [np.round(i) for i in num_deers]
        num_foxes = [np.round(i) for i in num_foxes]

        self.num_foxes = num_foxes
        self.num_deers = num_deers

        return num_deers, num_foxes

    def run_time_deers(self, time, alpha, beta, gamma, delta, m):
        return np.array(self.run_full(alpha, beta, gamma, delta, m)[0])[time.astype(int)]

    def run_time_foxes(self, time, alpha, beta, gamma, delta, m):
        return np.array(self.run_full(alpha, beta, gamma, delta, m)[1])[time.astype(int)]

    def plot(self):
        plt.figure(figsize=(12, 9))
        plt.plot(list(range(len(self.num_deers))), self.num_deers)
        plt.plot(list(range(len(self.num_foxes))), self.num_foxes)
        plt.show()
