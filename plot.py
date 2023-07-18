import numpy as np
import matplotlib.pyplot as plt

with open('tendon.txt', 'r') as f:
    lines = f.readlines()
    tt = [float(line.split()[0]) for line in lines]
    tzb = [float(line.split()[1]) for line in lines]
    tbx = [float(line.split()[2]) for line in lines]
    tby = [float(line.split()[3]) for line in lines]
    tbz = [float(line.split()[4]) for line in lines]
    tze = [float(line.split()[5]) for line in lines]
    tex = [float(line.split()[6]) for line in lines]
    tey = [float(line.split()[7]) for line in lines]
    tez = [float(line.split()[8]) for line in lines]

with open('muscle.txt', 'r') as f:
    lines = f.readlines()
    mt = [float(line.split()[0]) for line in lines]
    mze = [float(line.split()[1]) for line in lines]
    mex = [float(line.split()[2]) for line in lines]
    mey = [float(line.split()[3]) for line in lines]
    mez = [float(line.split()[4]) for line in lines]


plt.figure(1)
plt.plot(tt,mze, 'o', markersize=2,label="muscle begin")
plt.plot(mt,tze,'o', markersize=2,label="tendon end")

plt.xlabel("time (ms)")
plt.ylabel("z-coordinate (cm)")
plt.legend()
plt.show()

plt.figure(2)
plt.plot(tt[:-100],mez[:-100], 'o', markersize=2,label="muscle tz")
plt.plot(tt[:-100],tbz[:-100], 'o', markersize=2,label="tendon tz")
plt.xlabel("time (ms)")
plt.ylabel("z-coordinate (cm)")
plt.legend()
plt.show()

