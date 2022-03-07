# calculator 라는 python 파일을 불러오겠다는 의미
# calculator.py : 모듈이라고 부름

# 1.
# import calculator

# print(calculator.add(2, 5))
# print(calculator.multiply(3, 4))

# 2.
# calculator 모듈을 불러올때 calc 라는 이름을 사용하겠다
# import calculator as calc

# print(calc.add(2, 5))
# print(calc.multiply(3, 4))

# calculator 라는 모듈에서 add, multiply 함수만 불러오겠다는 의미
from calculator import add, multiply, subtract
# from calculator import * 로 불러와도 되지만, 
# 이와같이 import 하는 경우, 출처가 불분명한 문제가 있음

print(add(2, 5))
print(multiply(3, 4))
# from calculator import add, multiply 까지만 불러왔다면 Error 발생
print(subtract(9, 2))