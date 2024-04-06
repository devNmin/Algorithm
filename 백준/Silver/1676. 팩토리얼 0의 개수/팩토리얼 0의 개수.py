def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def check(_num):
    count = 0
    reversed_string = str(_num)[::-1]
    for string in reversed_string:
        if string == "0":
            count += 1
        else:
            return count


N = int(input())

num = factorial(N)

ans = check(num)
print(ans)
