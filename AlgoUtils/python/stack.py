stack = []
stack.append(1)  # push
stack.append(2)
print(stack.pop())  # 출력: 2 (LIFO)
print(stack[-1])  # peek: 1
print(len(stack) == 0)  # is_empty: False