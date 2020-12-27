def disection(fcn, a, b, t, tolv=10 ** (-10)):
    ainsert = fcn(a)
    binsert = fcn(b)

    if ainsert == t:
        return a
    if binsert == t:
        return b

    i = 0
    while True:
        m = (a + b) * 0.5
        minsert = fcn(m)

        if minsert == t:
            return m

        if i == 0:
            oldminsert = minsert
            if minsert < t:
                a = m
            else:
                b = m
        else:
            if abs((minsert - oldminsert) / minsert) <= tolv:
                return m
            else:
                oldminsert = minsert
                if minsert < t:
                    a = m
                else:
                    b = m
        i += 1

class ODEsolver():
    def Euler(self, fcn, x0, y0, xend, h):

        TH = []
        for i in range(x0, xend+1, h):
            TH.append(y0)
            y0 = y0 + fcn(y0) * h
        return TH

    def Heun(self, fcn, x0, y0, xend, h):

        TH = []
        for i in range(x0, xend+1, h):
            TH.append(y0)
            y0 = y0 + (0.5 * fcn(y0) + 0.5 * fcn(y0 + fcn(y0) * h))*h
        return TH

    def RungeKutta4(self, fcn, x0, y0, xend, h):

        TH = []
        for i in range(x0, xend+1, h):
            TH.append(y0)
            y0 = y0 + h*(1/6)*(fcn(y0) + 2*fcn(y0+0.5*fcn(y0)*h) + 2*fcn(y0+0.5*fcn(y0+0.5*fcn(y0)*h)*h) + fcn(y0+h*fcn(y0+0.5*fcn(y0+0.5*fcn(y0)*h)*h)))
        return TH

    def doODEsolving(self, which, fcn, x0, y0, xend, h):
        A = which(fcn, x0, y0, xend, h)
        return A


import sympy as sp

fcn = lambda x: -2.2067 * (10 ** (-(12))) * (x ** 4 - 81 * 10 ** 8)
ffcn = lambda x: (0.92593 * sp.log((x - 300) / (x + 300)) - 1.8519 * sp.atan(0.0033333 * x) + 2.9282) * 1000 / (
    -0.22067)

x0 = 0
y0 = 1200
xend = 6000
h = 240

T = []
TH0 = []
for k in range(x0,xend+1,h):
    TT = disection(ffcn, 1200, 301, k)
    T.append(k)
    TH0.append(TT)

f = ODEsolver()
TH1 = f.doODEsolving(f.Euler, fcn, x0, y0, xend, h)
TH2 = f.doODEsolving(f.Heun, fcn, x0, y0, xend, h)
TH3 = f.doODEsolving(f.RungeKutta4, fcn, x0, y0, xend, h)

import matplotlib.pyplot as plt
plt.plot(T,TH0,'red')
plt.plot(T,TH1,'blue')
plt.plot(T,TH2,'purple')
plt.plot(T,TH3,'yellow')
plt.show()
