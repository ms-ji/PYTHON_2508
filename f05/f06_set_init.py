def main():
    """
    집합(Set) 생성
    """
    s01 = {1,2,2,3}
    print(f's01: {s01}, type: {type(s01)}') #s01: {1, 2, 3}, type: <class 'set'>

    #set()
    s02 = set([1,2,2,3,4,5])
    print(f's02: {s02}, type: {type(s02)}') #s02: {1, 2, 3, 4, 5}, type: <class 'set'>

    #{}
    emp_set = set()
    print(f'emp_set: {emp_set}, type: {type(emp_set)}') #emp_set: set(), type: <class 'set'>

    empty_dict = {}
    print(type(empty_dict)) #<class 'dict'>

    s03 = set('Hello')
    print(s03) #{'e', 'H', 'l', 'o'}

if __name__ == '__main__':
    main()
