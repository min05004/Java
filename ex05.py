# 자료형 : 정수, 실수, 문자열, 리스트, 튜플, 딕셔너리, 셋, 불리언(불)

#type() : 자료형을 확인하기 위해서 사용 
# 형식 : type(값), type(변수명) 

a = 10 #int 정수
print(a,type(a))

b = 3.14 #float 실수
print(b,type(b))

d = [1,2,3]  # 리스트 (list)
print(d,type(d))

e = (1,2,3)  # 튜플 (tuple) , (괄호 생략 가능)!
print(e,type(e))

f = {1,2,3}  # 셋 (set) 
print(f,type(f))

g = {'a':1, 'b':2, 'c':3}  # 딕셔너리 (dict) /  형식-  '변수명' : 값 
print(g,type(g))

h = True     # 불리언 or 불(bool) / True*대문자!!
print(f,type(h))