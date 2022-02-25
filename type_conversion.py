##### 자료형
# 04. 형변환

print(int(3.8))

# floating point
print(float(3))

# 문자열 2 → 정수형 2, 문자열 5 → 정수형 5로 바뀜
print(int("2") + int("5"))

print(float("1.1") + float("2.5"))

# 정수형 2 → 문자열 2, 정수형 5 → 문자열 5
print(str(2) + str(5))

age = 7
print("제 나이는 " + str(age) + "살입니다.")

# Error - 형변환을 할때 논리적으로 합당한지 생각해봐야함
# print(int("Hello World!"))