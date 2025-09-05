def main():
    """
    리스트 더하기(+) : 리스트 합치기
    """
    num_lows = [1,2,3]
    num_high =[4,5,6]

    print(f'num_lows+num_high:{num_lows+num_high}') #[1, 2, 3, 4, 5, 6]
    print("*"*52)

    #리스트 반복
    print(f'num_lows*3: {num_lows*3}')
    # print(f'num_lows*num_high:{num_lows*num_high}') : TypeError

if __name__ == '__main__':
    main()
