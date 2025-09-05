def main():
    """
    [ 표현식 for 항목 in 반복 가능한 객체 if 조건문 ]
    """
    numbers = [1,2,3,4,5]
    squares = [i*i for i in numbers]
    print(f'numbers:{numbers}') #[1, 2, 3, 4, 5]
    print(f'squares:{squares}') #[1, 4, 9, 16, 25]

    print("#"*53)

    # 1에서 10사이의 짝수를 담기
    squares1 = [i for i in range(10) if i % 2 == 0]
    print(f'squares:{squares1}') #[0, 2, 4, 6, 8]

    # 2차원 리스트 내포
    # 출력 : [[1,2,3,],[2,4,6],[3,6,9]]
    # [j for j in range(1,4)] -> [1, 2, 3]
    matrix = [[i*j for j in range(1,4)] for i in range(1,4)]
    print(matrix) # [[1, 2, 3], [2, 4, 6], [3, 6, 9]]


if __name__ == '__main__':
    main()
