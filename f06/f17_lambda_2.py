students = [("홍길동",90),("김철수",80),("이영희",85)]
print(students) #[('홍길동', 90), ('김철수', 80), ('이영희', 85)]
students.sort(key = lambda x : x[1])
print(students) #[('김철수', 80), ('이영희', 85), ('홍길동', 90)]


numbers = [1,2,3,4,5,6]
even_numbers = list(filter(lambda x : x%2==0,numbers))
print(even_numbers) #[2, 4, 6]