# Return 문의 역할
# 1) 값 돌려주기
# 2) 함수 즉시 종료하기

def square(x):
    print("Function Start!")
    return x * x
    print("Function End!")  # return 문에서 함수가 종료되므로 여기까지 도달 X

print(square(3))
print("Hello World!")


def print_square(x):
    print(x * x)

def get_square(x):
    return x * x

print(get_square(3))


# print_square fuction 에는 별도의 return 문이 없음
# Python 에서는 별도의 return 문의 없으면, None 이 return 됨
# ⇒ print_square(3) 에 의해 9를 출력한 뒤,
#   함수 호출부분이 None 으로 대체됨
print(print_square(3))