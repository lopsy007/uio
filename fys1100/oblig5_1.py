import matplotlib.pyplot as plt
import math

dt = 0.001
m = 80
rho=1.293; A_0=0.45; C_D=1.2
F = 400
#D = lambda v: 1/2*rho*C_D*A_0*v**2

f_v = 25.8
F_V = lambda v: -f_v*v
F_D = lambda v: F+F_V(v)

f_c = 488
t_c = 0.67
D = lambda v, t: 1/2*rho*C_D*A_0*(1-0.25*math.exp(-(t/t_c)**2))*v**2
F_C = lambda t: f_c*math.exp(-(t/t_c)**2)
F_net = lambda v, t: F + F_C(t) + F_V(v) - D(v, t)
t = [0]

x = [0]
v = [0]
#a = [(F-D(v[-1]))/m]
#a = [F_D(v[-1])/m]
a = [F_net(v[-1], t[-1])/m]

while x[-1] < 100:
#while a[-1] > 0.01:
    v.append( v[-1] + a[-1]*dt )
    x.append( x[-1] + v[-2]*dt )
    #a.append( (F-D(v[-1]))/m )

    #a.append( (F(v[-1])-D(v[-1]))/m )
    #a.append( (F_D(v[-1]))/m )
    a.append( F_net(v[-1], t[-1])/m)
    t.append(len(t)*dt)

#t = [i*dt for i in range(len(x))]
fig, axs = plt.subplots(1, 3, sharex=True)
axs[0].plot(t, a)
axs[0].set_ylabel('a [m/s^2]')
axs[1].plot(t, v)
axs[1].set_ylabel('v [m/s]')
axs[2].plot(t, x)
axs[2].set_ylabel('x [m]')


for ax in axs:
    ax.set_xlabel('t [s]')

plt.show()
print(t[-1])
#print(v[-1])
