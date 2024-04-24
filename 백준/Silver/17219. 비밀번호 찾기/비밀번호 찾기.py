N,M = list(map(int,input().split()))

password_dict = {}
for _ in range(N):
    a,b = list(input().split())
    password_dict[a] = b

for _ in range(M):
    a = input()
    print(password_dict[a])