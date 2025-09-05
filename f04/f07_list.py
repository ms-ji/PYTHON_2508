def main():
    """
    순서가 있고, 변경 가능하며, 중복을 허용하는 컬렉션
    [] 대괄호 사용
    """
    fruits =['사과','바나나','체리',14]
    print(fruits) #['사과', '바나나', '체리', 14]
    print(f'fruits[2]:{fruits[2]}') #체리

    #값을 변경
    fruits[1] = '오렌지'
    print(f'fruits[1]:{fruits[1]}') #오렌지

if __name__ == '__main__':
    main()
