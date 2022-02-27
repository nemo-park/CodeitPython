# range
# 장점 : 간편함, 깔끔함, 메모리 효율성(1 쓰고 버리고 2 쓰고 버리고 등)

# for i in range(start, stop):
#     print(i)
# → start 부터 stop-1 까지의 범위

for i in range(3, 11):
    print(i)

print()

# 파라미터 1개 버전
# for i in range(stop):
#     print(i)
# → 0 부터 stop-1 까지의 범위

for i in range(10):
    print(i)

print()

# 파라미터 3개 버전
# for i in range(start, stop, step):
#     print(i)
# → 0 부터 stop-1 까지의 범위

for i in range(3, 17, 3):   # 3 ~ 16
    print(i)