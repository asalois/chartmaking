import numpy as np
import matplotlib.pyplot as plt


def find_max(array1, array2):
    max = -1000
    for i, ele in enumerate(array1):
        if array1[i] > max:
            max = array1[i]
            maxi = i
    print('Max= ', max)
    print('f= ', array2[maxi])
    for j in range(0, maxi):
        if array1[j] < max - 3:
            lower = array1[j]
            loweri= j
    # print(lower)
    # print(array2[loweri])
    for l in range(maxi, len(array1) -1):
        if array1[l] > max - 3:
            upper = array1[l]
            upperi = l
    # print(upper)
    # print(array2[upperi])
    print('BW =', array2[upperi] - array2[loweri])


plt.figure(1)
a, b, c, d = np.loadtxt("input/Lab 4 - sheet5.csv", delimiter=',', unpack= True, skiprows= 1)
e, f = np.loadtxt('input/LAB4Stuff - PhasePlotSeriesBW20000.csv', delimiter=',', unpack=True, skiprows=1, usecols=(1, 2))
g, h = np.loadtxt('input/LAB4Stuff - PhaseSeriesBW20000.csv', delimiter=',', unpack=True, skiprows=1, usecols=(1, 2))
plt.plot(a, b, label='R = 1850')
plt.plot(a, c, label='R = 3700')
plt.plot(a, d, label='R = 7400')
find_max(b, a)
find_max(c, a)
find_max(d ,a)
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


# x0, y0 = np.loadtxt("input/tek0026CH1.csv", delimiter=',', unpack= True, skiprows= 21)
# x1, y1 = np.loadtxt("input/tek0027CH1.csv", delimiter=',', unpack= True, skiprows= 21)
# x2, y2 = np.loadtxt("input/tek0028CH1.csv", delimiter=',', unpack= True, skiprows= 21)
# x3, y3 = np.loadtxt("input/tek0029CH1.csv", delimiter=',', unpack= True, skiprows= 21)
# x4, y4 = np.loadtxt("input/tek0030CH1.csv", delimiter=',', unpack= True, skiprows= 21)
# x5, y5 = np.loadtxt("input/tek0031CH1.csv", delimiter=',', unpack= True, skiprows= 21)
# x6, y6 = np.loadtxt("input/tek0032CH1.csv", delimiter=',', unpack= True, skiprows= 21)
# x7, y7 = np.loadtxt("input/tek0033CH1.csv", delimiter=',', unpack= True, skiprows= 21)
# x8, y8 = np.loadtxt("input/tek0034CH1.csv", delimiter=',', unpack= True, skiprows= 21)
# x9, y9 = np.loadtxt("input/tek0035CH2.csv", delimiter=',', unpack= True, skiprows= 21)
# x10, y10 = np.loadtxt("input/tek0036CH2.csv", delimiter=',', unpack= True, skiprows= 21)
#
#
# plt.figure(4)
# plt.plot(x0, y0)
# plt.plot(x1, y1)
# plt.plot(x2, y2)
# axes = plt.gca()
# axes.set_xlim(-.00025, .00025)
#
# f, axarr = plt.subplots(8, sharex=True)
# axarr[0].plot(x3, y3)
# axarr[1].plot(x4, y4)
# axarr[2].plot(x5, y5)
# axarr[3].plot(x6, y6)
# axarr[4].plot(x7, y7)
# axarr[5].plot(x8, y8)
# axarr[6].plot(x9, y9)
# axarr[7].plot(x10, y10)

plt.show()