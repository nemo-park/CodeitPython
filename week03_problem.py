def C2F():

    # get Celsius
    celsius = int(input("섭씨 온도(C)를 입력하세요: "))
    # change scale to Fahrenheit
    fahrenheit = (celsius * 1.8) + 32
    # print result
    print("섭씨 온도(C) {}도는 화씨 온도(F) {}도 입니다.".format(celsius, fahrenheit))
    #################


def F2C():

    # get Fahrenheit
    fahrenheit = int(input("화씨 온도(F)를 입력하세요: "))
    # change scale to Celsius
    celsius = (fahrenheit - 32) / 1.8
    # print result
    print("화씨 온도(F) {}도는 섭씨 온도(C) {}도 입니다.".format(fahrenheit, celsius))
    #################


def Choose_mode() -> int:

    # choose scale change mode
    print("단위 환산")
    print("섭씨 온도(C)에서 화씨 온도(F)로 변환 = 1")
    print("화씨 온도(F)에서 섭씨 온도(C)로 변환 = 2")

    return int(input("선택하세요: "))
    #################


def Continue() -> bool:

    while True:
        # ask to continue
        input_bool = input("계속 하시겠습니까? (y/n): ")

        if input_bool == 'y':
            return True
        elif input_bool == 'n':
            return False
        else:
            continue

#################


def main():
    while True:
        choice = Choose_mode()
        if choice == 1:
            C2F()
        elif choice == 2:
            F2C()
        if not Continue():
            break


if __name__ == "__main__":
    main()