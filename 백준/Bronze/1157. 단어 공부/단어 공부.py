visited = [0] * 26
temp = input()

for ele in temp:
    ele = ele.upper()
    for x in range(65, 91):
        if ele == chr(x):
            visited[x - 65] += 1

sorted_visited = sorted(visited, reverse=True)
if sorted_visited[0] == sorted_visited[1]:
    print("?")
else:
    max_v = -1
    count = 0
    idx = 0
    for v in visited:
        if v > max_v:
            max_v = v
            idx = count
        count += 1
    print(chr(65 + idx))
