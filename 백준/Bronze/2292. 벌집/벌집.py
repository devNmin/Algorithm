N = int(input())
r = 1
s = 2
l = 7

while True:
    if N == 1:
        break
    r += 1
    if s <= N <= l:
        break
    s = l + 1
    l = s + ((6 * r) - 1)

print(r)
