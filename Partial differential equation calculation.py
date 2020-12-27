import math

c = 1
dx = 1 / 30
dt = 0.01

u_k0 = lambda x: math.sin(math.pi * x) + x + 2
u_k1 = lambda x: u_k0(x) + 4 * math.sin(2 * math.pi * x) * dt + ((c * dt ** 2) / (2 * dx ** 2)) * (u_k0(x + dx) - 2 * u_k0(x) + u_k0(x - dx))

xlist = [x * dx for x in range(int(1 / dx) + 1)]
tlist = [t * dt for t in range(int(1 / dt) + 1)]

list_k0 = [u_k0(i) for i in xlist]
list_k1 = [u_k1(j) for j in xlist]

result = []
result.append(list_k0)
result.append(list_k1)

for k in range(1,len(tlist)-1):
    A = []
    for j in range(1,len(xlist)-1):
        A1 = result[k][j]
        A2 = result[k - 1][j]
        A3 = result[k][j + 1]
        A4 = result[k][j - 1]
        A.append(2 * A1 - A2 + c * ((dt ** 2) /(dx ** 2)) * (A3 - 2 * A1 + A4))

    A.insert(0, 2.0)
    A.append(3.0)
    result.append(A)


print((result))
print((result[2]))
for k in range(len(result)):
    print(result[k])
import matplotlib.pyplot as plt
for k in range(0,101,10):
    plt.plot(result[k])
plt.show()
