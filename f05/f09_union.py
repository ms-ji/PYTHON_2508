def main():
    """
    
    """
    a = set([1,2,3,4,5])
    b = set([4,5,6])

    # 합집합(Union)
    union1 = a.union(b)
    print(f'a|b: {a|b}') #{1, 2, 3, 4, 5, 6}
    print(f'union1:{union1} type: {type(union1)}')
    #union1:{1, 2, 3, 4, 5, 6} type: <class 'set'>


    # 교집합(Intersection)
    intersec = a.intersection(b)
    print(f'a & b: {a & b}')  #{4, 5}
    print(f'intersec:{intersec} type: {type(intersec)}')
    #intersec:{4, 5} type: <class 'set'>

    # 차집합(Difference)
    diff = a.difference(b)
    print(f'a - b: {a - b}')  #{1, 2, 3}
    print(f'diff:{diff} type: {type(diff)}')
    # diff:{1, 2, 3} type: <class 'set'>

    # 대칭 차집합()
    s_diff = a.symmetric_difference(b)
    print(f'a^b: {a ^ b}')  # {1, 2, 3, 6}
    print(f's_diff:{s_diff} type: {type(s_diff)}')
    #s_diff:{1, 2, 3, 6} type: <class 'set'>



if __name__ == '__main__':
    main()
