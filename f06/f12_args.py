def add_numbers(*args):
    '''
    여러 값을 튜플로 전달
    :param args:
    :return:
    '''
    return sum(args)

def main():
    """
    
    """
    print(add_numbers(14,14)) #28
    print(add_numbers(14, 14,30)) # 58

if __name__ == '__main__':
    main()
