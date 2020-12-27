import math

f = lambda x : math.exp(-(x**2))
ff = lambda x :-2*x*math.exp(-(x**2)) 
result = []

'''
for i in range(0,11):
    A = []
    x = i*0.1
    for j in range(1,11):
        h = j*0.01
        t = ff(x)
        a = (f(x+h)-f(x))/h
        A.append(abs((t-a)))
    result.append(A)
'''

for i in range(0,11):
    A = []
    x = i*0.1
    for j in range(1,11):
        h = j*0.01
        t = ff(x)
        a = (f(x+h)-f(x-h))/(2*h)
        A.append(abs((t-a)))
    result.append(A)



import matplotlib.pyplot as plt
for i in range(11):
    plt.plot(result[i])
plt.show()
