def main():
    """
    
    """
    name = "이상무"
    greeting = '즐겨운 목요일 2일 전'

    print(type(name)) #<class 'str'>
    print(type(greeting)) #<class 'str'>

    full_name = "이" + " " + "상무"
    print(full_name) #이 상무

    ##문자열 반복##
    repeated="HI" * 10
    print(type(repeated)) #<class 'str'>
    print(repeated) #HIHIHIHIHIHIHIHIHIHI
    print("-"*50) #--------------------------------------------------

    ##문자열 슬라이싱##
    text="Python"
    print(text[0]) #첫 번쨰 문자 : P
    print(text[-1]) #마지막 문자 : n
    print(text[1:4]) #부분 문자열 : yth (n:m-1)까지 추출한다.


if __name__ == '__main__':
    main()
