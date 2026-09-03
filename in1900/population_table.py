import sympy

# N(t) = B / (1 + C * e^(-kt))
# der B = 50000, k = 0.2h^(-1), N(0)=5000

# Finner C:
B = 50000
k = 0.2
t = 0

C = sympy.Symbol('C')
C = sympy.solve( sympy.Eq(5000, B / (1 + C * sympy.E**(-k*t))), C )[0]

# Definerer N(t):
def N_(t):
    return B / (1 + C * float(sympy.E)**(-0.2*t))

# Beregner verdiene:
t = []
N = []
t_min = 0
t_maks = 48
n = 12
dt = t_maks/n

for i in range(n+1):
    t_ = t_min+i*dt
    t.append(t_)
    N.append(int(N_(t_)))

[print(f'[{t[i]:<10}][{N[i]:>10}]') for i in range(len(t))]
