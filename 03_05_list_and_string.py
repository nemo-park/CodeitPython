# 리스트와 문자열은 굉장히 비슷합니다.
# 리스트가 어떤 자료형들의 나열이라면, 문자열은 문자들의 나열

# [공통점] 1. 인덱싱 (Indexing)

# 알파벳 리스트의 인덱싱
alphabets_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
print(alphabets_list[0])
print(alphabets_list[1])
print(alphabets_list[4])
print(alphabets_list[-1])

# 알파벳 문자열의 인덱싱
alphabets_string = 'ABCDEFGHIJ'
print(alphabets_string[0])
print(alphabets_string[1])
print(alphabets_string[4])
print(alphabets_string[-1])



# [공통점] 2. for 반복문
# 알파벳 리스트의 반복문
alphabets_list = ['C', 'O', 'D', 'E', 'I', 'T']
for alphabet in alphabets_list:
    print(alphabet)

# 알파벳 문자열의 반복문
alphabets_string = 'CODEIT'
for alphabet in alphabets_string:
    print(alphabet)



# [공통점] 3. 슬라이싱 (Slicing)
# 알파벳 리스트의 슬라이싱
alphabets_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
print(alphabets_list[0:5])
print(alphabets_list[4:])
print(alphabets_list[:4])

# 알파벳 문자열의 슬라이싱
alphabets_string = 'ABCDEFGHIJ'
print(alphabets_string[0:5])
print(alphabets_string[4:])
print(alphabets_string[:4])



# [공통점] 4. 덧셈 연산
# 두 자료형에게 모두 덧셈은 "연결"하는 연산입니다.
# 리스트의 덧셈 연산
list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8]
list3 = list1 + list2
print(list3)

# 문자열의 덧셈 연산
string1 = '1234'
string2 = '5678'
string3 = string1 + string2
print(string3)



# [공통점] 5. len 함수
# 리스트의 길이 재기
print(len(['H', 'E', 'L', 'L', 'O']))

# 문자열의 길이 재기
print(len("Hello, world!"))


# [차이점] 1. Mutable (수정 가능) vs. Immutable (수정 불가능)
# 리스트는 데이터를 바꿀 수 있지만, 문자열은 데이터를 바꿀 수 없음
# 'mutable'한 자료형 : 리스트와 같이 수정 가능한 자료형
# 'immutable'한 자료형 : 문자열과 같이 수정 불가능한 자료형, 숫자, 불린, 문자열은 모두 immutable한 자료형입니다.
numbers = [1, 2, 3, 4]
numbers[0] = 5
print(numbers)

name = 'codeit'
# name[0] = 'C'
# TypeError: 'str' object does not support item assignment
# ⇒  문자열은 리스트와 달리 데이터의 생성, 삭제, 수정이 불가능합니다. ***
# print(name)

# 아래 구문은 문자열을 수정한 것은 아니고,
# 문자열을 이용하여 새로운 문자열을 만들었기 때문에 Error 발생 X ***
name = 'codeit' + 'it'
print(name)


# 마지막 네 글자가 '*'로 대체되어야 합니다!
def mask_security_number(security_number):
    return security_number[:-4] + '****'