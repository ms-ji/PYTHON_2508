def main():
    """
    불리언(논리 값)
    """
    is_happy = True
    is_sad = False
    print(type(is_happy)) #<class 'bool'>
    print(type(is_sad)) #<class 'bool'>

    #####################################
    x = True
    y = False
    print(x and y) #False
    print(x or y) #True
    print(not x) #False
    print(not y) #True
    #####################################
    print(True+1) #2
    print(False+1) #1

if __name__ == '__main__':
    main()
