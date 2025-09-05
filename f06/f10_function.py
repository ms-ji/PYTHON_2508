def greet():
    print("hello")

greet() #hello


def greet(name):
    print(f'안녕하세요,{name}님')

greet('이상무')

#반환값 사용
def add(a,b):
    return a+b

result = add(14,16)
print(f'result:{result}') #result:30

# 여러 개의 반환값
def add_and_substract(x,y):
    '''

    :param x:
    :param y:
    :return: x+y, x-y
    '''
    return x+y,x-y

add_result,sub_result = add_and_substract(6,7)
print(f'add_result:{add_result}') # 13
print(f'sub_result:{sub_result}') # -1



