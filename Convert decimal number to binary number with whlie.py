inputNumber=float(input('임의의 실수를 입력하시오 :'))
N=int(inputNumber)
F=inputNumber-int(inputNumber)
integerPart=[]
fractionPart=[]

while True:
    Q=N//2
    R=N%2
    integerPart.append(str(R)) #문자형태로 R을 integerPart에 저장
    N = Q
    if Q==0:                   #Q가 0이면 반복문 탈출
        break
integerPart.reverse()          #문자형태 R의 모임으로 저장된 리스트를 뒤집기
i=0
while F!=0:                    #F가 0이 아닐 때만 반복
    T=F*2
    S=int(T)
    T=T-int(T)
    fractionPart.append(str(S))
    F=T
    i=i+1
    if i==10:                  #소수점 10자리 이하까지만 나오도록 그 이상은 탈출
        break

if inputNumber-int(inputNumber) !=0:
    result=''.join(integerPart)+'.'+''.join(fractionPart)
else:
    result=''.join(integerPart)
print(result)
