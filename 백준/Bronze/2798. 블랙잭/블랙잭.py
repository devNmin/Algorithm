def my_blj(n,target,nl): # 1 2 3 / 12 4/ 125 /134 /135 /145/234/235/345
  result = []
  target_pre = 0
  for i in range(n):
    for j in range(n):
      for k in range(n):
        if i != j and i !=k and j!=k:
          if nl[i]+nl[j]+nl[k] == target:
            return nl[i]+nl[j]+nl[k]
          if target>nl[i]+nl[j]+nl[k] and target_pre<=nl[i]+nl[j]+nl[k]:
            # print(i,j,k,target_pre)
            target_pre = nl[i]+nl[j]+nl[k] 
          
  return target_pre


number, value = map(int,input().split())  
number_list  = list(map(int,input().split()))
print(my_blj(number,value,number_list))