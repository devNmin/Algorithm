# 백준 알파벳 찾기 브2 10809

string = input()
alphabet_count = {chr(i): -1 for i in range(ord('a'), ord('z') + 1)}

for i in range(len(string)):
    if alphabet_count[string[i]] == -1:
        alphabet_count[string[i]] = i

result = list(map(str,alphabet_count.values()))

print(" ".join(result))