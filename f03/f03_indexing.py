def main():
    """
    문자열 인덱싱은 문자열에서 특정 위치에 있는 문자를 가져오는 방법
    """
    text = 'Python'

    #양의 인덱스
    print(f'text[0]:{text[0]}')
    print(f'text[2]:{text[2]}')

    #음의 인덱스
    print(f'text[-1]:{text[-1]}')

    #################################
    # 슬라이싱
    text = "Python Programming"
    print(f'text[0:6]:{text[0:6]}')

    #시작 번지 생략 : 0번지부터 시작
    print(f'text[:6]:{text[:6]}')

    #끝 인덱스 생략
    print(f'text[7:]:{text[7:]}')

    #시작과 끝 모두다 생략 -> 문자열 전체
    print(f'text[:]:{text[:]}')

    #간격 지정
    print(f'text[:12:2]:{text[:12:2]}')

if __name__ == '__main__':
    main()
