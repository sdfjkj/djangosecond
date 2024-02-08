import numpy as numpy
ar = numpy.array([1,2,3])
# ndim은 몇 차원인지 확인
# print(ar.ndim) #단순한 리스트로 1차원 배열이 됨
# shape 각 차원의 데이터 개수를 튜플로 리턴
# print(ar.shape) # 3개인데 출력을 할 때는 튜플로 출력이 되어야 해서 (3, )

table = numpy.array([[1,2,3],[4,5,6]])
# print(table.ndim) # list 안에 list가 있어서 2차원
# print(table.shape) # 2행 3열의 배열이므로 (2,3)
# print(table.dtype) 

image = numpy.array([[[1,2,3],[1,2,3]],[[4,5,6],[7,8,9]]])
# print(image.ndim) # 3
# print(image.shape) #(2,2,3)

ar = numpy.arange(1,10,2)
ar1 = numpy.arange(10,2,-1)
# print(ar)
# print(ar1)

ar2 = numpy.empty(10)
# print(ar2)

a3 = numpy.eye(8,6,0)
# print(a3)

# 주대각선 방향이 1인 3*3 정방 행렬 생성
a4 = numpy.eye(3, k=1)
# print(a4)
# 행렬에서 주 대각선의 데이터만 골라서 배열을 생성
# print(numpy.diag(a4))

# 데이터 타입 확인과 형변환
ar4 = numpy.array([1,"2", 3]) # 숫자와 문자열을 가지고 배열을 생성 - 문자
# print(ar4)
# print(ar4.dtype)

ar5 = numpy.array([1, 2.3, 3]) # 숫자와 문자열을 가지고 배열을 생성 - 문자
# print(ar5)
# print(ar5.dtype)

# ar 배열의 자료형을 정수로 변환
ar6 = ar5.astype(numpy.int32)
# print(ar6)
# print(ar6.dtype)

# 0부터 19까지 숫자를 가지고 1차원 배열 생성
ar7 = numpy.arange(20)
# print(ar7)

# ar를 4*5 짜리 2차원 배열로 변환
# matrix = ar7.reshape((4,5))
matrix = ar7.reshape((4,-1))
# 5 대신에 -1을 대입해도 결과는 동일
# print(matrix)

#다차원 데이터를 1차원으로 변환
br = matrix.reshape(-1)
# print(br)

br2 = matrix.flatten()
# print(br2)

#배열에서 하나의 요소에 접근
ar8 = numpy.arange(10)
ma = ar8.reshape((2,-1))
print(ar8)
print(ma)

# 1차원 배열에서 요소에 접근
# print(ar8[0]) #첫번째 데이터
# print(ar8[-1]) # 마지막 데이터
# 2차원 배열에서 요소 접근
# print(ma[1,2])
# print(ma[1][2])

# print(ar8[1:4])
# print(ar8[5:])
# print(ar8[:4])
# print(ar8[:])

print(matrix[1][1:3]) # [6 7]
print(matrix[1]) # [5 6 7 8 9]
print(matrix[:,1]) # [ 1  6 11 16]

# [0 1 2 3 4 5 6 7 8 9]
# [[0 1 2 3 4]
#  [5 6 7 8 9]]
