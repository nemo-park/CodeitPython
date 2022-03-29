def triangle_dp() -> int:
    n, k = map(int, input("줄의 번호와 칸의 번호를 공백을 한 칸 두고 입력하세요: ").split())

    dp = []

    for i in range(n):
        pascal = []
        for j in range(i+1):
            if (j == 0) or (j == i):
                # 처음과 끝은 1로 저장
                pascal.append(1)
            else:
                # 파스칼 삼각형
                pascal.append(dp[i - 1][j - 1] + dp[i - 1][j])
        dp.append(pascal)

    return dp[n - 1][k - 1]
    #################


def main():
    print(triangle_dp())


if __name__ == "__main__":
    main()
