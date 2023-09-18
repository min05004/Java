setData1 = {1,2,3,4,5}
setData2 = {1,7,2,8,3}

# 교집합
# 형식 : 
# 연산자를 이용하는 방법 : 변수1 & 변수2
# 메소드를 이용하는 방법 : 변수1.intersection(변수2)
print("교집합", setData1 & setData2)  # 교집합 {1, 2, 3}
print("교집합", setData1.intersection(setData2))  # 교집합 {1, 2, 3}

# 합집합
# 형식 : 
# 연산자를 이용하는 방법 : 변수1 | 변수2
# 메소드를 이용하는 방법 : 변수1.union(변수2)
print("합집합", setData1 | setData2)  # {1, 2, 3, 4, 5, 7, 8}
print("합집합", setData1.union(setData2))  # {1, 2, 3, 4, 5, 7, 8}

# 차집합
# 형식 : 
# 연산자를 이용하는 방법 : 변수1 - 변수2
# 메소드를 이용하는 방법 : 변수1.difference(변수2)
print("차집합", setData1 - setData2)  # 차집합 {4, 5}
print("차집합", setData1.difference(setData2))  # 차집합 {4, 5}


# listData1의 중복값을 제거하기 위해서 set을 사용한다.
listData1 = [1,2,3,1,2,3,3,3,3,4,4]
listData2 = set(listData1)
print(listData1)  # [1, 2, 3, 1, 2, 3, 3, 3, 3, 4, 4]
print(listData2)  # {1, 2, 3, 4}
listData1 = list(listData2)
print(listData1)  # [1, 2, 3, 4]