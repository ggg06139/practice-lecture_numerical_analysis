import matplotlib.pyplot as plt

class Random:
    def __init__(self, seed, n, A =15485863, C=7, M=2 ** 31 - 1):
        self.seed = seed
        self.n = n
        self.A = A
        self.C = C
        self.M = M
        self.xi = self.seed

    def make_randomlist(self):
        randomlist = []
        for i in range(self.n):
            self.xi = (self.A * self.xi + self.C) % self.M
            randomlist.append(self.xi / self.M)
        return randomlist


import math
import matplotlib.pyplot as plt
fcn = lambda x: (1/(2*math.pi)**0.5)*math.exp(-(x**2/2))

a = 0
b = 3
ymax = 0.4

n = 10000
s = 0

f1 = Random(3, n)
f2 = Random(4, n)

x = f1.make_randomlist()
y = f1.make_randomlist()

for i, j in zip(x, y):
    x1 = a + (b - a) * i
    y1 = (ymax) * j

    if y1 <= fcn(x1):
        s += 1
        plt.plot(i, j, 'r.')
    else:
        plt.plot(i, j, 'b.')

I = (( (ymax) * (b-a) * s ) / n )

print(f'구한 답은 {I}입니다.')

plt.figure(1)
plt.title(f'182526 Hwang Seung Hyeon, N = {n}')
plt.xlabel('X')
plt.ylabel('Y')
plt.xlim(0,1)
plt.ylim(0,1)
plt.grid()
plt.show()
