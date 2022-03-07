
# 입력함수 input() 을 통해 들어오는 모든 값은 string 형태로 저장됨
x = input("입력값 : ")

print(x)
print(type(x))

print("동전 합산 서비스에 오심을 환영합니다.")
print("단, 음수는 입력하지 마세요.")

# 입력함수 input() 을 통해 들어오는 모든 값은 String 형태로 저장되므로 Int 형으로 변경
coin500 = int(input("500원짜리는 몇 개 입니까?"))
coin100 = int(input("100원짜리는 몇 개 입니까?"))

total = 500 * coin500 + 100 * coin100
print("손님의 동전은 총 {}원 입니다.".format(total))