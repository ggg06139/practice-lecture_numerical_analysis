import sympy as sp
x = sp.symbols('x')

def fun1(x):
    return sp.tan(x) - 2*x

def fun2(x):
    return 65*(x**4) - 72*(x**3) -1.5*(x**2) + 16.5*x - 1

def fun3(x):
    return x**3 - 6*(x**2) + 12*x - 8

def fun4(x):
    return sp.sin(x)

#이분법으로 해와 반복 횟수를 반환하는 함수

def rootFindings_Bisection(fcn, a, b, tolv = 10**(-10)):    #tolv = 10^-10으로 디폴트 인자를 사용하였습니다.
                                                            #fnc: 함수, a:구간 시점, b:구간 종점, tolv: 임계값

    ainsert = fcn.subs(x,a)                                 #subs 라는 값을 대입해주는 메소드를 사용했습니다.
    binsert = fcn.subs(x,b)

    if ainsert == 0:                                        #운이 좋게 a나 b를 넣은 값이 0이 된다면 return 값으로 받아오고 반복 횟수 0이 됩니다.
        return a, 0
    if binsert == 0:
        return b, 0

    if ainsert * binsert < 0:
        i = 0                                               #처음 실행한 것은 반복이 아니므로, i의 초기값을 0으로 정했습니다.
        while True:
            x_m = (a + b) * 0.5                             #x_m을 중간값으로 칭하겠습니다.
            x_minsert = fcn.subs(x,x_m)

            if x_minsert == 0:
                return x_m, i
            else:
                if i == 0:                                  #상대근사오차를 구하기 위해서는 적어도 한번은 반복을 해야합니다.
                    beforex_m = x_m
                    if x_minsert * ainsert > 0:             #만일 f(중간값)과 f(a)값의 곱이 양수면 중간값과 a 사이에는 해가 없습니다.
                        a = x_m                             #따라서 a에 중간값을 초기화 해줍니다.
                    else:                                   #반대의 상황이라면 중간값과 a 사이에 해가 존재합니다.
                        b = x_m                             #따라서 b에 중간값을 초기화 해줍니다.
                else:
                    if abs((x_m-beforex_m)/x_m) <= tolv:    #상대근사오차 구하는 식입니다.
                        return x_m, i                       #상대근사오차가 정해둔 값보다 작거나 같다면 종료합니다.
                    else:                                   #그렇지 않다면 다시 a와 b중에서 중간값으로 초기화 할 값을 찾아서 초기화해줍니다.
                        beforex_m = x_m
                        if x_minsert * ainsert > 0:
                            a = x_m
                        else:
                            b = x_m
            i += 1
    else:
        print('{a}와 {b}사이에 해가 없습니다.')
        return -1, -1                                       #해가 없게 되면 아래의 문장에서 에러가 나기 때문에 -1값을 주었습니다.


root, repeat = rootFindings_Bisection(fun2(x), 0, 1)

if root >=0 or repeat >=0:                                  #해가 없다면 실행이 되지 않도록 해두었습니다.
    print(f'해는 {root}이고 반복 횟수는 {repeat}입니다.')