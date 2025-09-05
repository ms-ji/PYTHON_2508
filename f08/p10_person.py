class Person:
    #클래스 변수
    count = 0

    #생성자
    def __init__(self,name):
        # 인스턴스 변수
        self.name = name

    #인스턴스 메서드
    def introduce(self):
        print(f'안녕하세요.저는 {self.name}입니다.')

    # 클래스 메서드
    @classmethod
    def how_many(cls):
        print(f'현재 인원수:{cls.count}명')

def main():
    """
    
    """
    p01 = Person('철수')
    p02 = Person('영희')
    p01.introduce()
    p02.introduce()

    Person.how_many()


if __name__ == '__main__':
    main()
