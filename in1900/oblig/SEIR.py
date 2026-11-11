from SEIR0 import SEIR0, solve_SEIR
import matplotlib.pyplot as plt

class SEIR(SEIR0):

    def __init__(self, beta=0.33, r_ia=0.1,
                 r_e2=1.25, lmbda_1=0.33,
                 lmbda_2=0.5, p_a=0.4, mu=0.2):

        if isinstance(beta, (float, int)): # is it a number?
            self.beta_function = lambda t: beta     # wrap as function
        elif callable(beta):
            self.beta_function = beta
        else:
            raise TypeError("beta must be float, int or callable")

        super().__init__(self.beta_function(0), r_ia, r_e2, lmbda_1, lmbda_2, p_a, mu)

    def __call__(self, t, u):
        self.beta = self.beta_function(t)
        return super().__call__(t, u)


def test_SEIR_beta_const():
    model = SEIR()
    expected = [-0.12964285714285714, -0.5303571428571429, -1.104, 0.7, -0.736, 1.8]
    computed = model(0, [1,2,3,4,5,6])
    tol = 1e-10
    assert all(abs(exp-comp)<tol for exp,comp in zip(expected, computed))
    
def test_SEIR_beta_var():
    beta = lambda t: 0.33-0.0033*t
    model = SEIR(beta)
    expected1 = [-0.12964285714285714, -0.5303571428571429, -1.104, 0.7, -0.736, 1.8]
    expected2 = [-0.0, -0.66, -1.104, 0.7, -0.736, 1.8]
    computed1 = model(0, [1,2,3,4,5,6])
    computed2 = model(100, [1,2,3,4,5,6])
    tol = 1e-10
    assert all(abs(exp-comp)<tol for exp,comp in zip(expected1, computed1))
    assert all(abs(exp-comp)<tol for exp,comp in zip(expected2, computed2))

def plot_SEIR(t, u, components=['S', 'I', 'Ia', 'R']):
    u_components = ['S', 'E1', 'E2', 'I', 'Ia', 'R']
    u = list(zip(*u))
    for component in components:
        plt.plot(t, u[u_components.index(component)], label=component)
    plt.legend()
    plt.xlabel("Time (days)")
    plt.ylabel("Number in each category")
    plt.show()

if __name__=="__main__":
    test_SEIR_beta_const()
    test_SEIR_beta_var()

    model = SEIR(beta = 0.4)
    t, u = solve_SEIR(model, T = 200, N = 400,
                      S_0 = 5.5e6, E2_0 = 100)
    plot_SEIR(t,u)
    
    maks = max(list(zip(*u))[3])
    print(maks) # 258543
    hospital = 0.2*maks
    print(hospital) # 51709
    ventilator = 0.25*hospital
    print(ventilator) # 12927

    
    # 12927 er myyyye høyere enn 700!!

    