import sys
N = int(sys.stdin.readline())

for _ in range(N):
    test_list = list(sys.stdin.readline().split())
    result = ""
    for test_str in test_list:
        result += test_str[-1::-1]+' '
    print(result)