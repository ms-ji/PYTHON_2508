def main():
    """
    
    """
    with open(file='q2.txt',mode='r',encoding='utf-8') as f:
        num_str = f.read()  # '10,20,30,40,50'
        num_list = [int(n) for n in num_str.split(',')]
        print(num_list)

        #합계
        print(f'합계는 {sum(num_list)}')
        print(f'평균은 {sum(num_list)/ len(num_list)}')
        print(f'최대 값은 {max(num_list)}')
        print(f'최소 값은 {min(num_list)}')

if __name__ == '__main__':
    main()
