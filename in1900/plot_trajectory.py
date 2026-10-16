import matplotlib.pyplot as plt
import numpy as np
import sys

sys.argv.pop(0)
y0, theta, v0 = [float(arg) for arg in sys.argv]

g = 9.81

a = -g / (2 * v0**2 * np.cos(theta)**2)
b = np.tan(theta)
c = y0

x1 = (-b + np.sqrt(b**2 - 4 * a * c))/ (2 * a)
x2 = (-b - np.sqrt(b**2 - 4 * a * c))/ (2 * a)

x_stop = max(x1,x2)

x = np.linspace(0, x_stop, 101)
y = a*x**2 + b*x + c

plt.plot(x,y)
plt.show()
