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



if __name__ == '__main__':
    main()
