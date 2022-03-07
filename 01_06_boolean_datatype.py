##### 자료형
# 06. Boolean

print(True)
print(False)

print("AND 연산----------")
print(True and True)
print(True and False)
print(False and True)
print(False and False)

print("OR 연산----------")
print(True or True)
print(True or False)
print(False or True)
print(False or False)

print("NOT 연산----------")
print(not True)
print(not False)

print("문자열 연산----------")
print("Hello" == "Hello")
print("Hello" != "Hello")

print(2 > 1 and "Hello" == "Hello") # True

print("논리연산자")
print(not(False or ((not False) and True)))
# not False 가 True 이므로, 뒤에 볼 필요가 없이 True
print((not False) or ((not False)and True))
print(not False or not False and True)

print("단축계산 (Short-circuit Evaluation")
# 계산결과가 명확하면 필요없는 계산 생략
# 예) False and ?? >> False
#     True or ??   >> True
def loop():loop()

# Error
# print(True and loop())
# print(False or loop())
print("False and 면 뒤에 보지 않아도 False")
print(False and loop())
print(True or loop())

print(not not True)     # not False
print(not not False)    # not True

print(7 == 7 or (4 < 3 and 12 > 10))    # True or False

x = 3
print(x > 4 or not (x < 2 or x == 3))   # False or not True

print("비교논리식")
print(False == 0)
print(True == 1)