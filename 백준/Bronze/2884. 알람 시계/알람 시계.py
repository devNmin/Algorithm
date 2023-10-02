hour, min = list(map(int,input().split()))

if hour == 0:
    hour = 24
if min-45 < 0:
    hour -= 1
    min = 60+(min-45)
else:
    min -= 45
if hour ==24:
    hour = 0
print(hour,min)