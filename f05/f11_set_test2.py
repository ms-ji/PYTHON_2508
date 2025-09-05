def main():
    """
    
    """
    # 추첨 결과: [3, 5, 12, 17, 23, 38]
    # 사용자 입력 번호: [5, 8, 12, 13, 23, 42]

    result = set([3, 5, 12, 17, 23, 38])
    input_num = set([5, 8, 12, 13, 23, 42])

    my_result = result & input_num;
    print(f'맞은 번호:{my_result}')
    print(f'맞은 개수:{len(my_result)}')

if __name__ == '__main__':
    main()
