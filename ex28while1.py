"""
파일명: exWhile1.py
프로그램 설명: while문
"""
print("--------while1문-----------")

# 반복문을 사용하지 않고 1 ~ 5까지 출력
i = 1
print(i)
i += 1
print(i)
i += 1
print(i)
i += 1
print(i)
i += 1
print(i)

# 반복문을 사용하고 1 ~ 5까지 출력
# 초깃값 -> 조건식 -> 실행문 -> 증감식

i = 1         # 초깃값
while i <= 5: # 조건식
    print("안녕하세요")  # 실행문
    i += 1    # 증감식
else:
    print('while문 종료')    

print("------------------")

listData = [1,2,3,4,5]
count = len(listData)  # listData의 전체 자료의 개수를 구한다.

a = 1                     # 초깃값
while a <= count:         # 조건식  자료의 개수만큼 반복한다.
    print(listData[a-1])  # 실행문
    a += 1                # 증감식

print("-------- while2문 --------")


import getpass

userid = 'pythonuser'  # 단순변수 -> File -> DB
userpw = '123456'

print('>>> 로그인 <<<')

i = 1
while i <= 3:
    inputUserid = input('사용자: ')
    inputUserpw = input('비밀번호: ')

    if userid == inputUserid and userpw == inputUserpw:
        print('로그인 성공!')
        print(f'{userid}님 환영합니다.')
        break
    else:
        print('로그인 실패!')
    i += 1
else:
    print('프로그램 종료')
    exit()    
print('로그인 후 실행되는 코드가 온다.')

"""
실습>  아래 코드를 수정하시오.
로그인 횟수 1번 -> 3번으로 변경

"""

# 1. 로그인 기능
import getpass

userid = 'pythonuser'  # 단순변수 -> File -> DB
userpw = '123456'

print('>>> 로그인 <<<')
i = 1
count = 3  # 로그인 횟수
while i <= count:
    inputUserid = input('사용자: ')
    inputUserpw = getpass.getpass('비밀번호: ')

    if userid == inputUserid and userpw == inputUserpw:
        print('로그인 성공!')
        print(f'{userid}님 환영합니다.')
        break
    else:
        print('아이디/비밀번호를 다시 확인해주세요!\n')
        i += 1   
else: 
    print('로그인 실패!')      
    import sys
    sys.exit()  
   
# 2. 입력 부분
name = input('이름: ')
kor  = int(input('국어점수: '))
eng  = int(input('영어점수: '))
mat = int(input('수학점수: '))
# print(name, kor, eng, mat)

# 3. 처리 부분
total = kor + eng + mat
average = total / 3

# 4. 출력 부분
print(f'이름: {name}')
print(f'국어점수: {kor}')
print(f'영어점수: {eng}')
print(f'수학점수: {mat}')
print(f'총점: {total}')
print(f'평균: {average:.2f}')


# 초기값, 조건식, 실행문, 증감식 순으로 분석하기
# 2단 ~ 9단까지 출력
# 1. 바깥쪽 while문, 2. 안쪽 while문


dan = 2  # 1.초깃값

while dan <= 9:  # 1.조건식 2 ~ 9
    # 1.실행문
    i = 1  # 2.초깃값
    while i <= 9:  # 2.조건식 1 ~ 9
        print(f'{dan}x{i}={dan*i:<3d} ', end='')  # 2.실행문
        i += 1  # 2.증감식
    else:
        print()

    dan += 1  # 1.증감식