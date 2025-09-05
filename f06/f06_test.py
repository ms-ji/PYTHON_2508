def main():
    """
    
    """
    # 1부터 1000까지 자연 수 중 3의 배수의 합을 구하세요.
    count = 0
    for i in range(1,1001):
        if i % 3 != 0:
            continue
        count += i
    print(f'결과값:{count}') #결과값:166833

    # 숫자를 입력 받아 팩토리알 계산
    # 입력된 숫자가 음수가 아니면 팩토리알 계산

    while True:
        num = int(input('양의 정수를 입력하세요(0을 입력하면 종료:'))
        if num < 0:
            print(f'{num}양수를 입력하세요.')
            continue
        if num == 0:
            print('프로그램을 종료합니다.')
            break
        factorial = 1
        for i in range(1, num+1):
            factorial*=i

        print(f'{num}!={factorial}')









if __name__ == '__main__':
    main()
