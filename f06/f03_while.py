def main():
    """
    
    """
    i =1
    while i <= 5:
        print(i)
        i = i+1
    print("#"*54)

    count = 5
    while count > 0:
        print(count)
        count -= 1
    else:
        print('카운트 다운 종료 @!')
    print("#"*54)

    n = 12
    for i in range(2,n):
        if n%i == 0:
            print(f'{n}은 소수가 아닙니다.')
            break
    else:
        print(f'{n}은 소수가 입니다.')


if __name__ == '__main__':
    main()
