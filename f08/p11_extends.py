class Animal:
    def speak(self):
        print('동물이 소리를 냅니다.')
#자식 클래스 정의(Animal 상속)
class Dog(Animal):
    def bark(self):
        print('멍멍')

def main():
    #객체 생성
    dog01 = Dog()
    dog01.speak() #부모 클래스 메서드 호출
    dog01.bark() #자식 클래스 메서드 호출


if __name__ == '__main__':
    main()
