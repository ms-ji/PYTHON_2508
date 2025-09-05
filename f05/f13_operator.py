def main():
    """
    
    """
    # 삼항 연산자
    score = 88
    result = '합격' if score > 60 else '불합격'
    print(f'result: {result}')  # 합격

    fruits = ['블루베리','복숭아','바나나']
    print(f'fruits: {fruits}') #['블루베리', '복숭아', '바나나']

    if '복숭아' in fruits:
        print(f'리스트에 복숭아가 있습니다.')

    if '사과' not in fruits:
        print(f'리스트에 사과가 없습니다.')

    # 논리 연산자
    age = 25
    is_employed = False

    if age > 18 or is_employed:
        print('성인이면 작업이 있습니다.')

    if not is_employed:
        print('작업이 있습니다.')

if __name__ == '__main__':
    main()
