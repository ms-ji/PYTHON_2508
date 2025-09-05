def main():
    """
    
    """

    #f =open('없는 파일.txt','r')

    try:
        result = 10/0 #ZeroDivisionError
    except ZeroDivisionError as e:
        print(f'0으로 나눌 수 없습니다. e:{e}')
        #0으로 나눌 수 없습니다. e:division by zero

if __name__ == '__main__':
    main()
