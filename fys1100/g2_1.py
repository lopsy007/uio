import graf

A = 3
v = lambda t: 1/2*A*t**2
a = lambda t: A*t
x = lambda t: 1/6*A*t**3

t = list(range(11))

graf.tegn(t, [x(t) for t in t], "x", "m")
graf.tegn(t, [v(t) for t in t], "v", "m/s")
graf.tegn(t, [a(t) for t in t], "a", "$m/s^2$")
