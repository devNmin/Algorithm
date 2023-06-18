def d(n):
    n += sum(map(int,str(n)))
    return n

OrgValue = set(range(1,10001))
NonValue = set()

for i in range(1,10001):
    NonValue.add(d(i))

result = sorted(OrgValue-NonValue)
for i in result:
    print(i)