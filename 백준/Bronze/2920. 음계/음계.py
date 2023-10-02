sing = list(map(int, input().split()))


def check_song(_um):
    first = _um[0]
    for s in _um:
        if first == s:
            first += 1

    if first == 9:
        return print("ascending")

    else:
        return print("mixed")


def check_song2(_um):
    last = _um[0]
    for s in _um:
        if last == s:
            last -= 1

    if last != 0:
        return print("mixed")
    else:
        return print("descending")

if sing[0] == 1:
    check_song(sing)
elif sing[0] == 8:
    check_song2(sing)
else:
    print("mixed")
