'''
성적처리 프로그램

'''
#함수이용하지 않음.
# 1. 입력 부분
name = input('이름: ')
kor  = int(input('국어점수: '))
eng  = int(input('영어점수: '))
mat = int(input('수학점수: '))
# print(name, kor, eng, mat)

# 2. 처리 부분
total = kor + eng + mat
average = total / 3

# 3. 출력 부분
print(f'이름: {name}')
print(f'국어점수: {kor}')
print(f'영어점수: {eng}')
print(f'수학점수: {mat}')
print(f'총점: {total}')
print(f'평균: {average:.2f}')


#함수 이용
# 1. 입력 부분

def jumsu():
 name = input('이름: ')
 kor  = int(input('국어점수: '))
 eng  = int(input('영어점수: '))
 mat = int(input('수학점수: '))
# print(name, kor, eng, mat)

# 2. 처리 부분
total = kor + eng + mat
average = total / 3
#3. 출력 부분
print(f'이름: {name}')
print(f'국어점수: {kor}')
print(f'영어점수: {eng}')
print(f'수학점수: {mat}')
print(f'총점: {total}')
print(f'평균: {average:.2f}')