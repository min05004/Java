# 함수를 이용안하고 2단을 출력한 경우
dan = 2
for i in range(1,10):
     print(f'{dan}x{i}={dan*i}', end='  ')
else:
    print()

#함수를 이용해서 2단 출력
print("------함수이용1--------")
def gugudan () :
    dan=2
    for i in range(1,10):
        print(f'{dan}x{i}={dan*i}', end=' ')
    else :
        print()
    
gugudan()

print("------함수이용2--------")

def gugudan (dan) : # 매개변수를 생성해서 인수로 값을 받기.
    
    for i in range(1,10):
        print(f'{dan}x{i}={dan*i:<3}', end=' ') #:<3 왼쪽 3자리 정렬
    else :
        print()
    
gugudan(2)
gugudan(3)
gugudan(4)

print("------함수이용3--------")
# 2단 ~ 9단까지 효율적으로 호출하는 방법은?
for i in range(2,10):
    gugudan(i)   