class Dog:
    # 클래스 속성
    shared_value = 14

    def __init__(self,name,age):
        '''
        생성자
        :param name:
        :param age:
        '''
        #속성
        self.name = name
        self.age = age
    def bark(self):
        print(f'{self.name}가 짓습니다.')

    def info(self):
        print(f'{self.name}는 {self.age}살 입니다.')



def main():
    """
    
    """
    dog1 = Dog('멍멍이',2)
    print(dog1) #<__main__.Dog object at 0x0000023659C36F90>
    print(type(dog1)) #<class '__main__.Dog'>

    dog1.bark()
    dog1.info()

    dog2 = Dog('바둑이',3)
    dog2.info()

    print(Dog.shared_value)
    print(dog1.shared_value)
    print(dog2.shared_value)
    # shared_value = 16
    Dog.shared_value = 16
    print(Dog.shared_value)
    print(dog1.shared_value)
    print(dog2.shared_value)

if __name__ == '__main__':
    main()
