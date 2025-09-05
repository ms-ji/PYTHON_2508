def main():
    """
    
    """
    try:
        num = int(input('숫자를 입력하세요>'))
        print(f'1')
        result = 10/num
        print(f'2')
    except ZeroDivisionError as e:
        print(f'ZeroDivisionError \n{e}')
    except ValueError as e:
        print(f'숫자만 입력 가능\n{e}')
    except Exception as e:
        print(f'Exception \n{e}')
    else:
        # 정상 종료되면 수행
        print(f'결과:{result}')
    finally:
        print('프로그램 종료')


if __name__ == '__main__':
    main()
