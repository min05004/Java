"""
파일명 : exListComprehansion.py
프로그램 설명 : 리스트 컴프리헨션
"""
'''
리스트 컴프리헨션 (list comprehension)
리스트 컴프리헨션이란 리스트를 간략하게 표현한 것으로 리스트 안에 
for문을 사용할 수 있도록 한 것이다.

형식 (리스트 + for문) : 변수명 = [실행문 for문]
형식 (리스트 + for문 + 단일 if문) : 변수명 = [실행문 for문 if문]
형식 (리스트 + for문 + 단일 if~else문) : 변수명 = [실행문 if 조건식 else 실행문 for문 ]'''

# for문을 한 줄로 줄인다.
# a.append() 메소드는 삭제한다.
# 콜론(:)을 삭제한다.
# 변수 i를 왼쪽으로 이동시킨다.
# 대괄호([])를 추가한다.
# a변수에 저장한다.

# 리스트 컴프리헨션을 사용하지 않을 경우
# a=[]
# a.append(1)
# a.append(2)
# a.append(3)
# a.append(4)
# a.append(5)
# print()

# print("---------------------")
# a=[]
# for i in range(1,6):
#     a.append(i)

# print()


# 리스트컴프리헨션을 사용해서 값을 추가한 경우 
# 변수명 = [실행문 for문]
a = [i for i in range(1,6)]
print(a)

# 리스트컴프리헨션을 사용하지 않고 값을 추가한 경우
# for문을 한 줄로 줄인다.
# 콜론(:)을 삭제한다.
# 실행문을 왼쪽으로 이동시킨다.
# i는 남겨두고 b.append()를 삭제한다.
# 대괄호([]) 안으로 이동시킨다.
# b = [i for i in range(1,6)]

# b = [ i for i in range(1,6)]
  
print("---for문---")
# 형식 : 변수명 = [실행문 for문]
listData1 = [i for i in range(1,6)]
print(listData1)  # [1, 2, 3, 4, 5]

listData1 = [i*2 for i in range(1,6)]
print(listData1)  # [2, 4, 6, 8, 10] 각 리스트 안의 값의 *2 값이 들어감.

print("---if문---")
# 형식 : 변수명 = [실행문 for문 if문]
# listData2 = [] # 빈 리스트 이면 밑에서 변수명.append(값)이용해서 값을 추가하겠다라는 의미
# for i in range(1,11):
#     if i%2 == 0: # 짝수만 저장
#         listData2.append(i)

listData2 = [i for i in range(1,11) if i%2 == 0]
print(listData2)

print("---if else문---")
# 형식 : 변수명 = [실행문 if 조건식 else 실행문 for문 ]
# listData3 = [i if i%2 == 0 else i+100 for i in range(1,11)]
# 일렬 정리 후 .append 함수, 콜론: 지우기. 참인 경우인 식만 왼쪽 배치.
listData3 = []  # [101, 2, 103, 4, 105, 6, 107, 8, 109, 10]

for i in range(1,11):
    if i%2 == 0:  # 짝수
        listData3.append(i) # 짝수 이면 값은 그냥 저장됨.
    else:  # 홀수
        listData3.append(i+100) # 홀수일 경우는 홀수 값의 +100 해서 들어감.
print(listData3)  

print("---list comprehension---")
listData4 = [ i if i%2 ==0 else i+100 for i in range(1,11)]
print(listData4)

print("---contiue,break---")

for i in range(1,10):
    if i%2: # if i%2 == 1: 
        if i == 7: 
            break
        continue
    print(i)

else:
    print('for문 종료')    

print('프로세스 종료')
