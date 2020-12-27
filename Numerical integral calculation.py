class NumericalIntegration():
  	#fcn: 함수명, h:구간의 크기, ys: x[i]에 해당하는 y[i]의 집합
	#a: 구간의 시작값, b: 구간의 끝값, n: 전체 구간의 개수
	#which: TrapezoidalRule/Simpson13 중 선택
	#doNumInit: 선택된 수치해석방법을 호출하는 함수
    def TrapezoidalRule(self, fcn, h, ys):
        I = (h/2)*(2*sum(ys) - ys[0] - ys[-1])
        return I
    
    def Simpson13(self, fcn, h, ys):
        A = 0
        B = 0
        if len(ys)%2 == 0:
            for a in range(1,len(ys)-1,2):
                A += ys[a]
            for b in range(2,len(ys),2):
                B += ys[b]
            I = (1/3)*h*(ys[0] + 4*A + 2*B + ys[-1])
        else:
            for a in range(1,len(ys),2):
                A += ys[a]
            for b in range(2,len(ys)-1,2):
                B += ys[b]
            I = (1/3)*h*(ys[0] + 4*A + 2*B + ys[-1])
        return I
    
    def doNumInt(self, which, fcn, a, b, n):
        h = (b-a)/n
        ys = []
        k = a
        while True:
            ys.append(fcn(k))
            k += h
            if len(ys) == n:
                ys.append(fcn(b))
                break
            
        A = which(fcn,h,ys)
        return A

fcn = lambda x : x**3
A = NumericalIntegration()
B = A.doNumInt(A.TrapezoidalRule, fcn, 1, 2, 10)

print(B)