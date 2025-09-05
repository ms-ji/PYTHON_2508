def main():
    """
    
    """
    s01 = set([13,14,15])

    #요소 추가 : add
    s01.add(15)
    print(f's01: {s01}')

    # 여러 요소 추가
    s01.update([15,16,17])
    print(f's01: {s01}')

    # 요소 삭제
    s01.remove(17)
    # s01.remove(99) -> KeyError
    print(f's01: {s01}')

    # 요소 삭제 : 예외 미발생
    s01.discard(16)
    s01.discard(99) # 오류 미발생
    print(f's01: {s01}')


if __name__ == '__main__':
    main()
