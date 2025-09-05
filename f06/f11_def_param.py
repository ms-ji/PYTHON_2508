def greet(name='사용자'):
    '''
    기본값 매개 변수
    :param name:
    :return:
    '''
    print(f'안녕하세요, {name}님')


def main():
    """
    
    """
    greet() # 기본값 매개변수 사용
    greet('영히') # 메개변수 전달

if __name__ == '__main__':
    main()
