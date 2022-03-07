# console 을 통해 사용자로부터 입력을 받는 함수

# input함수는 파라미터로 문자열을 넣을 수 있는데, 사용자에게 입력을 받기 전에 출력됨
# ⇒ 사용자에게 어떤값을 입력해야하는지 설명하는 용도로 사용
name = input("이름을 입력하세요: ")
print(name)

# input 함수가 받는 사용자 입력은 문자열
# val = input("숫자를 입력하세요: ")
# 문자열 + 정수를 더하려고 하여 오류 발생
# TypeError: can only concatenate str (not "int") to str
# print(val + 5)

val = int(input("숫자를 입력하세요: "))
print(val + 5)

