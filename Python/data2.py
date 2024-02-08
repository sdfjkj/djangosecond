import numpy as numpy
ar = numpy.arange(10)
# Fancy Inndexing
#데이터를 복제합니다
br = ar[[1,3,5,7]]
print(br)
br[0] = 15700
print(br)
print(ar)

matrix = ar.reshape((2,-1))
print(matrix)
print(matrix[:,0])
# 2차원 배열에서 list를 이용해서 행 번호나 열 번호를 지정하면 2차원 배열이 만들어집니다.
print(matrix[:,[0]])
#numpy의 ndarray나 pandas의 DataFrame에서 하나의 열을 선택할 때 list로 설정하는 경우는 구조를 유지하기 위해서입니다.
print(bool([1,2,3] and [1,2,3]))
print(bool([1,2,3] and []))
print(matrix+10)
data = numpy.array([100,200,300,400,500])
print(matrix+data)

print(matrix)
print(ar)
# 브로드캐스트 연산
# numpy의 ndarray와 논리연산을 수행하면 bool의 배열이 만들어진다
print(ar == 3)
# 인덱스의 bool배열을 대입하면 True인 데이터만 추출됨
print(ar[ar%2 ==1])
print(ar[(ar%2 ==1) | (ar%4 ==0)])

# 홀수이거나 4의 배수인 데이터만 골라내기
