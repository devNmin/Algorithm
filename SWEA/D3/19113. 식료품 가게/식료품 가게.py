T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    N = int(input())
    product = list(map(int, input().split()))

    # 75% 가격

    n = 0
    while n < N:
        for i in range(n + 1, N * 2):
            if product[n] * 4/3 == product[i]:
                product.__delitem__(i)
                break
        n += 1
    result = " ".join(str(e) for e in product)
    print(f"#{test_case} {result}")
    # ///////////////////////////////////////////////////////////////////////////////////
