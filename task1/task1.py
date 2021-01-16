import matplotlib.pyplot as plt


x0 = 4000
y0 = 1000
alpha = 1e-5
beta = 2e-5
gamma = 5e-9
delta = 5e-6
M = 20000
T = 120

def run():
    x, y = damped(x0, y0, alpha, beta, gamma, delta, M, T)
    print("Number of deers at the end: ", x[-1])
    print("Number of foxes at the end: ", y[-1])

    plt.figure(figsize = (12,9))
    plt.plot(list(range(T)), x)
    plt.plot(list(range(T)), y)
    plt.show()


def add_next_damped(x, y, alpha, beta, gamma, delta, M):
    xt = x[-1]
    yt = y[-1]
    xnext = xt + xt * alpha * (M - xt - yt) - xt * yt * beta
    ynext = yt + yt * (delta * xt - gamma)
    x.append(xnext)
    y.append(ynext)
    return x, y
        
def damped(x0, y0, alpha, beta, gamma, delta, M, T):
    x = [x0]
    y = [y0]
    for t in range(1, T):
        x, y = add_next_damped(x, y, alpha, beta, gamma, delta, M);
    x = [int(u) for u in x]
    y = [int(v) for v in y]
    return x, y


run()
