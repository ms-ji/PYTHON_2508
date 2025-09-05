from tokenize import String


def main():
    """
    
    """

    while True:
        num =int(input('숫자를 입력하세요.(0을 입력하면 종료됩니다):'))

        if num >= 10:
            print('9단 이하 입력 하세요.')
            continue
        if num == 0:
            print('프로그램을 종료합니다.')
            break
        max_width = num
        for i in range(1, num+1):
            word = str(i)
            print(f'{word*i:>{max_width}}')
            #print(" "*int(num-i)+word*i)






if __name__ == '__main__':
    main()
