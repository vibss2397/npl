import matplotlib.pyplot as plt
import time
import random
import sys
import loading

def func1():
    axes = plt.gca()
    axes.set_xlim(0, 100)
    axes.set_ylim(-50, +50)
    line, = axes.plot(xdata, ydata, marker='o',linewidth=1, markersize=3,color='#17A2B8')
    return line,axes

def draww(linee,i,ax):
    xdata.append(i*4)
    ydata.append(ysample[i])
    xmin, xmax = ax.get_xlim()
    plt.text(xmin-10, 6, r'$\mu=%,\ \sigma=15$')
    linee.set_xdata(xdata)
    linee.set_ydata(ydata)
    plt.draw()

def main():
    plt.show()
    line,axes=func1()
    for i in range(100):
        draww(line,i,axes)
        plt.pause(1e-17)
        time.sleep(1)
        loading.loading_dots()
    plt.show()

if __name__ == '__main__':
    ysample = random.sample(range(-50, 50), 100)
    xdata = []
    ydata = []
    main()
