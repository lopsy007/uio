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
tN1 = [[],[]]
tN2 = []
t_min = 0
t_maks = 48
n = 12
dt = t_maks/n

for i in range(n+1):
    t = t_min+i*dt
    tN1[0].append(t)
    tN1[1].append(int(N_(t)))

    tN2.append([t, int(N_(t))])


[print(f'|{int(tN1[0][i]):<10}|{int(tN1[1][i]):>10}|') for i in range(len(tN1[0]))]
print()
[print(f'|{int(tN2[i][0]):<10}|{int(tN2[i][1]):>10}|') for i in range(len(tN1[0]))]
