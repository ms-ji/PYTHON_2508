def main():
    """
    is	동일한 객체인가?	a is b	FALSE
    is not	동일한 객체가 아닌가?	a is not b	TRUE
    """
    a = 14
    b = 16
    c = "4"
    d = "4"

    print(f'a is b: {a is b}') #False
    print(f'a is not b: {a is not b}') #True

    print(f'c is d: {c is d}') #True


if __name__ == '__main__':
    main()
