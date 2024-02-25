
n = int(input())

def my_fun(now):

    for _ in range(n):
        num = int(input())

        while now <= num:
            stack.append(now)
            result.append("+")
            now += 1

        if stack.pop() == num:
            result.append("-")
        else:
            return print("NO")
    for re in result:
        print(re)
now = 1
stack = []
result = []
my_fun(now)
            

        
