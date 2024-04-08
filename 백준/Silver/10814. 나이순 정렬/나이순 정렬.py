N = int(input())
people = []

for i in range(1,N+1):
    age, name = list(input().split())
    people.append([i,int(age),name])

people.sort(key=lambda x:(x[1],x[0]))

for peop in people:
    result = str(peop[1]) + " " + peop[2]
    print(result)
