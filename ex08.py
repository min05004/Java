# + 연산자
# + 연산자를 이용해서 문자열끼로 더할 수 있다.
# 형식 : 
# "문자열1" + "문자열2"  => 문자열1문자열2
# 문자열변수1 + 문자열변수2 => 문자열변수1의값문자열변수2의값
# 변수명 = "문자열1" + "문자열2"  => 문자열1문자열2
# 변수명 = 문자열변수1 + 문자열변수2 => 문자열변수1의값문자열변수2의값

StringData1= "hello"
StringData2= " python"
print(StringData1 + StringData2)

StringData1 = StringData1 + StringData2  # StringData1 +=  StringData2 동일
print(StringData1)

print("-----------")
# * 연산자
# * 연산자를 이용해서 문자열을 반복한다.
# 형식 : 
# "문자열1" * 3  => 문자열1문자열1문자열1
# 문자열변수1 * 3 => 문자열변수1에 저장된 값을 3번 반복

print(StringData1 * 3)
print(StringData1 + StringData2 * 3) # 우선순위는 * 가 높아서 *먼저 연산이 됨./ = 대입연산이 제일 낮음
print((StringData1 + StringData2) * 3)

print("------------")

line = '*' * 20

print(line)
print('안녕하세요!!!')
print(line)
print('파이썬입니다.!!!')
print(line)

# 문자열은 
# +, * 연산은 가능하지만
# -, / 연산은 불가능하다. 
# print(stringData1 / stringData2)
# print(stringData1 - stringData2)

print("---------------")
