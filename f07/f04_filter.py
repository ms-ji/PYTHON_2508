#짝수만 필터링
nums = [1,2,3,4,5,6]

evens=list(filter(lambda x:x%2 ==0,nums))

print(f'evens: {evens}')
#evens: [2, 4, 6]
