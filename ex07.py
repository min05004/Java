stringData ="python!"
print('p' in stringData)
print('p' not in stringData)

print(len(stringData))


#초기값
#while 조건식 : 참이면 반복 ,거짓이면 나옴
# 실행문
# 증감식
print("---while문---")
i=0
while i<len(stringData):
    print(stringData[i])
    i = i+1

data = "오늘은 화요일 이고 파이썬을 배우고 있습니다."
# 글자 하나당 8byte (UTF-8)
print(data.find('파이썬')) # 파이썬을 찾으면 찾은 인덱스 번호를 출력함

#못 찾으면 -1로 나옴


# 반복성 (Iterable)
# 반복할 때 사용하는 형식 : 제어문을 사용한다.
# 제어문은 프로그램의 흐름을 제어할 때 사용한다.
# for문
# 형식 : 
# for 변수 in 리스트:
#     실행문1
# else:
#     실행문2

# for문을 이용해서 l변수에 저장된 1 ~ 5까지 출력하기
print("-------for문--------")

stringData = "python!"
for v in stringData :
    print(v, end=' ')
else:
    print()

