def solution(sizes):
    width = [ ]
    height = [ ]
    for size in sizes:
        width.append(max(size))
        height.append(min(size))
    max_w = max(width)
    max_h = max(height)
    answer = max_h * max_w
    return answer