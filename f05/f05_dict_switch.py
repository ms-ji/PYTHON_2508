def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y



def main():
    """
    딕셔너리로 스위치 기능 구현
    """
    #함수를 딕셔너리에 할당
    operation = {
        "add":add,
        "subtract":subtract
    }

    result = operation['add'](14,16)
    print(f'result: {result}')

    result = operation['subtract'](14,16)
    print(f'result: {result}')

if __name__ == '__main__':
    main()
