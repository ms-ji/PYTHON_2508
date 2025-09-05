def main():
    """
    &	AND	a & b	1
    |	OR	a | b	1
    ^	XOR	a ^ b	6
    ~	NOT	~a	-6
    <<	왼쪽 시프트	a << 1	10
    >>	오른쪽 시프트	a >> 1	2
    """

    a = 5 #0101
    b = 3 #0011

    print(a>>1) #0010 -> 2
    print(a&b) #True(1)
    print(a & b << 1) # 4
    print(a & b >> 1)  # 1

if __name__ == '__main__':
    main()
