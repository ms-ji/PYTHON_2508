def main():
    """
    
    """
    empty_list = []
    numbers_list = [1,2,3,3,4,5]
    string_list = ['banana','apple','water melon']
    mixed_list = numbers_list+string_list

    list_inner = [1,2,3,['A','B','C']]

    print("*"*53)
    print(f'empty_list: {empty_list}')
    print(f'numbers_list: {numbers_list}')
    print(f'string_list: {string_list}')
    print(f'mixed_list: {mixed_list}')
    print(f'numbers_list+string_list: {numbers_list+string_list}')
    print("*" * 53)

    print(f'list_inner[3]:{list_inner[3]}') # ['A', 'B', 'C']
    print(f'list_inner[3][0]:{list_inner[3][0]}') # A
    print(f'list_inner[2]:{list_inner[2]}') # 3

if __name__ == '__main__':
    main()
