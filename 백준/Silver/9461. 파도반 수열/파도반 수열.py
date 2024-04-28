def fun(n):
    global tlst
    if n not in tlst:
        value = fun(n - 2) + fun(n - 3)
        tlst[n] = value
        return value
    else:
        return tlst[n]


tlst = {
    1: 1,
    2: 1,
    3: 1,
}
T = int(input())

for _ in range(T):
    ans = fun(int(input()))
    print(ans)