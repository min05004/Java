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
'''-- exWhile3.py --

실습>  아래 코드를 수정하시오.

로그인 횟수 1번 -> 3번으로 변경

-- jumsu2Login.py --'''
"""
파일명: jumsu2Login.py
프로그램 설명: 성적처리프로그램 + 로그인 기능 (입력 횟수: 3번)
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
'''-- jumsu2Login.py --

break문
반복문 안에서 실행문을 실행하는 도중에 break문을 만나면 반복문(loop)을 탈출(종료)한다.
break문은 반복문 밖에서는 단독으로 사용할 수 없다.
break문을 만나면 while문의 else와 for문의 else는 실행되지 않는다.
이유는 while문 안쪽으로 들어왔다는 얘기는 while의 else쪽과 무관하기 때문이다.
반복문 안에서 단독으로 사용할 수 있지만 주로 if문과 함께 사용한다.


-- exBreak.py --'''
"""
파일명: exBreak.py
프로그램 설명: break문
"""

# break  # SyntaxError: 'break' outside loop
i = 1          # 초깃값
while i <= 5:  # 조건식
    print(i)   # 실행문
    i += 1     # 증감식
    if i == 3:
        break

# while문으로 1 ~ 10까지 짝수중에서 2,4만 출력하시오.
i = 1          # 초깃값
while i <= 10:  # 조건식
    if i % 2 == 0:
        print(i)   # 실행문
        if i == 4:
            break
    i += 1     # 증감식

print('프로세스 종료')