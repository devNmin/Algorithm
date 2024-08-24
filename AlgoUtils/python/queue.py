from collections import deque

queue = deque()
queue.append(1)  # enqueue
queue.append(2)
print(queue.popleft())  # 출력: 1 (FIFO)
print(queue[0])  # peek: 2
print(len(queue) == 0)  # is_empty: False
