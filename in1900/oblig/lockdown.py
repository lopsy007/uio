from datetime import date, timedelta
import numpy as np
import matplotlib.pyplot as plt

class Beta:
    def __init__(self, filename):

        #formatting & processing
        with open(filename) as file:
            lines = file.readlines()[2:]
        lines = [line.strip().split(' ') for line in lines]
        lines = [[string for string in line if string] for line in lines]
        start_dates = list(zip(*lines))[0]
        start_dates = [Beta.str2date(date) for date in start_dates]

        self.start_dates = [(date-start_dates[0]).days for date in start_dates]
        self.betas = list(zip(*lines))[2]

    def __call__(self, t):
        #find last beta with start interval <=t
        for time, beta in zip(self.start_dates, self.betas):
            if time>t: break
        return beta

    def plot(self, T):
        t = np.linspace(0, T, 1001)
        betas = []
        for time in t:
            betas.append(self.__call__(time))
        plt.plot(t, betas)

    def str2date(date_str):
        day, month, year = (int(n) for n in date_str.split('.'))
        return date(year, month, day)

def test_Beta():
    instance = Beta("r_values.txt")
    instance(1)
    instance(1)
    print(instance.start_dates)


if __name__ == "__main__":
    from SEIR import SEIR, solve_SEIR, plot_SEIR
    test_Beta()
    beta = Beta('r_values.txt')
    beta.plot(600)
    model = SEIR(beta)
    t, u = solve_SEIR(model, T=600, N = 600,
                      S_0=5.5e6, E2_0=100)
    plot_SEIR(t, u, components = ['I','Ia'])
