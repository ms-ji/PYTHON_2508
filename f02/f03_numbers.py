def main():
    """
    
    """
    #복소수
    z = 2+3j
    print(type(z))

    ################################################
    #진수 표현 (2진수 0b, 8진수 0, 16진수 0x)

    #2진수를 10진수로 출력
    binary_number = 0b101010
    print('2진수: 0b101010 -> ',binary_number)
    # 8진수를 10진수로 출력
    octal_number = 0o134
    print('8진수: 0o134 -> ', octal_number)
    # 16진수를 10진수로 출력
    hexa_number = 0x1f
    print('16진수: 0x1f -> ', hexa_number)

if __name__ == '__main__':
    main()
