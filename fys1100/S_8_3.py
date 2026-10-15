import matplotlib.pyplot as plt
import numpy as np



g = 9.81
l = 2
dt = 0.01
t = np.arange(0,30,dt)
thetas = np.zeros_like(t)

v0 = 0
theta0 = 20

#alpha = vinkelaksellerasjon, omega = vinkelfart, theta = vinkel
alpha = lambda theta: -g/l*np.sin(theta)

thetas[0] = np.deg2rad(theta0)
v = v0

for i in range(len(t)-1):
    v += alpha(thetas[i])*dt
    thetas[i+1] = (thetas[i] + v*dt)

plt.plot(t,np.degrees(thetas))
plt.show()

#--------------------------------------
thetaanal = lambda t: np.deg2rad(theta0)*np.cos(np.sqrt(g/l)*t)
theta0s = [15,30,45,90]

for theta0 in theta0s:
    thetas = np.zeros_like(t)
    thetas[0] = np.deg2rad(theta0)
    v = v0
    for i in range(len(t)-1):
        v += alpha(thetas[i])*dt
        thetas[i+1] = (thetas[i] + v*dt)
    #plt.plot(t,np.degrees(thetas), 'r')
    #plt.plot(t,np.degrees(thetaanal(t)))
    #plt.show()
#---------------------------------------
thetaanal = lambda t: np.deg2rad(theta0)*np.cos(np.sqrt(g/l)*t)


dts = [1,0.1,0.01,0.001,0.0001]
theta0s = [15,30,45,90]

fig, axes = plt.subplots(len(dts), len(theta0s), figsize=(16, 16), sharex=True)

for row, dt in enumerate(dts):
    t = t = np.arange(0,30,dt)

    for col, theta0 in enumerate(theta0s):
        thetas = np.zeros_like(t)
        thetas[0] = np.deg2rad(theta0)
        v = v0
        for i in range(len(t)-1):
            v += alpha(thetas[i])*dt
            thetas[i+1] = (thetas[i] + v*dt)

        ax = axes[row,col]
        ax.plot(t, np.degrees(thetas), 'r', label='numerisk')
        ax.plot(t, np.degrees(thetaanal(t)), label='analytisk')
        ax.set_title(f'dt={dt}, theta0={theta0}')

for ax in axes[-1]:
    ax.set_xlabel('t [s]')

for ax in axes[:, 0]:
    ax.set_ylabel('theta [deg]')

axes[0, 0].legend()
plt.tight_layout()
plt.show()

#---------------------------------------

dts = [1,0.1,0.01,0.001,0.0001]
theta0s = [15,30,45,90]

fig, axes = plt.subplots(len(dts), len(theta0s), figsize=(16, 16), sharex=True)

for row, dt in enumerate(dts):
    t = t = np.arange(0,30,dt)

    for col, theta0 in enumerate(theta0s):
        thetas = np.zeros_like(t)
        thetas[0] = np.deg2rad(theta0)
        v = v0
        for i in range(len(t)-1):
            thetas[i+1] = (thetas[i] + v*dt)
            v += alpha(thetas[i])*dt

        ax = axes[row,col]
        ax.plot(t, np.degrees(thetas), 'r', label='numerisk')
        ax.plot(t, np.degrees(thetaanal(t)), label='analytisk')
        ax.set_title(f'dt={dt}, theta0={theta0}')

for ax in axes[-1]:
    ax.set_xlabel('t [s]')

for ax in axes[:, 0]:
    ax.set_ylabel('theta [deg]')

axes[0, 0].legend()
plt.tight_layout()
plt.show()