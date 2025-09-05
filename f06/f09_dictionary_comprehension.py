def main():
    """
    Dictionary Comprehension
    """
    nums = [1,2,3,4]
    #{1 : 1, 2 : 4,3 : 9,4 : 16}

    square_dict = { x:x*x for x in nums }
    print(f'square_dict:{square_dict}')
    #square_dict:{1: 1, 2: 4, 3: 9, 4: 16}

    # 집합 내포(Set Comprehension)
    # 1~ 10 중 3의 배수의 제곱
    square_set = {x for x in range(1,11) if x % 3 == 0}
    print(f'square_set:{square_set}') #{9, 3, 6}

if __name__ == '__main__':
    main()
