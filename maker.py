import numpy as np
import matplotlib.pyplot as plt


plt.figure(2)
a, b, c, d = np.loadtxt("C:/Users/asalo/Desktop/Lab 4 - sheet5.csv", delimiter=',', unpack= True, skiprows= 1)
plt.plot(a, b)
plt.plot(a, c)
plt.plot(a, d)

plt.figure(3)
x, y = np.loadtxt("C:/Users/asalo/Downloads/Lab 4 - Voltage cap.csv", delimiter=',', unpack= True, skiprows= 1)
plt.plot(x, y)

plt.figure(4)
x, y = np.loadtxt("C:/Users/asalo/Downloads/Lab 4 - phase cap.csv", delimiter=',', unpack= True, skiprows= 1)
plt.plot(x, y)

plt.figure(5)
x, y = np.loadtxt("C:/Users/asalo/Downloads/Lab 4 - Voltage Cap Para.csv", delimiter=',', unpack= True, skiprows= 1)
plt.plot(x, y)

plt.figure(6)
x, y = np.loadtxt("C:/Users/asalo/Downloads/Lab 4 - phase Cap Para.csv", delimiter=',', unpack= True, skiprows= 1)
plt.plot(x, y)

plt.figure(26)
x, y = np.loadtxt("C:/Users/asalo/Downloads/Lab5/tek0026CH1.csv", delimiter=',', unpack= True, skiprows= 21)
plt.plot(x, y)

plt.figure(27)
x, y = np.loadtxt("C:/Users/asalo/Downloads/Lab5/tek0027CH1.csv", delimiter=',', unpack= True, skiprows= 21)
plt.plot(x, y)

plt.figure(28)
x, y = np.loadtxt("C:/Users/asalo/Downloads/Lab5/tek0028CH1.csv", delimiter=',', unpack= True, skiprows= 21)
plt.plot(x, y)

plt.figure(29)
x, y = np.loadtxt("C:/Users/asalo/Downloads/Lab5/tek0029CH1.csv", delimiter=',', unpack= True, skiprows= 21)
plt.plot(x, y)

plt.figure(30)
x, y = np.loadtxt("C:/Users/asalo/Downloads/Lab5/tek0030CH1.csv", delimiter=',', unpack= True, skiprows= 21)
plt.plot(x, y)

plt.figure(31)
x, y = np.loadtxt("C:/Users/asalo/Downloads/Lab5/tek0031CH1.csv", delimiter=',', unpack= True, skiprows= 21)
plt.plot(x, y)

plt.figure(32)
x, y = np.loadtxt("C:/Users/asalo/Downloads/Lab5/tek0032CH1.csv", delimiter=',', unpack= True, skiprows= 21)
plt.plot(x, y)

plt.figure(33)
x, y = np.loadtxt("C:/Users/asalo/Downloads/Lab5/tek0033CH1.csv", delimiter=',', unpack= True, skiprows= 21)
plt.plot(x, y)

plt.figure(34)
x, y = np.loadtxt("C:/Users/asalo/Downloads/Lab5/tek0034CH1.csv", delimiter=',', unpack= True, skiprows= 21)
plt.plot(x, y)

plt.figure(35)
x, y = np.loadtxt("C:/Users/asalo/Downloads/Lab5/tek0035CH2.csv", delimiter=',', unpack= True, skiprows= 21)
plt.plot(x, y)

plt.figure(36)
x, y = np.loadtxt("C:/Users/asalo/Downloads/Lab5/tek0036CH2.csv", delimiter=',', unpack= True, skiprows= 21)
plt.plot(x, y)

plt.show()