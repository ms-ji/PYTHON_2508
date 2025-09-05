def main():
    """
    set자료형에 저장된 값을 인덱싱으로 접근 하려면
    리스트나 튜플로 변환 후 해야 함.
    """
    s01 = set([14,15,19])
    print(f's01: {s01}, type:{type(s01)}')
    #s01: {19, 14, 15}, type:<class 'set'>

    tmp_list = list(s01)
    print(f'tmp_list: {tmp_list}, type:{type(tmp_list)}')
    #tmp_list: [19, 14, 15], type:<class 'list'>

    tmp_list[0]=15
    print(f'tmp_list: {tmp_list}, type:{type(tmp_list)}')
    #tmp_list: [15, 14, 15], type:<class 'list'>

    tmp_set = set(tmp_list)
    print(f'tmp_set: {tmp_set}, type:{type(tmp_set)}')
    #tmp_set: {14, 15}, type:<class 'set'>

    tmp_tuple = tuple(tmp_set)
    print(f'tmp_tuple[1]:{tmp_tuple[1]} ')
    print(f'tmp_tuple: {tmp_tuple}, type:{type(tmp_tuple)}')
    # tmp_tuple: (14, 15), type:<class 'tuple'>

    s01 = set(tmp_tuple)
    print(f's01: {s01}, type:{type(s01)}')
    #s01: {14, 15}, type:<class 'set'>

if __name__ == '__main__':
    main()
