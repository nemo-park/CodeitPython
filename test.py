def calculate_change(payment, cost):
    target = payment - cost

    print("50000원 지폐: {}장".format(target // 50000))
    target -= (50000 * (target // 50000))

    print("10000원 지폐: {}장".format(target // 10000))
    target -= (10000 * (target // 10000))

    print("5000원 지폐: {}장".format(target //5000))
    target -= (5000 * (target // 5000))

    print("1000원 지폐: {}장".format(target // 1000))
    target -= (1000 * (target // 1000))


# 테스트
calculate_change(100000, 33000)
print()
calculate_change(500000, 378000)