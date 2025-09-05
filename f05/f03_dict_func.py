def main():
    """
    
    """
    person = {'name':' 영희','age':25,'city':'Seoul'}

    # 모든 키 조회 keys()
    person.keys()
    print(person.keys()) #dict_keys(['name', 'age', 'city'])

    # 모든 값 조회 values()
    person.values()
    print(type(person.values())) #<class 'dict_values'>

    # items()
    print(f'person.items(): {person.items()}')
    print(f'person.items(): {type(person.items())}') #<class 'dict_items'>

    # 반복문
    for key in person.keys():
        print(f'key:{key}, value:{person[key]}')

    # 해당 key가 딕셔너리에 있는지 확인
    is_name_in = 'name' in person
    print(f'is_name_in: {is_name_in}') #True

if __name__ == '__main__':
    main()
