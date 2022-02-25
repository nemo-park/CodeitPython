##### 자료형
# 07. Type Function

# <class 'int'>
print(type(3))
# <class 'float'>
print(type(3.0))
# <class 'str'>
print(type("3"))

# <class 'str'>
print(type("True"))
# <class 'bool'>
print(type(True))


def hello():
    print("Hello World!")

# <class 'function'>
print(type(hello))
# <class 'builtin_function_or_method'>
print(type(print))