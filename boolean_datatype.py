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

print(not not True)     # not False
print(not not False)    # not True

print(7 == 7 or (4 < 3 and 12 > 10))    # True or False

x = 3
print(x > 4 or not (x < 2 or x == 3))   # False or not True