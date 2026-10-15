import matplotlib.pyplot as plt
import numpy as np

k = 500 #N/m
m = 5.0 #kg
l_0 = 0.50 #m
h = 0.30 #m

#-------------- e
x = np.linspace(-0.75,0.75,151)

plt.plot(x, -k*x*(1-l_0/np.sqrt(x**2 + h**2)))
plt.xlabel('x [m]')
plt.ylabel('F [N]')
plt.show()
#-------------- f,g

x1s = [0.6, 0.65] #m
dt = 0.001
fig, axes = plt.subplots(2,3, figsize=(20,12), sharey='col')

for j,x1 in enumerate(x1s):
    t = np.arange(0,10,dt)
    x_list = np.zeros_like(t)
    v_list = np.zeros_like(t)
    a_list = np.zeros_like(t)
    x_list[0]=x1

    x = lambda x,dt,v: x+v*dt
    v = lambda v,dt,a: v+a*dt
    a = lambda x: (-k*x*(1-l_0/np.sqrt(x**2 + h**2)))/m


    for i in range(len(t)-1):
        a_list[i] = a(x_list[i])
        v_list[i+1] = v(v_list[i],dt,a_list[i])
        x_list[i+1] = x(x_list[i],dt,v_list[i+1])


    axes[j][0].plot(t,a_list)
    axes[j][0].set_xlabel('t [s]')
    axes[j][0].set_ylabel('a [m/s^2]')

    axes[j][1].plot(t,v_list)
    axes[j][1].set_xlabel('t [s]')
    axes[j][1].set_ylabel('v [m/s]')

    axes[j][2].plot(t,x_list)
    axes[j][2].set_xlabel('t [s]')
    axes[j][2].set_ylabel('x [m]')

    
plt.show()

#--------------- k

x1 = 0.75
my = 0.050
g = 9.81

x_list = np.zeros_like(t)
v_list = np.zeros_like(t)
a_list = np.zeros_like(t)
x_list[0]=x1

x = lambda x,dt,v: x+v*dt
v = lambda v,dt,a: v+a*dt
N = lambda x: (k*h*(1-l_0/np.sqrt(x**2 + h**2))+m*g)
R = lambda x,v: -np.sign(v)*my*abs(N(x))
a = lambda x,v: (-k*x*(1-l_0/np.sqrt(x**2 + h**2)) + R(x,v))    /m

for i in range(len(t)-1):
    a_list[i] = a(x_list[i],v_list[i])
    v_list[i+1] = v(v_list[i],dt,a_list[i])
    x_list[i+1] = x(x_list[i],dt,v_list[i+1])

fig, ax = plt.subplots(3, 1)
ax[0].plot(t,a_list)
ax[1].plot(t,v_list)
ax[2].plot(t,x_list)
plt.show()

#---------------- l
x1 = 0.75
my = 0.050
g = 9.81

x_list = np.zeros_like(t)
v_list = np.zeros_like(t)
a_list = np.zeros_like(t)
x_list[0]=x1

x = lambda x,dt,v: x+v*dt
v = lambda v,dt,a: v+a*dt
N = lambda x: (k*h*(1-l_0/np.sqrt(x**2 + h**2))+m*g)
R = lambda x,v: -np.sign(v)*my*abs(N(x))
a = lambda x,v: (-k*x*(1-l_0/np.sqrt(x**2 + h**2)) + R(x,v))    /m

W_list = np.zeros_like(t)
for i in range(len(t)-1):
    a_list[i] = a(x_list[i],v_list[i])
    v_list[i+1] = v(v_list[i],dt,a_list[i])
    x_list[i+1] = x(x_list[i],dt,v_list[i+1])
    dx = x_list[i+1]-x_list[i]
    W_list[i+1] = W_list[i] + R(x_list[i+1],v_list[i+1]) * dx

E_k = 1/2*m*v_list**2
print(W_list)
E_p = (max(E_k)+W_list)-E_k

fig, ax = plt.subplots(3, 1)
ax[0].plot(t, E_k)
ax[1].plot(t, E_p)
ax[2].plot(t,x_list)
plt.show()
