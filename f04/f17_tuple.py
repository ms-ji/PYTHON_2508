def get_min_max(numbers):
	return min(numbers), max(numbers)

def main():
    """
    
    """
    single_element =(5,)
    print(type(single_element)) #<class 'tuple'>
    single_element = (5)
    print(type(single_element)) #<class 'int'>
    #####################################################
    print("*"*53)

    # 인덱싱
    fruits = ('사과','바나나','체리',99)
    print(fruits[0]) #사과
    print(fruits[-1]) #99

    # 슬라이싱
    nums = (1,2,3,4,5,6,7,8)
    print(f'nums[1:4]:{nums[1:4]}')
    print(f'nums[0:]:{nums[0:]}')
    print(f'nums[:9]:{nums[:9]}')
    print(f'nums[::-1]:{nums[::-1]}')

    print(f'nums.count(2):{nums.count(2)}')
    print(f'nums.index(3):{nums.index(3)}')

    print(f'{get_min_max(nums)}') #(1, 8)



if __name__ == '__main__':
    main()
