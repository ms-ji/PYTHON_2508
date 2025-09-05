def main():
    """
    변수
    """
    #변수명 : 영문, 숫자, _ 사용 가능
    #시작은 : 영문자 또는 언더바(_)
    valid_name = 10
    _name = "이상무"
    #5name = "error"
    Name = "이상무"
    name = "Alice"

    print(Name)
    print(name)

    ########################
    #my-name = "error"
    #my name = "error"
    #한글 변수 선언 가능 : 현장에서 사용하진 않는다.
    이름 = "이상무"
    print(이름)

    #여러 변수 한 번에 할당
    x = y =z =100
    print(x)
    print(y)
    print(z)

    a,b,c =1,2,3
    print(a)
    print(b)
    print(c)

    #type()
    name="이상무"
    age=22
    height = 178.8

    print(type(name)) #<class 'str'>
    print(type(age)) #<class 'int'>
    print(type(height)) #<class 'float'>

    #상수
    PI = 3.141592
    MAX_USERS = 20
    #PI = '파이'
    print(PI) #3.141592
    print(MAX_USERS) #20

if __name__ == '__main__':
    main()


