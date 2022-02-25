# 추상화 (Abstration)
# 복잡한 내용은 숨기고 주요 기능에만 신경쓰면 됨
# 함수 (Function) : 명령 저장

burger_price = 4990
# 내장함수 : 기본 제공되는 함수 ex) print
print(burger_price)

# Function Header
# 파라미터 (Parameter)
#   함수에 넘겨주는 값
#   함수에 파라미터를 넘겨주면, 파라미터에 따라 함수가 조금씩 다르게 동작하도록 할 수 있다
def hello(name):
    print("Hello!")
    print(name)
    print("Welcome to Codeit!")

hello("Nemo")


def get_square(x):
    return x*x

print(get_square(3))
print(get_square(3) + get_square(4))