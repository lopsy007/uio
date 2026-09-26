import matplotlib.pyplot as plt
import numpy as np

my = 0.5 # dynamisk froksjonskoeffisient
v0 = 10.0 # startfart i m/s
g = 9.81 # tyngdeakselerasjonen
k = 1

a = lambda x: -k*x*g
v = [v0]
x = [0]
dt = 0.001

while v[-1] > 0:
    v.append(v[-1]+a(x[-1])*dt)
    x.append(x[-1]+v[-1]*dt)

t = np.linspace(0,(len(v)-1)*dt,len(v))
print(x[-1])

fig, (ax1, ax2, ax3) = plt.subplots(3, 1)

ax1.plot(t, [a(x) for x in x])
ax1.set_xlabel('t [s]')
ax1.set_ylabel('a [m/s^2]')

ax2.plot(t, v)
ax2.set_xlabel('t [s]')
ax2.set_ylabel('v [m/s]')

ax3.plot(t, x)
ax3.set_xlabel('t [s]')
ax3.set_ylabel('x [m]')


plt.show()
