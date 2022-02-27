# 파라미터에 '기본값(default value)'을 설정할 수 있음
# 기본값을 설정해 두면, 함수를 호출할 때 꼭 파라미터에 값을 안 넘겨 줘도 됨
# ⇒ optional parameter

# ★ 옵셔널 파라미터는 꼭 마지막에!

def myself(name, age, nationality="Korea"):
    print("내 이름은 {}".format(name))
    print("내 나이는 {}살".format(age))
    print("국적은 {}".format(nationality))

myself("Pizza", 1, "USA")
print()
myself("Codeit", 1)


# Case : SyntaxError: non-default argument follows default argument
# def myself(name, nationality="USA", age):
#    print("내 이름은 {}".format(name))
#    print("내 나이는 {}살".format(age))
#    print("국적은 {}".format(nationality))

# myself("Pizza",  1)
# print()
# myself(("Codeit", "Korea", 1))

print()
print()

def myself(name, age=7, nationality="Korea"):
    print("내 이름은 {}".format(name))
    print("내 나이는 {}살".format(age))
    print("국적은 {}".format(nationality))

myself("Pizza", 1, "USA")
print()
myself("Codeit")