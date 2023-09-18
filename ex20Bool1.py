'''
Bool
불리언 자료형은 참과 거짓을 나타내는 자료형이다.
주로 제어문에 많이 사용된다.

# 불리언 자료형은 참과 거짓을 나타내는 자료형이다.
# True : 참
# False : 거짓

print(3 > 5)  # False 왼쪽 기준으로 읽음
print(10 < 20)  # True

'''

# 이터러블은 반복할 수 있으므로 반복문인 for문으로 돌릴 수 있다.
# 형식 : 
# for 변수명 in 문자열, 리스트, 튜플, 딕셔너리, 셋, 함수:
#     실행문
# for i in [1,2,3,4,5]:
for i in range(1,6):  # 1 ~ 5
    print(i)

for i in range(5):  # 0 ~ 4
    print(i)


# 데이터를 반복하면서 출력한 형태
i = 0          # 초기값
while i < len(listData):  # 조건식
    print(listData[i])   # 실행문
    i += 1     # 증감식

print('프로그램 종료')