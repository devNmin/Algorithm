
# 마이너스로 스플릿함 55-50+40 => ['55','50+40']
tlst = input().split("-")

ans = 0
if tlst[0]:     # 마이너스로 스플릿시에 맨앞 값이 존재하면 
    tt = list(map(int, tlst[0].split("+"))) # +로 스플릿해서 최종값에 합산
    ans += sum(tt)

for t in tlst[1:]: # 첫번째 이후 부터 똑같이 작업( -로 먼저 스플릿한거기때문에 뒤에 모든값이 -로 합산해줘야 최저값가능)
    tt = list(map(int, t.split("+")))
    ans -= sum(tt)      #따라서 뒷부분 모두 값 빼줌
print(ans)
