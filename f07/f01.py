def square(x):
    '''
    x의 제곱
    :param x:
    :return:
    '''
    return x*x
def high_order_func(func,value):
    return func(value)

result = high_order_func(square,3)
print(f'result:{result}') #9