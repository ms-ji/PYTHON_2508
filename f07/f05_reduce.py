from functools import reduce

# 리스트 요소의 합계 구하기
nums = [1,2,3,4,5]

total = reduce(lambda x,y:x+y,nums)
print(f'total: {total}') # 15

# 초기값을 10으로 누적
new_total = reduce(lambda x,y:x+y,nums,10)
print(f'new_total: {new_total}') #25

