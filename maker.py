# a program to help to make graphs for data from csv or text files
# by Alex Salois Feb 2018


import numpy as np
import matplotlib.pyplot as plt


def find_max(array1, array2):  # a function to find the max and the 3dB Bandwidth from dB data
    max = -1000
    for i, ele in enumerate(array1):
        if array1[i] > max:
            max = array1[i]
            maxi = i
    print('Max= ', max)
    print('f= ', array2[maxi])
    for j in range(0, maxi):  # to find the 3dB BW
        if array1[j] < max - 3:  # to find lower
            lower = array1[j]
            loweri= j
    for l in range(maxi, len(array1) - 1):  # to find higher
        if array1[l] > max - 3:
            upper = array1[l]
            upperi = l
    print('BW =', array2[upperi] - array2[loweri])


plt.figure(1)  # Plot 1 and inputing files
a, b, c, d = np.loadtxt("input/Lab 4 - sheet5.csv", delimiter=',', unpack= True, skiprows= 1)
e, f = np.loadtxt('input/LAB4Stuff - PhasePlotSeriesBW20000.csv', delimiter=',', unpack=True, skiprows=2, usecols=(1, 2))
g, h = np.loadtxt('input/LAB4Stuff - PhaseSeriesBW5000.csv', delimiter=',', unpack=True, skiprows=3, usecols=(1, 2))
x0, y0 = np.loadtxt('input/LAB4Stuff - MagnitudePlotParallelBW20000.csv', delimiter=',', unpack=True, skiprows=3, usecols=(1, 2))
x1, y1 = np.loadtxt('input/LAB4Stuff - PhasePlotParallelBW20000.csv', delimiter=',', unpack=True, skiprows=3, usecols=(1, 2))
x2, y2 = np.loadtxt('input/LAB4Stuff - PhasePlotParallelBW5000.csv', delimiter=',', unpack=True, skiprows=3, usecols=(1, 2))
x3, y3 = np.loadtxt('input/LAB4Stuff - MagnitudePlotParallelBW5000.csv', delimiter=',', unpack=True, skiprows=3, usecols=(1, 2))


# add plots to figure 1
plt.plot(a, b, label='R = 1850')
plt.plot(a, c, label='R = 3700')
plt.plot(a, d, label='R = 7400')
find_max(b, a)
find_max(c, a)
find_max(d, a)
find_max(y0, x0)
find_max(y3, x3)
plt.xlabel('Frequency')
plt.ylabel('dB Voltage')
axes = plt.gca()
axes.set_xlim(15000, 45000)
axes.set_ylim(-40, 0)
plt.legend()
plt.savefig("output/different rs.png")

plt.figure(2)
plt.title('Voltage of a RLC')
ax, ay = np.loadtxt("input/Lab 4 - Voltage cap.csv", delimiter=',', unpack= True, skiprows= 1)
bx, by = np.loadtxt("input/Lab 4 - phase cap.csv", delimiter=',', unpack= True, skiprows= 1)
cx, cy = np.loadtxt("input/Lab 4 - Voltage Cap Para.csv", delimiter=',', unpack= True, skiprows= 1)
dx, dy = np.loadtxt("input/Lab 4 - phase Cap Para.csv", delimiter=',', unpack= True, skiprows= 1)
find_max(ay, ax)
find_max(cy, cx)
plt.plot(ax, ay, label='Series')
plt.plot(cx, cy, label='Parallel')
plt.xlabel('Frequency')
plt.ylabel('dB Voltage')
plt.legend()
axes = plt.gca()
axes.set_xlim(0, 600000)
axes.set_ylim(-80, 20)
plt.savefig("output/voltage.png")

plt.figure(3)
plt.title('Phase of a RLC')
plt.plot(bx, by, label='Series')
plt.plot(dx, dy, label='Parallel')
plt.xlabel('Frequency')
plt.ylabel('Degrees')
plt.legend()
axes = plt.gca()
axes.set_xlim(0, 100000)
axes.set_ylim(-180, 100)
plt.savefig("output/phase.png")

plt.figure(4)
plt.title('Phase change R')
plt.plot(g, h, label='R = 1850')
plt.plot(bx, by, label='R = 3700')
plt.plot(e, f, label='R = 7400')
plt.xlabel('Frequency')
plt.ylabel('Degrees')
plt.legend()
axes = plt.gca()
axes.set_xlim(0, 25000)
plt.savefig("output/phasers.png")

plt.figure(5)
plt.plot(cx, cy, label='R = ')
plt.plot(x0, y0, label='R = ')
plt.plot(x3, y3, label='R = ')
plt.xlabel('Frequency')
plt.ylabel('dB Voltage')
plt.legend()
axes = plt.gca()
axes.set_xlim(10000, 60000)
axes.set_ylim(-40, 0)
plt.savefig("output/voltagepara.png")


plt.figure(6)
plt.title('Phase change R')
plt.plot(x1, y1, label='R = ')
plt.plot(dx, dy, label='R = ')
plt.plot(x2, y2, label='R = ')
plt.xlabel('Frequency')
plt.ylabel('Degrees')
plt.legend()
axes = plt.gca()
axes.set_xlim(0, 60000)
plt.savefig("output/phaserspara.png")
plt.show()
