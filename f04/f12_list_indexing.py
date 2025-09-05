def main():
    """
    인덱싱은 리스트에서 특정 위치에 있는 데이터를 가져오는 방법으로, 데이터에는 고유한 인덱스가 있습니다.

    """
    mixed_list =[18,14,16,['A', 'B', 'C']]
    print(f'mixed_list[-1]:{mixed_list[-1]}') # ['A', 'B', 'C']
    print(f'mixed_list[-1]:{mixed_list[-1][1]}') # B

    tripe_list = [1,2,['A', 'B', ['LIFE','GOOD']]]

    print(f'tripe_list[-1][-1][0]:{tripe_list[-1][-1][0]}') #LIFE

if __name__ == '__main__':
    main()
