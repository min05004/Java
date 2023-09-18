# 딕셔너리변수.update()  : key와 value를 갱신한다.
# dictData1   {} 빈 딕셔너리가 된다.
# dictData2   {0: 10, 1: 20, 2: 30}

dictData1 = {0:100,1:200,2:300}
dicData2 = {0:10,1:20,2:30}
dictData1.update(dicData2) # .update()안에 함수의 값으로 업데이트 됨. 가지고 있는 항목들만! 업데이트가 됨.

# ** (별 두개) : 딕셔너리를 의미한다.
dictData1 = {0:100, 1:200, 2:300}# **dictData1 : dictData1 변수의 모든 항목들
                                 # **dictData2 : dictData2 변수의 모든 항목들
dictData2 = {3:400, 4:500, 5:600}
dictData3 = {**dictData1, **dictData2}
print()

# 딕셔너리변수.clear()  : 변수의 모든 항목을 삭제한다.
dictData1 ={0: 100, 1: 200, 2: 300}
dictData2 ={3: 400, 4: 500, 5: 600}
dictData3 ={0: 100, 1: 200, 2: 300, 3: 400, 4: 500, 5: 600}
dictData4 ={0, 1, 2, 3, 4, 5}
dictData1.clear()  # dictData1의 모든 항목을 삭제한다.
dictData2.clear()  # dictData2의 모든 항목을 삭제한다.
dictData3.clear()  # dictData3의 모든 항목을 삭제한다.
dictData4.clear()  # dictData4의 모든 항목을 삭제한다.

