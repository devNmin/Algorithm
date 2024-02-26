_input = list(input())
arr = []
count = 0
for i in range(len(_input)):
    if _input[i] == "(":
        arr.append("(")
    else:
        if _input[i-1] == "(":
            arr.pop()
            count +=len(arr)
        else:
            arr.pop()
            count +=1
print(count)