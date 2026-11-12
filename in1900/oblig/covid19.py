from SEIR import SEIR

class SEIRimport(SEIR):
    def __init__(self, beta=0.33, r_ia=0.1,
                r_e2=1.25, lmbda_1=0.33,
                lmbda_2=0.5, p_a=0.4, mu=0.2,
                sigma=0):
        self.sigma = sigma
        super().__init__(beta, r_ia, r_e2, lmbda_1, lmbda_2, p_a, mu)

    def __call__(self, t, u):
        values = super().__call__(t, u)
        values[2] += self.sigma
        return values

def test_SEIRimport():
    sigma = 1
    model1 = SEIRimport(sigma=sigma)
    model2 = SEIR()
    tol = 1e-9

    assert all(abs(computed1-computed2)<(sigma+tol) for computed1, computed2 in zip(model1(1, [1,2,3,4,5,6]), model2(1, [1,2,3,4,5,6])))


if __name__ == "__main__":
    from SEIR import SEIR, solve_SEIR, plot_SEIR
    from lockdown import Beta
    beta = Beta('r_values.txt')
    beta.plot(600)
    model = SEIRimport(beta, sigma=10)
    t, u = solve_SEIR(model, T=600, N = 600,
                      S_0=5.5e6, E2_0=100)
    plot_SEIR(t, u, components = ['I','Ia'])
