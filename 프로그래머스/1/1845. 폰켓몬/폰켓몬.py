def solution(nums):
    num_len = len(nums)
    max_get = num_len // 2
    result = []
    for num in nums:
        if num not in result:
            result.append(num)
    if max_get > len(result):
        return len(result)
    else:
        return max_get