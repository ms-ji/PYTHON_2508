from functools import reduce
#1~20까지의 정수 중에서 짝수만 골라 제곱한 결과의 합을 구하시오.

# 1. 1~20사이 정수
numbers = list(range(1,21))
print(numbers)
#[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

# 2. filter : 짝수만 고르기
evens = list(filter(lambda x:x%2==0,numbers))
print(evens)
#[2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# 3. map : 제곱한 새로운 리스트 생성
squares = list(map(lambda x:x**2,evens))
print(squares)

# 4. reduce 제곱한 합계 구하기
result = reduce(lambda x,y:x+y,squares)
print(f'result:{result}') #result:1540
