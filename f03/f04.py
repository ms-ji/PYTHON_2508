def main():
    """
    리터럴
    """
    # 멀티 라인
    multiline = ''' 이것은 문자열 입니다 
    여러줄에 걸쳐 작성 됩니다.
    '''
    print(f'multiline:{multiline}')
    print('#'*54)

    # Escape 문자
    new_line = "Hello\nWord"  # 줄바꿈
    tap_space = "Hello\tWord"  # 탭
    quote = "He said. \'Hello\'"  # 작은 따옴표 출력

    print(f'new_line:\n{new_line}')
    print(f'tap_space:\n{tap_space}')
    print(f'quote:\n{quote}')
    print('#' * 54)

    # 진수 표현
    binary = 0b1010  # 10
    octal = 0o12 #10
    hexadecimal = 0xA  # 10
    print(f'binary:{binary}')
    print(f'octal:{octal}')
    print(f'hexadecimal:{hexadecimal}')


if __name__ == '__main__':
    main()
