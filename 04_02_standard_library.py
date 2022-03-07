import math

print("1. math 모듈")
print(math.log10(100))
print(math.cos(0))
print(math.pi)
print()

# 랜덤한 숫자를 생성하기 위한 다양한 함수들을 제공
import random

print("2. random 모듈")
print(random.random())

# 두 수 사이의 랜덤한 정수 리턴
# a ≤ N ≤ b를 만족하는 어떤 랜덤한 정수 N을 리턴
print(random.randint(1, 20))
print(random.randint(1, 20))
print(random.randint(1, 20))

# 두 수 사이의 랜덤한 소수 리턴
# a ≤ N ≤ b를 만족하는 어떤 랜덤한 소수 N을 리턴
print(random.uniform(0, 1))
print(random.uniform(0, 1))
print(random.uniform(0, 1))
print()

# Python 으로 운영체제를 조작하기 위한 모듈
import os

print("3. operating system 모듈")
print(os.getlogin())
print(os.getcwd())
print()

# '날짜'와 '시간'을 다루기 위한 다양한 '클래스'
import datetime

print("4. datetime 모듈")
# 시간은 자동으로 00시 00분 00초로 설정
pi_day = datetime.datetime(2022, 3, 14)
print(pi_day)
print(type(pi_day))

pi_day = datetime.datetime(2022, 3, 14, 13, 6, 15)
print(pi_day)
print(type(pi_day))

today = datetime.datetime.now()
print(today)
print(type(today))

today = datetime.datetime.now()
pi_day = datetime.datetime(2022, 3, 14, 13, 6, 15)
print(today - pi_day)
# <class 'datetime.timedelta'> : 날짜 간의 차이를 나타내는 타입
print(type(today - pi_day))

today = datetime.datetime.now()
my_timedelta = datetime.timedelta(days=5, hours=3, minutes=10, seconds=50)

print(today)
print(today + my_timedelta)

today = datetime.datetime.now()

print(today)
print(today.year)  # 연도
print(today.month)  # 월
print(today.day)  # 일
print(today.hour)  # 시
print(today.minute)  # 분
print(today.second)  # 초
print(today.microsecond)  # 마이크로초


today = datetime.datetime.now()

print(today)
print(today.strftime("%A, %B %dth %Y"))

# 포맷 코드	설명	                            예시
# %a	    요일 (짧은 버전)	                Mon
# %A	    요일 (풀 버전)	                Monday
# %w	    요일 (숫자 버전, 0~6, 0이 일요일)	5
# %d	    일 (01~31)	                    23
# %b	    월 (짧은 버전)	                Nov
# %B	    월 (풀 버전)	                    November
# %m	    월 (숫자 버전, 01~12)	            10
# %y	    연도 (짧은 버전)	                16
# %Y	    연도 (풀 버전)	                2016
# %H	    시간 (00~23)	                    14
# %I	    시간 (00~12)	                    10
# %p	    AM/PM	                        AM
# %M	    분 (00~59)	                    34
# %S	    초 (00~59)	                    12
# %f	    마이크로초 (000000~999999)	    413215
# %Z	    표준시간대	                    PST
# %j	    1년 중 며칠째인지 (001~366)	    162
# %U	    1년 중 몇 주째인지 (00~53, 일요일이 한 주의 시작이라고 가정)	35
# %W	    1년 중 몇 주째인지 (00~53, 월요일이 한 주의 시작이라고 가정)	35