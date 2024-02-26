
N, K = list(map(int,input().split()))
arr = list(range(0, N+1))
result = []
index = 0 

for n in range(N):
    result.append(str(arr.pop(index)))
    index += K - 1
    if index >= len(arr):
        index = index % len(arr)

result.extend(list(map(str,arr)))
result = result[1::]
answer = ", ".join(result)
print(f"<{answer}>")

