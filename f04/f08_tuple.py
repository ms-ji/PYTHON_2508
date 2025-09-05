def main():
    """
    - 정의 : 순서가 있고, **변경이 불가능**하며, 중복을 허용하는 컬렉션
    - 기호 : ( ) 소괄호
    """
    colors = ('Red','Blue','Green')
    print(f'colors[1]:{colors[1]}') #Blue

    #colors[1] = 'black' TypeError -> 바꿀 수 없음

if __name__ == '__main__':
    main()
