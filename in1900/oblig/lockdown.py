from cmath import inf
from datetime import date, timedelta
import numpy as np
import matplotlib.pyplot as plt
from outbreak import R_to_beta

class Beta:
    def __init__(self, filename):

        #formatting & processing
        with open(filename) as file:
            lines = file.readlines()[2:]
        lines = [line.strip().split(' ') for line in lines]
        lines = [[string for string in line if string] for line in lines]

        start_dates = list(zip(*lines))[0]
        start_dates = [Beta.str2date(date) for date in start_dates]
        start_dates = [(date-start_dates[0]).days for date in start_dates]
        if list(zip(*lines))[1][-1] == '-':
            self.start_dates = start_dates + [-1]

        r_values = list(map(float, list(zip(*lines))[2]))
        self.betas = [R_to_beta(r) for r in r_values]

    def __call__(self, t):
        #find last beta with start interval <=t
        for time, beta in zip(self.start_dates[1:], self.betas):
            if t<time: break
            if time==-1: break
        return beta

    def plot(self, T):
        t = np.linspace(0, T, 1000)
        betas = []
        for time in t:
            betas.append(self.__call__(time))
        plt.plot(t, betas)
        plt.show()

    @staticmethod
    def str2date(date_str):
        day, month, year = (int(n) for n in date_str.split('.'))
        return date(year, month, day)

def test_Beta():
    instance = Beta("r_values.txt")
    tol = 1e-9
    assert abs(instance(28)-R_to_beta(3.2))<tol
    assert abs(instance(29)-R_to_beta(0.5))<tol


if __name__ == "__main__":
    from SEIR import SEIR, solve_SEIR, plot_SEIR
    test_Beta()
    beta = Beta('r_values.txt')
    beta.plot(600)
    model = SEIR(beta)
    t, u = solve_SEIR(model, T=600, N = 600,
                      S_0=5.5e6, E2_0=100)
    plot_SEIR(t, u, components = ['I','Ia'])

# Vi forventer større bølger enn vi får, så modellen mangler nok en eller flere forsterkende faktorer.
# Et mulig eksempel er innreisende smittebærere.
