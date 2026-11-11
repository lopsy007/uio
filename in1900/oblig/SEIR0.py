import ODESolver
import matplotlib.pyplot as plt

class SEIR0:
    def __init__(self, beta=0.33, r_ia=0.1,
                 r_e2=1.25, lmbda_1=0.33,
                 lmbda_2=0.5, p_a=0.4, mu=0.2):

        self.beta = beta
        self.r_ia = r_ia
        self.r_e2 = r_e2
        self.lmbda_1 = lmbda_1
        self.lmbda_2 = lmbda_2
        self.p_a = p_a
        self.mu = mu

    def __call__(self, t, u):
        beta = self.beta
        r_ia = self.r_ia
        r_e2 = self.r_e2
        lmbda_1 = self.lmbda_1
        lmbda_2 = self.lmbda_2
        p_a = self.p_a
        mu = self.mu

        S, E1, E2, I, Ia, R = u
        N = sum(u)
        dS = -beta * S * I / N - r_ia * beta * S * Ia / N \
            - r_e2 * beta * S * E2 / N
        dE1 = beta * S * I / N + r_ia * beta * S * Ia / N \
            + r_e2 * beta * S * E2 / N - lmbda_1 * E1
        dE2 = lmbda_1 * (1 - p_a) * E1 - lmbda_2 * E2
        dI = lmbda_2 * E2 - mu * I
        dIa = lmbda_1 * p_a * E1 - mu * Ia
        dR = mu * (I + Ia)
        return [dS, dE1, dE2, dI, dIa, dR]


def test_SEIR0():
    model = SEIR0()
    expected = [-0.12964285714285714, -0.5303571428571429, -1.104, 0.7, -0.736, 1.8]
    computed = model(0, [1,2,3,4,5,6])
    tol = 1e-10
    assert all(abs(exp-comp)<tol for exp,comp in zip(expected, computed))

def solve_SEIR(model: SEIR0, T, N, S_0, E2_0):
    solver = ODESolver.RungeKutta4(model)
    solver.set_initial_condition([S_0, 0, E2_0, 0, 0, 0])
    return solver.solve([0, T], N)

def test_solve_SEIR():
    t, u = solve_SEIR(SEIR0(), 10, 100, 10, 10)
    tol = 1e-10
    assert all(abs(sum(u_i)-sum(u[0]))<tol for u_i in u)

def plot_SEIR(t,u):
    u = list(zip(*u))
    plt.plot(t, u[0], label="S")
    plt.plot(t, u[3], label="I")
    plt.plot(t, u[4], label="Ia")
    plt.plot(t, u[5], label="R")
    plt.legend()
    plt.xlabel("Time (days)")
    plt.ylabel("Number in each category")
    plt.show()


if __name__ == "__main__":
    test_SEIR0()
    test_solve_SEIR()
    model = SEIR0(0.4)
    solution = solve_SEIR(model, 200, 400, 5.5e6, 100)
    plot_SEIR(*solution)