def main():
    """
    리스트 컴프리헨션(List Comprehension)은 기존 리스트나 이터러블을 기반으로
    새로운 리스트를 간결하고 효율적으로 생성하는 문법 입니다.
    """

    for x in range(1,6):
        print(x**2)

    # 1~5 까지 각각의 숫자를 제곱한 리스트 생성
    seq = [x**2 for x in range(1,6)]
    print(f'seq:{seq}') #[1, 4, 9, 16, 25]

    # 1부터 10사이 짝수만 리스트로 생성
    seq_if = [x for x in range(1,11) if x%2 == 0]
    print(f'seq_if:{seq_if}') #[2, 4, 6, 8, 10]


if __name__ == '__main__':
    main()
