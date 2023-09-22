print(" --로그인 기능이 없는 성적 처리 프로그램 ---")

# 1. 입력 부분
name = input('이름: ')
kor  = int(input('국어점수: '))
eng  = int(input('영어점수: '))
mat = int(input('수학점수: '))
# print(name, kor, eng, math)

# 2. 처리 부분
total = kor + eng + mat
average = total / 3

# 3. 출력 부분 
print(f'이름: {name}') # 안 쪽의 함수 부터 반환을 해줌
print(f'국어점수: {kor}')
print(f'영어점수: {eng}')
print(f'수학점수: {mat}')
print(f'총점: {total}')
print(f'평균: {average:.2f}')

print("-------------------------------")
print("로그인 기능이 있는 성적처리 프로그램")

# 1. 로그인 기능
import getpass

userid = 'pythonuser'  # 단순변수 -> File -> DB
userpw = '123456'

print('>>> 로그인 <<<')
inputUserid = input('사용자: ')
inputUserpw = getpass.getpass('비밀번호: ')

if userid == inputUserid and userpw == inputUserpw:
    print('로그인 성공!')
    print(f'{userid}님 환영합니다.')
else:
    print('로그인 실패!')
    exit()
    
# 2. 입력 부분
name = input('이름: ')
kor  = int(input('국어점수: '))
eng  = int(input('영어점수: '))
mat = int(input('수학점수: '))
# print(name, kor, eng, math)

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


number = input('숫자입력: ')

if number ==1 :
    print("1입니다.")
if number ==2 :
    print("2입니다.")
if number ==3 :
    print("3입니다.")
if number ==4 :
    print("4입니다.")


print("-------다중 if문 성적처리프로그램--------")

# A학점 : 90 ~ 100   , grade = 'A'
# B학점 : 80 ~ 89.9  , grade = 'B'
# C학점 : 70 ~ 79.9  , grade = 'C'
# D학점 : 60 ~ 69.9  , grade = 'D'
# F학점 : 0 ~ 59.9   , grade = 'F'
# 1. 점수 입력
print('>>> 성적 처리 프로그램 <<<')
kor  = input('국어 점수: ')
eng  = input('영어 점수: ')
mat = input('수학 점수: ')

# 2. 점수 체크
kor  = 0 if not kor.isdigit()  else int(kor)
eng  = 0 if not eng.isdigit()  else int(eng)
math = 0 if not mat.isdigit() else int(mat)

# 3. 점수 계산
total = kor + eng + mat  # 총점
average = total / 3  # 평균

# 4. 학점 구하기
# A학점 : 90 ~ 100   , grade = 'A'
# B학점 : 80 ~ 89.9  , grade = 'B'
# C학점 : 70 ~ 79.9  , grade = 'C'
# D학점 : 60 ~ 69.9  , grade = 'D'
# F학점 : 0 ~ 59.9   , grade = 'F'
if average >= 90 and average <= 100:  # A학점 : 90 ~ 100
    grade = 'A'
elif average >= 80 and average < 90:  # B학점 : 80 ~ 89.9
    grade = 'B'
elif average >= 70 and average < 80:  # C학점 : 70 ~ 79.9
    grade = 'C'
elif average >= 60 and average < 70:  # D학점 : 60 ~ 69.9
    grade = 'D'
else:  # F학점 : 0 ~ 59.9  
    grade = 'F'

# 5. 점수 출력
print('>>> 점수의 결과 <<<\n'
     f'국어 점수: {kor}\n'
     f'영어 점수: {eng}\n'
     f'수학 점수: {mat}\n'
     f'총점: {total}\n'
     f'평균: {average:.2f}\n'
     f'학점: {grade}')