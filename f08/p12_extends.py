class Animal:
    def speak(self):
        print('동물이 소리를 냅니다.')

#자식 클래스 정의(Animal 상속)
class Dog(Animal):
    def speak(self):
        super().speak() #부모 메서드 호출
        print('멍멍')

def main():
    dog01 = Dog()
    dog01.speak()
    #동물이 소리를 냅니다.
    #멍멍

if __name__ == '__main__':
    main()
