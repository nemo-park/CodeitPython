##### 자료형
# 01. 숫자형

# e = 10의 x승 개념
print(0.0025e3)
print(250e-2)

# 덧셈 - 정수형
print("덧셈----------")
print(4 + 7)
# 덧셈 - 소수형
print(4.0 + 7.0)
# Python 에서는 소수형이 정수형보다 힘이 더 쎄다!
print(4 + 7.0)

print("뺄셈----------")
print(2 - 4)
print(2.0 - 4.0)

print("곱셈----------")
print(5 * 3)

print("나머지----------")
print(7%3)

print("몫 구하기----------")
print(7//3)
# floor division (버림 나눗셈)
print(7 // 2)
print(8 // 3)
# 둘 중 하나가 소수형이면 결과값도 소수형으로 출력됨
print(8.0 // 3)
print(8.0 // 3.0)

print("거듭제곱----------")
print(2 ** 3)
print(2 ** 5)

# 나눗셈은 정수(Integer)/소수(Floating Point) 무관하게 결과는 소수형으로 출력됨
print("나눗셈----------")
print(7 / 2)
print(6 / 2)
print(7.0 / 2)
print(6.0 / 2.0)

print("사칙연산----------")
print(2 + 3 * 2)
print(2 * (2 + 3))


# round (반올림)
print(round(3.1415926535))
print(round(3.1415926535, 2))
print(round(3.1415926535, 4))