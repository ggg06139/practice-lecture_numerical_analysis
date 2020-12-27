def getNDDCoeffs(x, y):
    n = len(y)
    pyramid = [[0 for c in range(n)] for r in range(n)]
    for j in range(n):
        pyramid[j][0] = y[j]

    for j in range(1,n):
        for i in range(n-j):
               pyramid[i][j] = (pyramid[i+1][j-1] - pyramid[i][j-1]) / (x[i+j] - x[i])
    return pyramid

def calculateNewtonInterFcn(x, x_input, c):
    a = 1
    y_out = c[0]
    i = 0
    while True:
        if i == len(c)-1:
            break
        a *= (x_input-x[i])
        y_out += c[i+1]*a
        i += 1
    return y_out

def AddOneDataPair(pyramid, x, y, x_new, y_new):
    x.append(x_new)
    y.append(y_new)
    a = len(pyramid)
    b = 0
    c = a

    pyramid.append([0 for i in range(a+1)])
    pyramid[a][0] = y_new

    for i in range(a):
        pyramid[i].append(0)
    
    while True:
        if c == 0:
            break
        pyramid[c-1][b+1] = (pyramid[c][b] - pyramid[c-1][b]) / (x[a] - x[c-1])
        b += 1
        c -= 1
        
    return x, y , pyramid

x = [-1,0,1,2]
y = [1,1,2,0]

x_new = 3
y_new = -1
pyramid = getNDDCoeffs(x, y)
c = pyramid[0]


import matplotlib.pyplot as plt
s = -2
xx = []
yy = []
while s <= 3:
    xx.append(s)
    yy.append(calculateNewtonInterFcn(x, s, c))
    s += 5/1000
plt.plot(xx,yy)
plt.show()

