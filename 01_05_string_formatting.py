##### 자료형
# 05. format을 이용한 문자열 포멧팅

# 오늘은 2022년 2월 25일입니다.
year = 2022
month = 2
day = 25

# TypeError: can only concatenate str (not "int") to str
# print("오늘은 " + year + "년 " + month + "월 " + day + "일입니다.")

print("오늘은 " + str(year) + "년 " + str(month) + "월 " + str(day) + "일입니다.")

print("오늘은 {}년 {}월 {}일입니다.".format(year, month, day))

date_string = "오늘은 {}년 {}월 {}일입니다."
print(date_string.format(year, month, day))
print(date_string.format(year, month, day + 1))

print("저는 {}, {}, {}를 좋아합니다!".format("Pizza", "Pasta", "Sushi"))
# 0번 Pizza, 1번 Pasta, 2번 Sushi
print("저는 {1}, {0}, {2}를 좋아합니다!".format("Pizza", "Pasta", "Sushi"))

num_1 = 1
num_2 = 7
print("{0} 나누기 {1}은 {2}입니다.".format(num_1, num_2, num_1/num_2))
# 소숫점 둘째짜리로 반올림 .4f
print("{0} 나누기 {1}은 {2:.2f}입니다.".format(num_1, num_2, num_1/num_2))
# 소숫점 넷째짜리로 반올림 .4f
print("{0} 나누기 {1}은 {2:.4f}입니다.".format(num_1, num_2, num_1/num_2))
# 정수로 바꾸려면 .0f
print("{0} 나누기 {1}은 {2:.0f}입니다.".format(num_1, num_2, num_1/num_2))

name = "최웅"
age = 30
print(f"제 이름은 {name}이고 {age}살입니다.")