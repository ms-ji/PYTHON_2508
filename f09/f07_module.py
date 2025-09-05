import sys
import os

def main():
    target_path = 'D:\\my_python_libs'
    sys.path.append(target_path)

    print("[*] sys.path에 추가된 경로:", target_path)

    module_path = os.path.join(target_path, 'mymodule.py')
    print("[*] mymodule.py 실제 존재 여부:", os.path.exists(module_path))

    import mymodule
    print("[*] 모듈 import 성공!")
    print("더하기 결과:", mymodule.substract(3, 4))

if __name__ == '__main__':
    main()
