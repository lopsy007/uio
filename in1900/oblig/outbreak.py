from SEIR import SEIR, solve_SEIR, plot_SEIR

class LockdownBeta:
    def __init__(self, t_lock, beta_0, beta_1):
        self.t_lock = t_lock
        self.beta_0 = beta_0
        self.beta_1 = beta_1

    def __call__(self, t):
        return (self.beta_0 if t<self.t_lock else self.beta_1)

def R_to_beta(R, r_ia=0.1, r_e2=1.25, lmbda_2=0.5, p_a=0.4, mu=0.2):
    return R/((1-p_a)*(r_e2/lmbda_2+1/mu)+p_a*r_ia/mu)

def test_R_to_beta():
    expected = 0.40425531914893614
    computed = R_to_beta(1.9)
    tol = 1e-10
    assert abs(expected-computed)<tol


if __name__=="__main__":
    t_locks = [19, 26, 33, 49]
    maxs = []
    for t_lock in t_locks:
        beta = LockdownBeta(t_lock, R_to_beta(3.2), R_to_beta(0.5))
        model = SEIR(beta)
        t, u = solve_SEIR(model, T = 200, N = 400,
                          S_0 = 5.5e6, E2_0 = 100)
        plot_SEIR(t,u, components=['I', 'Ia'])

        maxs.append(max(list(zip(*u))[3]))
    ventilator = [0.25*0.2*maks for maks in maxs]

    print(f"{'t_lock':<20}{'max infected':^20}{'ventilators':>20}")
    for i, t_lock in enumerate(t_locks):
        print(f"{t_lock:<20}{int(maxs[i]):^20}{int(ventilator[i]):>20}")
