import matplotlib.pyplot as plt
import numpy as np

k = 500 #N/m
m = 5.0 #kg
l_0 = 0.50 #m
h = 0.30 #m

x = np.linspace(-0.75,0.75,151)

plt.plot(x, -k*x*(1-l_0/np.sqrt(x**2 + h**2)))
plt.show()


x1 = 0.65 #m
dt = 0.00001
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


plt.plot(t,a_list)
plt.show()
plt.plot(t,v_list)
plt.show()
plt.plot(t,x_list)
plt.show()


x1 = 0.75
my = 0.050
g = 9.81

x_list = np.zeros_like(t)
v_list = np.zeros_like(t)
a_list = np.zeros_like(t)
x_list[0]=x1

x = lambda x,dt,v: x+v*dt
v = lambda v,dt,a: v+a*dt
R = lambda x,v: -np.sign(v)*my*(k*h*(1-l_0/np.sqrt(x**2 + h**2))+m*g)
a = lambda x,v: (-k*x*(1-l_0/np.sqrt(x**2 + h**2)) + R(x,v))    /m

for i in range(len(t)-1):
    a_list[i] = a(x_list[i],v_list[i])
    v_list[i+1] = v(v_list[i],dt,a_list[i])
    x_list[i+1] = x(x_list[i],dt,v_list[i+1])


plt.plot(t,a_list)
plt.show()
plt.plot(t,v_list)
plt.show()
plt.plot(t,x_list)
plt.show()
