def main():
    """
    append(x)	리스트 끝에 요소 추가	lst.append(10)
    extend(iterable)	리스트에 다른 리스트나 iterable 요소 추가	lst.extend([20, 30])
    insert(i, x)	특정 위치 i에 요소 삽입	lst.insert(1, "hello")
    remove(x)	첫 번째로 등장하는 요소 x 삭제	lst.remove(10)
    pop([i])	특정 위치 i의 요소를 제거하고 반환 (기본: 마지막)	lst.pop()
    index(x)	요소 x의 첫 번째 인덱스 반환	lst.index("apple")
    count(x)	요소 x의 개수 반환	lst.count(3)
    sort()	리스트를 오름차순으로 정렬	lst.sort()
    reverse()	리스트를 역순으로 정렬	lst.reverse()
    clear()	모든 요소 제거	lst.clear()
    """
    # 리스트
    numbers = [1,2,3,4,5,6,7]

    numbers.append(88)
    print(numbers) #[1, 2, 3, 4, 5, 6, 7, 88]

    #값 변경
    numbers[0]=99
    print(numbers) #[99, 2, 3, 4, 5, 6, 7, 88]

    #삭제
    numbers.remove(2) #중복된 숫자일 경우 앞의 수 삭제
    print(numbers) #[99, 3, 4, 5, 6, 7, 88]

    del numbers[-1]
    print(numbers) #[99, 3, 4, 5, 6, 7]

    #리스트 끝 요소 꺼내기
    print(f'리스트 끝 요소 꺼내기: {numbers.pop()}')

    # 오름차순 정렬
    print(f'sort: {numbers.sort()}')
    print(numbers) #[3, 4, 5, 6, 99]
    # 역순 정렬
    print(f'reverse: {numbers.reverse()}')
    print(numbers) #[99, 6, 5, 4, 3]

    # 리스트 확장
    x =[1,2,3]
    x.extend([4,5])
    print(x) #[1, 2, 3, 4, 5]


if __name__ == '__main__':
    main()
