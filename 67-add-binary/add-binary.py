# binrary to 10
def bin_to_num(bin_str):
    multiple_x = 1
    sum = 0
    for i in range(len(bin_str),0,-1):
        sum += int(bin_str[i-1]) * multiple_x
        multiple_x *=2
    return sum
    
def num_to_bin(num_value):
    value = ""
    if num_value == 0:
        return "0"
    while num_value >= 1:
        if  num_value % 2 == 1:
            value = "1" + value
        else:
            value = "0" + value
        num_value = num_value//2
    return value
        
class Solution:
    
    def addBinary(self, a: str, b: str) -> str:
        sum_num_value = bin_to_num(a) + bin_to_num(b)
        print(sum_num_value)
        return num_to_bin(sum_num_value)