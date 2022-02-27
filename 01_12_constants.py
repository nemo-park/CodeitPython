# 상수 (constant)
# 네이밍규칙 : 대문자
#   1. 일반 변수와 상수를 쉽게 구분 짓기 위함
#   2. 실수를 하지 않기 위함. 상수는 어떤일이 있어도 수정하지 않겠다는 의미이므로

# 원주율 파이
PI = 3.14

def calculate_area(r):
    return PI * r * r

radius = 4
print("반지름이 {}면, 넓이는 {}".format(radius, calculate_area(radius)))

radius = 6
print("반지름이 {}면, 넓이는 {}".format(radius, calculate_area(radius)))