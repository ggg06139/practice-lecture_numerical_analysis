import sympy as sp
x,y,z = sp.symbols('x y z')

#테일러 시리즈 중 sin(x)의 근사함수를 구현한 함수

def funsin(x,n):
    z = 0
    def fac(a):
        result = 1
        for i in range(1, a + 1):
            result *= i
        return result

    for k in range(n+1):
        y = (-1)**k * (x**(2*k + 1)) / (fac(2*k + 1))
        z = z + y

    return z

#NR법으로 해와 반복 횟수를 반환하는 함수

def rootFinds_NRM(fcn,  fcnp, a, tolv = 10**(-10)):     #tolv = 10^-10으로 디폴트 인자를 사용하였습니다.
                                                        #fnc: 함수, fcnp: 함수미분, a:초기값, tolv: 임계값

    ainsert = fcn.subs(x,a)
    if ainsert == 0:                                    #운이 좋아서 초기값을 넣은 값이 0이 된다면 초기값을 근으로, 반복 횟수는 0으로 반환합니다.
        return a, 0
    else:
        i = 0                                           #처음 실행한 것은 반복이 아니므로, i의 초기값을 0으로 정했습니다.
        while True:
            ainsert = fcn.subs(x,a)                     #ainsert에 subs 메소드를 이용해서 fcn함수에 a를 넣은 값으로 초기화 합니다.
            apinsert = fcnp.subs(x,a)                   #apinsert에 subs 메소드를 이용해서 fcnp함수에 a를 넣은 값으로 초기화 합니다.

            apresent = a - ainsert/apinsert             #a = a - f(a)/f'(a)를 표현했습니다.

            if i == 0:                                  #상대근사오차를 갖기 위해 처음 실행하면 tolv와 비교를 하지 않습니다.
                abefore = apresent                      #a이전값을 a현재값으로 초기화합니다. 이렇게 해야, 다음 반복문 실행 시 이전값으로 인식합니다.
                a = apresent                            #a에 a현재값으로 초기화합니다.
            else:
                if (abs((apresent-abefore)/apresent)) <= tolv:
                    return apresent, i                  #상대참오차가 지정한 값보다 작거나 같으면 a현재값과 반복 횟수인 i를 반환합니다.
                else:
                    abefore = apresent                  #상대참오차가 지정한 값보다 크면 a이전값과 a를 현재값으로 초기화 합니다.
                    a = apresent
            i += 1

root, repeat = rootFinds_NRM(funsin(x,9), sp.cos(x) , 3.2)

print(f'해는 {root}이고 반복 횟수는 {repeat}입니다.')