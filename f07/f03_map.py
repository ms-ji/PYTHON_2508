#정수 리스트의 제곱 구하기

nums = [1,2,3,4,5]
#iterable의 각 요소에 함수를 적용하여 새로운 iterable을 생성
#map(function,iterable)

square = list(map(lambda x:x**2,nums))

print(f'square: {square}')
#square: [1, 4, 9, 16, 25]