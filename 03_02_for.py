# range
# 장점 : 간편함, 깔끔함, 메모리 효율성(1 쓰고 버리고 2 쓰고 버리고 등)

# for i in range(start, stop):
#     print(i)
# → start 부터 stop-1 까지의 범위

for i in range(3, 11):
    print(i)

print()

# 파라미터 1개 버전
# for i in range(stop):
#     print(i)
# → 0 부터 stop-1 까지의 범위

for i in range(10):
    print(i)

numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]

# 인덱스와 원소 출력
for i in range(len(numbers)):
    print(i, numbers[i])

print()

# 파라미터 3개 버전
# for i in range(start, stop, step):
#     print(i)
# → 0 부터 stop-1 까지의 범위

for i in range(3, 17, 3):   # 3 ~ 16
    print(i)


# 리스트 뒤집기
numbers = [2, 3, 5, 7, 11, 13, 17, 19]
numbers = [2, 3, 5, 7, 11, 13, 17, 19]

# 리스트 뒤집기
for left in range(len(numbers)):
    # 인덱스 left와 대칭인 인덱스 right 계산
    right = len(numbers) - left - 1

    # 위치 바꾸기
    temp = numbers[left]
    numbers[left] = numbers[right]
    numbers[right] = temp

print("뒤집어진 리스트: " + str(numbers))
