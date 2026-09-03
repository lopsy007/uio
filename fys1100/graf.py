import matplotlib
matplotlib.use('TkAgg')

import matplotlib.pyplot as plt

def tegn(x: list[float], y: list[float], y_name: str, y_unit: str, x_name: str = 't', x_unit: str = 's', title: str = '', line: bool = True):

    plt.figure()

    if line:
        plt.plot(x, y)
    else:
        plt.plot(x, y, 'bo')
    plt.xlabel(f'{x_name} [{x_unit}]')
    plt.ylabel(f'{y_name} [{y_unit}]')
    plt.grid()
    plt.title(title)
    plt.xlim(0)
    plt.ylim(0)
    

    plt.show()

