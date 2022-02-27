# Aliasing

x = [2, 3, 5, 7, 11]
y = x   # y는 x의 가명 (alias)
y[2] = 4

print(x)
print(y)


# y를 바꾸면서 x를 유지하려면
x = [2, 3, 5, 7, 11]
y = list(x)
y[2] = 4

print(x)
print(y)