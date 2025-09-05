def main():
    """
    수를 입력 받다가 0이면 종료
    """
    while True:
        num = int(input('숫자를 입력 하세요.(0을 입력하면 종료):'))

        if num == 0:
            print('종료 합니다.')
            break
        print(f'입력한 숫자:{num}')





if __name__ == '__main__':
    main()
