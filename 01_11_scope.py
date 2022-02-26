# Scope : 변수가 유효한 범위
# 로컬 변수 : 변수를 정의한 함수 내에서만 사용 가능
# 글로벌 변수 : 모든 곳에서 사용 가능
# 함수에서 변수를 사용할때, 로컬 변수를 먼저 찾고나서 글로벌 변수를 찾음

def my_function():
    x = 3
    print(x)

print("my_function()")
my_function()
# NameError: name 'x' is not defined
# x : my_function 함수 내에서 정의한 로컬변수
#     변수 x가 유효한 scope는 my_function 내부에서만!
# print(x)


# y : 글로벌 변수
y = 2

def my_function2():
    print(y)

print("my_function2()")
my_function2()
print(y)


# 글로벌 변수
z = 2

def my_function3():
    # 로컬 변수
    z = 3
    # 함수에서 변수 사용시 1) 로컬변수가 있는지 확인 2) 없으면, 글로벌 변수가 있는지 확인
    print(z)

print("my_function3()")
my_function3()
print(z)


# parameter도 로컬변수
def square(x):
    return x * x

print(square(3))