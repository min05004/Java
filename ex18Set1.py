'''
셋은 중복값을 허용하지 않는 집합 자료형이다.

셋의 특징
  . UnOrdered: 순서가 없다.
  . IMMutable: 값을 변경할 수 없다.
  . Iterable: 반복할 수 있다.
  . No duplicate: 중복된 데이터를 허용하지 않는다. 
  . 불변형 객체이므로 저장된 값을 변경할 수 없다.
  . 저장된 값은 순서가 지정되지 않아서 인덱스로 접근할 수 없다.

  . 멤버쉽 연산
  . 크기 함수
  . 반복성

형식 :
변수명 = { 값, ... }
변수명 = set()
변수명 = set([항목, 항목 ...])
변수명 = set((항목, 항목 ...))
변수명 = set({항목, 항목 ...})
변수명 = {}  <-- {} 는 빈 dictionary 자료형을 생성한다. 

'''
listData = [ 1,2,3,4,5,5,5 ]
setData = {1,2,3,4,5,5,5,}
print(listData)
print(setData) # 중복값 허용을 안함

# set은 indexing 을 할 수 없다.
# print(setData[0])  # TypeError 발생

# 데이터 추가: add(값) 1개만
# 데이터 추가: update(값) 2개 이상
# 데이터 삭제: remove(값)
# 데이터 삭제: pop(), 리스트와 다르게 앞의 데이터가 삭제된다.


# 데이터 추가 (1개)
# 형식 : 
# 변수명.add(값)
a = {1,2,3,4,5}
print(a)  # {1, 2, 3, 4, 5}
a.add(6)  # 6 추가
print(a)  # {1, 2, 3, 4, 5, 6}
# a.add(7,8,9)  # add()는 1개만 추가할 수 있다.


# 데이터 추가 (여러 개)
# 형식 :
# 변수명.update(값)
# iter(1)

# iter() 함수 : 객체가 iterable 객체인지 확인하는 함수
print(iter([]))    # <list_iterator object at 0x0000022EE1BADFD0>
print(iter({}))    # <dict_keyiterator object at 0x0000024DE5FD82C0>
print(iter(()))    # <tuple_iterator object at 0x000001A2CEBFDFD0>
# a.update(7,8,9)  # 개별 인수는 에러 발생!!! 
a.update((7,8,9))  # 변수 a에 7,8,9 를 추가한다.
print(a)  # {1, 2, 3, 4, 5, 6, 7, 8, 9}

# 데이터 삭제
# 형식 : 
# 변수명.remove(값)
# 변수명.pop()
a.remove(9)  # 9를 삭제한다.
print(a)     # {1, 2, 3, 4, 5, 6, 7, 8}
a.pop()
print(a)  # {2, 3, 4, 5, 6, 7, 8}
a.pop()
print(a)  # {3, 4, 5, 6, 7, 8}



