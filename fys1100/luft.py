import matplotlib.pyplot as plt

g = 9.81
k = 0.04
m = 1.0

tmax = 10.0
dt = 0.01
n = int(tmax/dt)

x = [0.0]
a = []
v = [0.0]
t = [0.0]

for i in range(n-1):
    a.append( g-k/m*v[i]**2 )
    v.append( v[i]+a[i]*dt )
    x.append( x[i]+v[i+1]*dt ) #euler cromers metode
    t.append( t[i] + dt )

a.append( g-k/m*v[n-1]**2 )


plt.plot(t, a)
plt.show()

plt.plot(t, v)
plt.show()

plt.plot(t, x)
plt.show()
