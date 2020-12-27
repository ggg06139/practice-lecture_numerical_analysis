inputNumber = float(input('임의의 실수를 입력하시오 :'))
N = int(inputNumber)
F = inputNumber - int(inputNumber)
integerPart = []
fractionPart = []
def integerFunction(N):
    if N == 0:                          #N이 0일 경우 탈출
        return 1
    Q = N // 2
    R = N % 2
    integerPart.append(str(R))
    N = Q
    integerFunction(N)
def fractionFunction(F,c):
    if c == 10:
        return 1
    else:
        F = F * 2
        if F == 1:                          #F가 1일 경우 1을 문자 형태로 리스트에 기록 후 탈출
            fractionPart.append(str(1))
            return 1
        elif F == 0:                        #F가 0일 경우 탈출
            return 1
        elif F > 1:
            fractionPart.append(str(1))
            F = F - 1
        elif F < 1:
            fractionPart.append(str(0))
    c += 1
    fractionFunction(F,c)


integerFunction(N)
integerPart.reverse()                   # 정수부분 배열 뒤집기
fractionFunction(F,0)

# 입력값에 소수부분이 존재하지 않으면 정수부분 결과값만 출력하도록
if inputNumber - int(inputNumber) != 0:
    result = ''.join(integerPart) + '.' + ''.join(fractionPart) #소수점 10자리 이하까지만 나오도록
else:
    result = ''.join(integerPart)

# 결과값 출력
print(result)
