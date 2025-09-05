def main():
    """
    - 정의 : 순서가 없고, 중복을 허용하지 않으며, 변경이 가능한 컬렉션
    - 기호 : { }  중괄호
    """
    numbers ={1,2,3,3}
    print(f'numbers:{numbers}') #{1, 2, 3}

    numbers.add(4)
    print(f'numbers:{numbers}') #{1, 2, 3, 4}


if __name__ == '__main__':
    main()
