# 리스트 (list)
numbers = [2, 3, 5, 7, 11, 13]

# 1. Indexing
print(numbers[0])
print(numbers[-1])

# 2. 리스트 슬라이싱 (List slicing)
# index 0 ~ 3
print(numbers[0:4])

# index 2 ~ 맨 마지막
print(numbers[2:])

# index 맨 앞 ~ 2
print(numbers[:3])

new_list = numbers[:3]  # [2. 3. 5]
print(new_list[2])      # 5

# 3. 크기 확인
numbers[0] = 7
print(numbers)
print(len(numbers))

# 4. 추가/삭제
names = []
# 추가연산 : 무조건 오른쪽 끝에 insert
names.append("태훈")
names.append("서호")
names.append("연수")
names.append("응")

print(names)
print(len(names))

del (names[3])
print(names)

# 삽입연산
names.insert(2, "웅")
print(names)

# 5. 리스트 정렬
# 1) sorted : 기존 리스트는 건드리지 않고, 정렬된 새로운 리스트를 리턴
print(numbers)
new_list = sorted(numbers)
print(new_list)
new_rev_list = sorted(numbers, reverse=True)
print(new_rev_list)
print(numbers)

# 2) sort : 아무것도 리턴하지 않고, 기존 리스트를 정렬
print("sort() 전: ")
print(numbers)
numbers.sort()
print(numbers)

numbers.sort(reverse=True)
print(numbers)


# 6. 리스트에서 값의 존재 유무 확인하기
# 값의 존재를 확인
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23]
print(7 in primes)  # True
print(12 in primes) # False

# 값이 없는지 확인
print(7 not in primes)  # False
print(12 not in primes)


# 7. 리스트 안의 리스트 (Nested List)
# 세 번의 시험을 보는 수업
grades = [[62, 75, 77], [78, 81, 86], [85, 91, 89]]

# 첫 번째 학생의 성적
print(grades[0])

# 세 번째 학생의 성적
print(grades[2])

# 첫 번째 학생의 첫 번째 시험 성적
print(grades[0][0])

# 세 번째 학생의 두 번째 시험 성적
print(grades[2][1])

# 첫 번째 시험의 평균
print((grades[0][0] + grades[1][0] + grades[2][0]) / 3)


# 8. reverse 메소드
# some_list.reverse()는 some_list의 원소들을 뒤집어진 순서로 배치합니다.
numbers = [5, 3, 7, 1]
numbers.reverse()
print(numbers)

# 9. index 메소드
# some_list.index(x)는some_list에서 x의 값을 갖고 있는 원소의 인덱스를 리턴해줍니다.
members = ["영훈", "윤수", "태호", "혜린"]
print(members.index("윤수"))
print(members.index("태호"))


# 10. remove 메소드
# some_list.remove(x)는some_list에서 첫 번째로 x의 값을 갖고 있는 원소를 삭제해줍니다.
fruits = ["딸기", "당근", "파인애플", "수박", "참외", "메론"]
fruits.remove("파인애플")
print(fruits)