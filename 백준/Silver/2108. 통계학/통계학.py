N = int(input())
arr = []
for _ in range(N):
    arr.append(int(input()))

# [1] 산술평균: N개의 수들의 합을 N으로 나눈 값
avg = sum(arr) / (len(arr))
print(round(avg))
# [2] 중앙값: N개의 수들을 증가하는 순서로 나열했을 경우 그 중앙에 위치하는 값
sorted_arr = sorted(arr)
print(sorted_arr[N // 2])
# [3] 최빈값: N개의 수들 중 가장 많이 나타나는 값
arr_count = {}
for i in arr:
    if i not in arr_count:
        arr_count[i] = 1
    else:
        arr_count[i] += 1
max_value = max(arr_count.values())
check = []
for key, value in arr_count.items():
    if max_value == value:
        check.append(key)
check.sort()
print(check[1]) if len(check) > 1 else print(check[0])
# [4] 범위: N개의 수들 중 최댓값과 최솟값의 차이
print(sorted_arr[-1] - sorted_arr[0])