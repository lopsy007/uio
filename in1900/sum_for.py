s = 0
M = 3

for k in range(1, M+1): # feil intervall: range(n) -> [0, n-1) OG feil løkke-variabel: i -> k
	s += 1/(2*k)**2     # manglende parantes (feil regnerekkefølge)

print(s)