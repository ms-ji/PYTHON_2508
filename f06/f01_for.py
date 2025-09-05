def main():
    """
    
    """
    fruits =['사과','바나나','복숭아']

    for fruit in fruits:
        print(fruit,sep=" ",end="\t")

    print("#"*53)
    # 문자열 반복
    text = "Python"

    for char in text:
        print(char)
    print("#"*53)

    #
    user_list = [(1,19),(2,16),(3,14)]
    print(type(user_list)) # <class 'list'>

    for (first,last)in user_list:
        print(first ,",",last)
    print("#"*53)

    #range()
    for i in range(1,11):
        print(i,end=",") #1,2,3,4,5,6,7,8,9,10,
    print("\t")

    for i in range(10,0,-1):
        print(i,end=",") #10,9,8,7,6,5,4,3,2,1,
    print("\t")

    #list()와 함께 사용
    numbers = list(range(1,11))
    print(numbers) #[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

if __name__ == '__main__':
    main()
