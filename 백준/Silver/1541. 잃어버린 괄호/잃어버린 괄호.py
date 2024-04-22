tlst = input().split("-")

ans = 0
if tlst[0]:
    tt = list(map(int, tlst[0].split("+")))
    ans += sum(tt)

for t in tlst[1:]:
    tt = list(map(int, t.split("+")))
    ans -= sum(tt)
print(ans)