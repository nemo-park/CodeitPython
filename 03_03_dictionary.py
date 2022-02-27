# 사전 (dictionary)
# key-value pair (키-값 쌍)
# list와 비슷하지만, key는 순서의 개념이 없다
# list의 index는 0, 1, 2, 3 정수형이나, dictionary의 key는 정수형이지 않아도 됨

my_dictionary = {
    5: 25,
    2: 4,
    3: 9
}

print(type(my_dictionary))  # <class 'dict'>

print(my_dictionary[3])

my_dictionary[9] = 81
print(my_dictionary)

my_family = {
    '엄마': '이효리',
    '아빠': '이상순',
    '딸': '이상미'
}

print(my_family['엄마'])

print(my_family)


print("my_family.values()----------")
print('이효리' in my_family.values())
print('최웅' in my_family.values())

for value in my_family.values():
    print(value)


print("my_family.keys()----------")
print(my_family.keys())

for key in my_family.keys():
    value = my_family[key]
    print(key, value)

print("my_family.items()----------")
for key, value in my_family.items():
    print(key, value+)